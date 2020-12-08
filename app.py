from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/railfence')
def railfence():
    return render_template("railfence.html")


@app.route('/vigenere')
def vigenere():
    return render_template("vigenere.html")


@app.route('/caesar')
def caesar():
    return render_template("caesar.html")


@app.route('/diffie')
def diffie():
    return render_template("diffie.html")


@app.route('/frequency')
def frequency():
    return render_template("frequency.html")

if __name__ == '__main__':
    app.run()
