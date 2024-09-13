import time
import redis
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
                r = redis.Redis(host='redis', port=6379, decode_responses=True)
                self.logger.info(f'Connected to Redis\n{r}')
                return r
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
