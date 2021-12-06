from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Digital Cloud Nest.</h1>"

@app.route('/about')
def about():
    return "<h1>We are Google Cloud Platform consultant.</h1>"

@app.route('/client/<name>')
def clients(name):
    return "<h1>Welcome {} onboard with us.</h1>".format(name)

@app.route('/debug/<name>')
def debugmode(name):
    try:
        return "<h1>10th letter of name {}</h1>".format(name[9])   
    except:
        return "<h1>Name does not have 10th letter {}</h1>".format(name) 

if __name__ == '__main__':
    app.run(debug=True)