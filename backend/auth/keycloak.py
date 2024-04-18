from flask_oidc import OpenIDConnect
from functools import wraps
from graphql import GraphQLError

class Keycloak:
    def __init__(self, app):
        self.oidc = OpenIDConnect(app)

    def require_keycloak_token(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not self.oidc.user_loggedin:
                raise GraphQLError('Authentication required!')
            return f(*args, **kwargs)
        return decorated
