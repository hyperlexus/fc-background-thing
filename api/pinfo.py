from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/api/pinfo', methods=['POST'])
def get_pinfo():
    data = request.get_json(force=True)
    pid = data.get('pid')
    headers = {'User-Agent': 'Mozilla/5.0'}

    print(f"Testing PID: {pid} from my IP...")

    try:
        response = requests.post("https://rwfc.net/api/pinfo", json={"pid": pid}, headers=headers, timeout=10)
        print(f"Status Code: {response.status_code}")
        return jsonify(response.json())
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible to your whole local network
    app.run(host='0.0.0.0', port=5000)