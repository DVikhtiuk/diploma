from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return render_template("index.html")


@app.route('/bye')
def bye():
    return "See you later"


@app.route('/<string:name>')
def greeting(name):
    return f'hello, {name}'


if __name__ == "__main__":
    app.run(debug=True)