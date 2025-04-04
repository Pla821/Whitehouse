
from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

DATA_FILE = "country_impact.json"

@app.route("/")
def index():
    return render_template("map.html")

@app.route("/impact/<country>")
def impact(country):
    country = country.lower()
    data = load_data()
    results = data.get(country, [])
    return jsonify(results)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

if __name__ == "__main__":
    app.run(debug=True)
