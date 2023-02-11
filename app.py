from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/orders', methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        tel = request.form["tel"]
        name = request.form["name"]
        return render_template("thanks.html")
    return render_template("orders.html")


@app.route('/pricing')
def get_pricing():
    return render_template('pricing.html')


@app.route('/testimonials')
def get_testimonials():
    return render_template('testimonials.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/features')
def get_features():
    return render_template('features.html')


if __name__ == "__main__":
    app.run(debug=True)