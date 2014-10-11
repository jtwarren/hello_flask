from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask"

app.run(host='0.0.0.0', threaded=True, debug=True)
