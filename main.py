from flask import Flask, render_template, request, send_from_directory
from poet import write
from mail import send
from post import write_on_img, send_line

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        if int(request.form["id"])==1:	#寫詩
            n = int(request.form["n"])
            style = int(request.form["style"])
            re = write(n, style)
            return render_template('main.html', poem=re)
        else:	#下載
            p = request.form["poem"]
            poem_list = p[2:-2].split("', '")
            ptext=""
            for line in poem_list:
                line = line.replace("\\n", "\n")
                ptext += line
            if int(request.form["id"])==3:	#要影印
                send_line(ptext)
            re = write_on_img(ptext).save("data/pc.png")
            return send_from_directory('data', "pc.png", as_attachment=True)

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