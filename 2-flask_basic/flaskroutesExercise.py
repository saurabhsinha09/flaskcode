from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Name change of puppies into Latin</h1>"

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    old_name = name
    if name[-1] == 'y':
        name = name[:-1] + 'iful'
    else:
        name += 'y'
    return "<h1>{} in latin is {}</h1>".format(old_name, name)

if __name__ == '__main__':
    app.run()