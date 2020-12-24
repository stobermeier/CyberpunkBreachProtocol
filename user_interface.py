import os
from flask import Flask, render_template, request
import solver_handler

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('enter_hexdump.html')


# route and function to handle the upload page
@app.route('/', methods=['GET', 'POST'])
def enter_hexdump_page():
    if request.method == 'POST':
        e00 = request.form['e00']
        e01 = request.form['e01']
        e02 = request.form['e02']
        e03 = request.form['e03']
        e04 = request.form['e04']
        e05 = request.form['e05']

        e10 = request.form['e10']
        e11 = request.form['e11']
        e12 = request.form['e12']
        e13 = request.form['e13']
        e14 = request.form['e14']
        e15 = request.form['e15']

        e20 = request.form['e20']
        e21 = request.form['e21']
        e22 = request.form['e22']
        e23 = request.form['e23']
        e24 = request.form['e24']
        e25 = request.form['e25']

        e30 = request.form['e30']
        e31 = request.form['e31']
        e32 = request.form['e32']
        e33 = request.form['e33']
        e34 = request.form['e34']
        e35 = request.form['e35']

        e40 = request.form['e40']
        e41 = request.form['e41']
        e42 = request.form['e42']
        e43 = request.form['e43']
        e44 = request.form['e44']
        e45 = request.form['e45']

        e50 = request.form['e50']
        e51 = request.form['e51']
        e52 = request.form['e52']
        e53 = request.form['e53']
        e54 = request.form['e54']
        e55 = request.form['e55']

        hexdump = [[e00, e01, e02, e03, e04, e05],
                   [e10, e11, e12, e13, e14, e15],
                   [e20, e21, e22, e23, e24, e25],
                   [e30, e31, e32, e33, e34, e35],
                   [e40, e41, e42, e43, e44, e45],
                   [e50, e51, e52, e53, e54, e55]
                   ]

        ram = request.form['ram']
        d1 = request.form['d1']
        d2 = request.form['d2']
        d3 = request.form['d3']

        solver_handler.breach(hexdump, ram, d1, d2, d3)

        return render_template('enter_hexdump.html')


if __name__ == '__main__':
    app.run()
