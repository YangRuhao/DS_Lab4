from flask import Flask, request, jsonify
import random, string

app = Flask(__name__)
db = {}

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.json['url']
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    db[code] = long_url
    return jsonify({"shortcode": code, "status": "success"})

@app.route('/lookup/<code>')
def lookup(code):
    return jsonify({"url": db.get(code)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
