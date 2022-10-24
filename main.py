from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from poet import write
from mail import send
from generate import write_on_img
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        if int(request.form["id"])==2:

            print("generating img...")
            p = request.form["poem"]
            poem_list = p[2:-2].split("', '")
            ptext=""
            for line in poem_list:
                ptext += line[:-2] + '\n'
                print(line)
            re = write_on_img(ptext).save("data/pc.png")
            return send_from_directory('data', "pc.png", as_attachment=True)


        else:
            n = int(request.form["n"])
            len = int(request.form["len"])
            style = int(request.form["style"])
            re = write(n, len, style)
            return render_template('main.html', poem=re)


    else:
        return render_template('main.html', poem='')


@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        fb = request.form["fb"]
        send(fb)
    return render_template('feedback.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

app.run(host='0.0.0.0', port=81)