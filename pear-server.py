#!/usr/bin/env python3
import http.server, json, os, datetime

DATA_FILE = os.path.expanduser('~/pear-data.json')

def load():
    try:
        with open(DATA_FILE) as f:
            return json.load(f)
    except:
        return {}

def save(d):
    with open(DATA_FILE, 'w') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.expanduser('~'), **kwargs)

    def log_message(self, format, *args):
        pass  # ログ抑制

    def send_cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors()
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/data':
            data = load()
            body = json.dumps(data, ensure_ascii=False).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_cors()
            self.end_headers()
            self.wfile.write(body)
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/collect':
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))
            data = load()
            now = datetime.datetime.now().isoformat()
            for word, info in body.items():
                if word not in data:
                    data[word] = {
                        'count': 0,
                        'type': info.get('type', 'katakana'),
                        'override': None,
                        'first_seen': now,
                        'last_seen': now
                    }
                else:
                    data[word]['last_seen'] = now
                data[word]['count'] = data[word].get('count', 0) + info.get('count', 1)
            save(data)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_cors()
            self.end_headers()
            self.wfile.write(b'{"ok":true}')

        elif self.path == '/api/save':
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))
            save(body)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_cors()
            self.end_headers()
            self.wfile.write(b'{"ok":true}')

if __name__ == '__main__':
    port = 8765
    print(f'Pear server running at http://localhost:{port}')
    http.server.HTTPServer(('', port), Handler).serve_forever()
