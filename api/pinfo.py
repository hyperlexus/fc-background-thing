from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/api/pinfo', methods=['POST'])
def get_pinfo():
    data = request.get_json()
    pid = data.get('pid')

    try:
        response = requests.post("http://rwfc.net/api/pinfo", json={"pid": pid})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)