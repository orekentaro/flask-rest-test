from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required
from routes.auth import auth

app = Flask(__name__)
app.config.from_object("utils.config")
CORS(app, supports_credentials=True)
app.register_blueprint(auth)
app.secret_key = "gwdfsgfadsdtyhjyetdgfsag0-a04o31qw@pa]:q12wegiejq8@43uqow"
jwt = JWTManager()
jwt.init_app(app)


@app.route("/", methods=["GET"])
@jwt_required()
def test():
    print(request.headers)
    return "OK"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
