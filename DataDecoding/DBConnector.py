from pymongo import MongoClient
import threading
from Useful import Useful

DBNAME = "cct"
COLLECTION = "measurements"


class DBConnector(threading.Thread):
    def __init__(self, document: dict):
        super().__init__()
        self.server = None
        self.db = None
        self.collection = None
        self.document = document
        self.logger = Useful.getLogger('mongoConnector')
        self.start()

    def _close_connection(self):
        if self.server:
            self.server.disconnect()
            self.logger.debug('Disconnected from server')

    def __del__(self):
        self._close_connection()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close_connection()

    def _connect(self):
        try:
            server = MongoClient(host='mongodb',
                                 port=27017)
            self.db = server[DBNAME]
            self.collection = self.db[COLLECTION]
            self.logger.debug("Connected to MongoDB")
        except Exception as e:
            self.logger.error("Failed to connect to MongoDB\n" + str(e))

    def insert_document(self):
        result = self.collection.insert_one(self.document)
        self.logger.info(f"Document inserted with _id: {result.inserted_id}")
        return result.inserted_id

    def run(self):
        self._connect()
        doc_id = self.insert_document()


if __name__ == "__main__":
    doc = {
        "customer": "customer1",
        "machine": "machine1",
        "date": '2024-07-18T18:05:05Z',
        "EE": 32
    }
    connector = DBConnector(doc)
    connector.insert_document()