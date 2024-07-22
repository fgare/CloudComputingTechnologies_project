from StoreConnector import StoreConnector


class Bridge:
    def __init__(self, topic: str, object: str):
        self.topic = topic
        self.object = object

    def preparePacket(self):
        hierarchy = self.topic.split('/')
        StoreConnector(hierarchy[1], self.object)