import time
import redis
from MeasureManager import MeasureManager
from Useful import Useful


class Receiver:
    def __init__(self):
        self.logger = Useful.getLogger('Decoding-receiver')
        self.server = self._connect()

    def _connect(self) -> redis.Redis:
        while True:
            try:
                r = redis.Redis(host='redis', port=6379, decode_responses=True)
                self.logger.info(f'Connected to Redis\n{r}')
                return r
            except Exception as e:
                self.logger.error("Failed connecting to redis\n" + str(e))
                time.sleep(5)


    def listen(self):
        listener = self.server.pubsub()
        listener.psubscribe('data.*')  # iscrizione secondo un pattern
        for message in listener.listen():
            print(message)
            if message['type'] == 'pmessage' or message['type'] == 'message':
                content = message['data']
                channel = message['channel']
                MeasureManager(channel, content).write_measure()
                # self.logger.info(f"Received {content} on channel {channel}")

    def run(self):
        self.logger.info("Avviato")
        server = self._connect()
        self.listen()


if __name__ == '__main__':
    Receiver().run()
