import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    value = os.getenv('PORT')
    return f'У меня получилось! Переменная окружения PORT = {value}'


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.getenv('PORT', default=5000)),
    )
