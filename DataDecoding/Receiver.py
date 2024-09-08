import time
import paho.mqtt.client as mqtt
from MeasureManager import MeasureManager
from Useful import Useful

TOPIC = 'data/#'

class Receiver:
    def __init__(self):
        self.logger = Useful.getLogger('Decoding-receiver')

    def _connect(self):
        while True:
            try:
                client = mqtt.Client()
                client.on_connect = self.on_connect
                client.on_message = self.on_message
                client.connect('localhost', 1883, 60)
                # client.username_pw_set(username='federico', password='mosquitto')
                return client
            except Exception as e:
                self.logger.error("Failed connecting to MQTT broker\n" + str(e))
                time.sleep(5)

    def on_message(self, client, userdata, msg):
        MeasureManager(msg.topic, msg.payload.decode()).write_measure()
        self.logger.info("Received " + msg.payload.decode())

    def on_connect(self, client, userdata, flags, rc):
        self.logger.info("Connected to MQTT broker with result code "+str(rc))
        client.subscribe(TOPIC)

    def run(self):
        self.logger.info("Avviato")
        client = self._connect()
        client.loop_forever()


if __name__ == '__main__':
    Receiver().run()
