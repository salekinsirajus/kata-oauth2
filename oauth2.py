import time

from authlib.flask.oauth2 import ResourceProtector, current_token
from authlib.specs.rfc6750 import BearerTokenValidator


class Token:
    def __init__(self, client_id=None, access_token=None, refresh_token=None, scope=None, revoked=None,
                 issued_at=None, expires_in=None):
        self.client_id = client_id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.scope = scope
        self.revoked = revoked
        self.issued_at = issued_at
        self.expires_in = expires_in

    def get_scope(self):
        return self.scope

    def get_expires_in(self):
        return self.expires_in

    def get_expires_at(self):
        return self.issued_at + self.expires_in


class MyBearerTokenValidator(BearerTokenValidator):
    def authenticate_token(self, token_string):
        # TODO: actually verify token_string. Either JWT or Token
        # Introspection or shared database.
        return Token(
            issued_at=time.time(),
            expires_in=100,
            scope='foo',
            revoked=False,
        )

    def request_invalid(self, request):
        return False

    def token_revoked(self, token):
        return token.revoked


ResourceProtector.register_token_validator(MyBearerTokenValidator())
require_oauth = ResourceProtector()
