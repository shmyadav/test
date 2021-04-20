import json
from flask import Flask, request

app = Flask(__name__)

def multiplyer(a,c):
    return a*c

@app.route("/result")
def result():

    return "Done"

if __name__ == '__main__':
    app.run()