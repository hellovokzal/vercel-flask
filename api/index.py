from os import *

system("pip install time")

from flask import Flask, Response
from time import *

num = 0
text = ""

app = Flask(__name__)

@app.route("/<path:message>")
def echo(message):
    global num
    global text
    text = message + "\n"
    num = 1
    return "OK"

@app.route("/stream")
def stream():
    def chat():
        global num
        global text
        while True:
            sleep(1)
            if num == 1:
                num = 0
                yield text
    return Response(chat(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
