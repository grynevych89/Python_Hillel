from flask import Flask, request
from utils import generate_passwords

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/password")
def password():
    length_str = request.args.get('length', '10')
    if not length_str.isdigit():
        return 'Length should be a digit'

    length = int(length_str)

    if length <= 0:
        return 'Length should be positive'

    if length > 1000:
        return 'Password is too long'

    return generate_passwords(length)


if __name__ == '__main__':
    app.run()
