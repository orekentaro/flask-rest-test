from flask import Flask
from flask_cors import CORS
from routes.route import ln, lr

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(lr)
app.register_blueprint(ln)
app.secret_key = "内緒"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
