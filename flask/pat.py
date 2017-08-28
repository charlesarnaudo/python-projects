from flask import Flask
import nflgame

app = Flask(__name__)
@app.route("/")

def hello():
    return "Hello World"

def okay():
    return "wtf"
