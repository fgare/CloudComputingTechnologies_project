import time

import paho.mqtt.client as mqtt
from StoreConnector import StoreConnector
from Useful import Useful

HOST = 'mosquitto'  # indirizzo del server MQTT
TOPIC = 'data/#'


class DataReceiver:
    def __init__(self):
        self.logger = Useful.getLogger('DataReceiver')

    def _connect(self):
        while True:
            try:
                client = mqtt.Client()
                client.on_message = self.on_message
                client.on_connect = self.on_connect
                client.connect(HOST, 1883, 60)
                # client.username_pw_set(username='federico', password='mosquitto')
                return client
            except Exception as e:
                self.logger.error("Connection failed\n" + str(e))
                time.sleep(5)

    def on_message(self, client, userdata, msg):
        hierarchy = msg.topic.split('/')
        StoreConnector(hierarchy[1], hierarchy[2], msg.payload.decode()).run()
        self.logger.info(f"Received {msg.payload.decode()}")

    def on_connect(self, client, userdata, flags, rc):
        self.logger.info(f"Connected with {HOST}, result code {rc}")
        client.subscribe(TOPIC, qos=1)

    def run(self):
        self.logger.info("Started MQTT connection")
        client = self._connect()
        self.logger.debug("Connected and subscribed to MQTT server")
        client.loop_forever()


if __name__ == '__main__':
    DataReceiver().run()
