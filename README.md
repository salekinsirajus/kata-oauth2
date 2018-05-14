Demonstration of a Flask REST API protected by OAuth2.

# Server (protected resource)

```
pip install -r requirements.txt

FLASK_DEBUG=1 FLASK_APP=app.py flask run
```

# Client (client credentials authorization grant)

If a real Authorization Server is available that supports the "Client
Credentials" authorization grant, then edit the `OAuthClient` settings in
`client.py` and uncomment the call to `fetch_access_token`. Otherwise a fake
token will be used.

Then run:

```
$ python client.py
```

Or (with fake token):

```
$ curl --header 'Authorization: Bearer dca6f1125fb4874e058887a098dadf91f0e1e70d' 'http://127.0.0.1:5000/'
```

Expected output:

```

Hello World. Token scope = 'user:email'.

```

Note that the server (protected resource) currently only checks that it
received a token, not whether the token is actually valid. Validation should be
added using JWT, Token Introspection, or consulting a shared database with the
Authorization Server.
