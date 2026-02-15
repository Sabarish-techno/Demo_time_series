from flask import Flask, render_template, request
from ml_model import run_forecast
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    
    if request.method == "POST":
        file = request.files["file"]
        result = run_forecast(file)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
