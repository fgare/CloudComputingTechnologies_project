from Decoder import Decoder
from DBConnector import DBConnector


class MeasureManager:
    def __init__(self, topic, datum):
        self.topic = topic
        self.datum = datum
        self.decode_packet()

    def decode_packet(self):
        self.datum = Decoder.decode_hex(self.datum)
        print("Datum ", self.datum)

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
        return DBConnector(self._prepare_document())
