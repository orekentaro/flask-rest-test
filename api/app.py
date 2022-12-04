from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

import utils.middleware as mw
from routes.auth import auth
from routes.job_seeker import job_seeker

app = Flask(__name__)
app.config.from_object("utils.config")
CORS(app, supports_credentials=True)
app.register_blueprint(auth)
app.register_blueprint(job_seeker)
app.secret_key = "gwdfsgfadsdtyhjyetdgfsag0-a04o31qw@pa]:q12wegiejq8@43uqow"
jwt = JWTManager()
jwt.init_app(app)
app.before_request(mw.before_request)
app.after_request(mw.after_request)
app.register_error_handler(Exception, mw.exception_handler)
app.register_error_handler(ValueError, mw.value_error_handler)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
