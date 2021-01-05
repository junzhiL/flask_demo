from flask import Flask, render_template
from jinja2 import escape


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s kkkkk profile'.format(escape(username))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    app.logger.debug('debug')
    app.logger.warning('warning')
    app.logger.error('error')
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
