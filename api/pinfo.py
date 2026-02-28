from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/api/pinfo', methods=['POST'])
def get_pinfo():
    try:
        requests.get("https://google.com", timeout=2)
    except Exception as e:
        return jsonify({"error": "Vercel has no internet access", "details": str(e)}), 500

    try:
        data = request.get_json()
        pid = data.get('pid')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.post("https://rwfc.net/api/pinfo", json={"pid": pid}, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)