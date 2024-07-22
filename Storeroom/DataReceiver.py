import paho.mqtt.client as mqtt
from StoreConnector import StoreConnector

TOPIC = 'data/#'


class DataReceiver:
    def __init__(self):
        pass

    def _connect(self):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.connect('mosquitto', 1883, 60)
        client.on_message = self.on_message
        return client

    def on_message(self, client, userdata, msg):
        hierarchy = msg.topic.split('/')
        StoreConnector(hierarchy[1], hierarchy[2], msg.payload.decode()).run()

    def run(self):
        print("Avviato")
        client = self._connect()
        print("Connesso")
        client.subscribe(TOPIC)
        client.loop_forever()


if __name__ == '__main__':
    DataReceiver().run()
