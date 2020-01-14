## Dash Authorization and Login

Docs: [https://plot.ly/dash/authentication](https://plot.ly/dash/authentication)

License: MIT

Tests: [![CircleCI](https://circleci.com/gh/plotly/dash-auth.svg?style=svg)](https://circleci.com/gh/plotly/dash-auth)

For local testing, install and use tox:

```
TOX_PYTHON_27=python2.7 TOX_PYTHON_36=python3.6 tox
```

Or create a virtualenv, install the dev requirements, and run individual
tests or test classes:

```
virtualenv venv
source venv/activate
pip install -r dev-requirements.txt
python -m unittest -v tests.test_plotlyauth.ProtectedViewsTest
```

Note that Python 2.7.7 or greater is required.

----------------------------------------------------------------------------------------------------
Cookie extension:

import dash_auth_cookie

# third parameter is a list of login cookies
auth = dash_auth_cookie.BasicAuth(
        app,
        VALID_USERNAME_PASSWORD_PAIRS,
        {'somename': 'somevalue'}
 )

Then if a cookie with name "somename" and value "somevalue" is present login will be granted. Normal login via username and password is still possible.
