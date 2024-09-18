from flask import Flask, request, jsonify
from datetime import datetime

class APIService:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()
        self.last_update = datetime.now()

    def setup_routes(self):
        @self.app.route('/health', methods=['GET'])
        def post_data():
            health_status = {
                "last_update": self.last_update,
                "status": "ok"
            }

            return jsonify(health_status), 200

    def run(self, host='localhost', port=5000):
        self.app.run(host=host, port=port)

    def update(self):
        self.last_update = datetime.now()


if __name__ == '__main__':
    api = APIService()
    api.run()
