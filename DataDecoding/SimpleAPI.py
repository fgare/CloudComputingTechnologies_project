from flask import Flask, request, jsonify
from DBConnector import DBConnector

class SimpleAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/api/data', methods=['POST'])
        def post_data():
            # Recupera i dati dal corpo della richiesta JSON
            data = request.get_json()

            # Verifica se i dati sono validi
            if not data:
                return jsonify({"error": "No data provided"}), 400

            # Esempio di elaborazione dei dati ricevuti
            response_data = {
                "received_data": data,
                "message": "Data successfully received!"
            }

            DBConnector(data)

            return jsonify(response_data), 200

    def run(self, host='0.0.0.0', port=5000):
        self.app.run(host=host, port=port)

# Istanzia e avvia l'API
if __name__ == '__main__':
    api = SimpleAPI()
    api.run()
