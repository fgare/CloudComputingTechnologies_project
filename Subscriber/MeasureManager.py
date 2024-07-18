from Subscriber.Decoder import Decoder
from Subscriber.DBConnector import DBConnector


class MeasureManager:
    def __init__(self, topic, datum):
        self.topic = topic
        self.datum = datum

    def decode(self):
        self.datum = Decoder().decode_hex(self.datum)

    def _get_topic_hierarchy(self):
        return self.topic.split('/')

    def _prepare_document(self):
        hierarchy = self._get_topic_hierarchy()
        document = {
            "customer": hierarchy[-2],
            "machine": hierarchy[-1],
            "date": self.datum[0],
            "EE": self.datum[1]
        }
        return document

    def write_measure(self):
        return DBConnector().insert_document(self._prepare_document())
