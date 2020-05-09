from flask import Flask
import logging
import json


app = Flask(__name__)
logger = logging.Logger("Ubuntu Docker Flask App", logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# Setup console logging
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)


@app.route("/")
def home_page():
    logger.info("Inside Ubuntu - Flask Home Page ...")
    return json.dumps({"Status Code": 200, "Message": "Welcome to Flask - Home Page"})



# Redirect any unknown url to home page
@app.errorhandler(404)
def page_not_found(e):
    return json.dumps({"Status Code": 404, "Message": "Page Not Found"})


if __name__ == "__main__":
    app.run()
