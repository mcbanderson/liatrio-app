from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Home page</p>"


@app.route("/about")
def about_me():
    return "<p>About me!</p>"


@app.route("/contact")
def contact_me():
    return "<p>Contact me!</p>"


if __name__ == "__main__":
    app.run()
