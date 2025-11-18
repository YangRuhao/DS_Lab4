from flask import Flask, redirect
import requests

app = Flask(__name__)
SHORTENER_URL = "http://shortener-service:5001"

@app.route('/<code>')
def go(code):
    r = requests.get(f"{SHORTENER_URL}/lookup/{code}")
    return redirect(r.json()["url"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
