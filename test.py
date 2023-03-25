from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/user/<username>')
@app.route('/user/')
def show_user_profile(username=None):
    if username is None:
        username = request.args.get('username')
        if username:
            return 'User %s' % username
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)

