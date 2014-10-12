from core import app

@app.route("/")
def hello():
    return "<h1>Hello Flask</h1>"
