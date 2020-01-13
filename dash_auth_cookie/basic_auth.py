from .auth import Auth
import base64
import flask


class BasicAuth(Auth):
    def __init__(self, app, username_password_list, cookie_name_value_list={}):
        Auth.__init__(self, app)
        self._users = username_password_list \
            if isinstance(username_password_list, dict) \
            else {k: v for k, v in username_password_list}
        self._cookies = cookie_name_value_list \
            if isinstance(cookie_name_value_list, dict) \
            else {k: v for k, v in cookie_name_value_list}

    def is_authorized(self):
        # If cookie authorization enabled
        if self._cookies:
            for cookie in flask.request.cookies:
                if self._cookies.get(cookie) == flask.request.cookies[cookie]:
                    return True

        header = flask.request.headers.get('Authorization', None)
        if header:
            username_password = base64.b64decode(header.split('Basic ')[1])
            username_password_utf8 = username_password.decode('utf-8')
            username, password = username_password_utf8.split(':')
            return self._users.get(username) == password
        else:
            return False

    def login_request(self):
        return flask.Response(
            'Login Required',
            headers={'WWW-Authenticate': 'Basic realm="User Visible Realm"'},
            status=401)

    def auth_wrapper(self, f):
        def wrap(*args, **kwargs):
            if not self.is_authorized():
                return flask.Response(status=403)

            response = f(*args, **kwargs)
            return response
        return wrap

    def index_auth_wrapper(self, original_index):
        def wrap(*args, **kwargs):
            if self.is_authorized():
                return original_index(*args, **kwargs)
            else:
                return self.login_request()
        return wrap
