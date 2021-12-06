from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Digital Cloud Nest</h1>"

@app.route('/information')
def info():
    return "<h1>We help clients to move into cloud or manage their environments.</h1>"

if __name__ == '__main__':
    app.run()