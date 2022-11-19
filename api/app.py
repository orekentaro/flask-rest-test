from flask import Flask
from flask_cors import CORS
from routes.auth import auth

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(auth)
app.secret_key = "gwdfsgfadsdtyhjyetdgfsag0-a04o31qw@pa]:q12wegiejq8@43uqow"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
