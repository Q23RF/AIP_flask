from flask import Flask, render_template, request
from poet import write

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        n = int(request.form["n"])
        len = int(request.form["len"])
        poet = int(request.form["poet"])
        re = write(n, len, poet)  #.replace('\n', '<br>')
        return render_template('main.html', poem=re)
    else:
        return render_template('main.html', poem='')


@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    return render_template('feedback.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


app.run(host='0.0.0.0', port=81)
