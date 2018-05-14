from flask import Flask

from oauth2 import current_token, require_oauth

app = Flask(__name__)

@app.route("/")
@require_oauth('user:email')
def hello():
    return "Hello World. Token scope = '{}'.\n".format(current_token.scope)
