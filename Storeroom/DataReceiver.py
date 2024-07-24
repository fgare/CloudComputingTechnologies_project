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
                client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
                client.connect(HOST, 1883, 60)
                client.username_pw_set(username='federico', password='mosquitto')
                client.on_message = self.on_message
                return client
            except Exception as e:
                self.logger.error("Connection failed\n" + str(e))
                time.sleep(5)

    def on_message(self, client, userdata, msg):
        hierarchy = msg.topic.split('/')
        StoreConnector(hierarchy[1], hierarchy[2], msg.payload.decode()).run()
        self.logger.info(f"Received {msg.payload.decode()}")

    def run(self):
        self.logger.info("Started MQTT connection")
        client = self._connect()
        client.subscribe(TOPIC)
        self.logger.debug("Connected and subscribed to MQTT server")
        client.loop_forever()


if __name__ == '__main__':
    DataReceiver().run()
