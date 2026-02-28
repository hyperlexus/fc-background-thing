from http.server import BaseHTTPRequestHandler
import json
import requests


class Handler(BaseHTTPRequestHandler):
    def do_post(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        pid = data.get('pid')

        response = requests.post("http://rwfc.net/api/pinfo", json={"pid": pid})

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response.json()).encode())