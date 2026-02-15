from flask import Flask, render_template, request
from model import forecast_timeseries

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    
    if request.method == "POST":
        file = request.files["file"]
        result = forecast_timeseries(file)

    return render_template("index.html", result=result)

app.run(debug=True)
