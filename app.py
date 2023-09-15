from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/refundandcancellation')
def refundandcancellation():
    return render_template('refund.html')

@app.route('/privacypolicy')
def privacypolicy():
    return render_template('privacypolicy.htm')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/shipping')
def shipping():
    return render_template('shippinganddelivery.html')

@app.route('/termsandconditions')
def termsandconditions():
    return render_template('termsandconditions.htm')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True)
