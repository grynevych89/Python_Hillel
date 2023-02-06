from flask import Flask
from faker import Faker

app = Flask(__name__)
fake = Faker()


@app.route("/requirements")
def requirements():
    req = open('requirements.txt', 'r')
    return req


@app.route("/faker")
def faker():
    names = []
    for i in range(100):
        names.append(i)
    return names


if __name__ == '__main__':
    app.run()
