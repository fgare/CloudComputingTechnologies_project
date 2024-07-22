from pymongo import MongoClient

DBNAME = "cct"
COLLECTION = "measurements"


class DBConnector:
    def __init__(self):
        self.server = None
        self.db = None
        self.collection = None
        self._connect()

    def _close_connection(self):
        if self.server:
            self.server.disconnect()
            print('Disconnected from server')

    def __del__(self):
        self._close_connection()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close_connection()

    def _connect(self):
        server = MongoClient('192.168.1.4', 27017)
        self.db = server[DBNAME]
        self.collection = self.db[COLLECTION]
        print("Connected to MongoDB")

    def insert_document(self, document):
        result = self.collection.insert_one(document)
        print(f"Document inserted with _id: {result.inserted_id}")
        return result.inserted_id


if __name__ == "__main__":
    connector = DBConnector()
    doc = {
        "customer": "customer1",
        "machine": "machine1",
        "date": '2024-07-18T18:05:05Z',
        "EE": 32
    }
    connector.insert_document(doc)