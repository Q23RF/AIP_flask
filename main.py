from flask import Flask, render_template, redirect, request, url_for, jsonify
from poet import write
import requests

app = Flask(__name__)
printurl = 'https://poem-receiver-for-aip.elsie094081.repl.co/'

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        n = int(request.form["n"])
        len = int(request.form["len"])
        style = int(request.form["style"])
        re = write(n, len, style)  #.replace('\n', '<br>')
        return render_template('main.html', poem=re)
    else:
        return render_template('main.html', poem='')


@app.route('/feedback', methods=["POST", "GET"])
def feedback():
  return render_template('feedback.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/route_function',methods=[ "GET",'POST'])
def route_function():
      return "default text"

app.run(host='0.0.0.0', port=81)