from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Selamat Datang di Layanan Kantin FMIPA UGM</h1>'


@app.route('/diko')
def diko():
    return 'Ini halaman Diko'


@app.route('/diko/dikolagi')
def diko1():
    return 'Ini halaman Diko lagi'


@app.route('/kantin1')
def kantin1():
    menu = ["Nasi Rames", "Buah", "Es Jeruk", "Es Teh"]
    return render_template("kantin1.html", menu=menu)


if __name__ == '__main__':
    app.run()
