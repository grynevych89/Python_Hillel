from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def main():
    return '''
        <li class="menu__item"><a href="/requirements" class="menu__link">requirements</a></li>
        <li class="menu__item"><a href="/generate_users" class="menu__link">generate_users</a></li>
        <li class="menu__item"><a href="/space" class="menu__link">space</a></li>
    '''


@app.route("/requirements")
def requirements():
    return utils.requirements()


@app.route("/generate_users")
def generate_users():
    return utils.generate_users()


@app.route("/space")
def space():
    return utils.space()


if __name__ == '__main__':
    app.run()
