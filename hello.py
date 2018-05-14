from flask import Flask

from oauth2 import current_token, require_oauth

app = Flask(__name__)

@app.route("/")
@require_oauth('foo')
def hello():
    return "Hello World. Token scope = '{}'.\n".format(current_token.scope)
