import utils.middleware as mw
from create_app import APP
from routes.auth import auth
from routes.job_seeker import job_seeker

app = APP

# route
app.register_blueprint(auth)
app.register_blueprint(job_seeker)
app.before_request(mw.before_request)
app.after_request(mw.after_request)

# error handler
app.register_error_handler(Exception, mw.exception_handler)
app.register_error_handler(ValueError, mw.value_error_handler)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
