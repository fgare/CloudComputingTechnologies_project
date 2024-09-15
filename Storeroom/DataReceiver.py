import time
import redis
from StoreConnector import StoreConnector
from Useful import Useful


class DataReceiver:
    def __init__(self):
        self.logger = Useful.getLogger('DataReceiver')
        self.server = self._connect()

    def _connect(self):
        while True:
            try:
                r = redis.Redis(host='redis', port=6379, decode_responses=True)
                self.logger.info(f'Connected to Redis\n{r}')
                return r
            except Exception as e:
                self.logger.error("Connection failed\n" + str(e))
                time.sleep(5)

    def listen(self):
        listener = self.server.pubsub()
        listener.psubscribe('data.*')  # iscrizione secondo un pattern
        for message in listener.listen():
            print(message)
            if message['type'] == 'pmessage' or message['type'] == 'message':
                content = message['data']
                channel = message['channel']
                hierarchy = channel.split('.')
                StoreConnector(hierarchy[1], hierarchy[2], content).run()
                self.logger.info(f"Received {content} on channel {channel}")


    def run(self):
        self.logger.info("Started")
        self.listen()


if __name__ == '__main__':
    DataReceiver().run()
