import paho.mqtt.client as mqtt
from MeasureManager import MeasureManager

TOPIC = 'data/#'


class Receiver():
    def __init__(self):
        pass

    def _connect(self):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.connect('localhost', 1883, 60)
        client.on_message = self.on_message
        return client

    def on_message(self, client, userdata, msg):
        MeasureManager(msg.topic, msg.payload.decode()).write_measure()

    def run(self):
        print("Avviato")
        client = self._connect()
        client.subscribe(TOPIC)
        client.loop_forever()


if __name__ == '__main__':
    Receiver().run()
