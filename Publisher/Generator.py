import datetime
import time
from Publisher.Sender import Sender
import random

TOPIC = "data/customer1/machine1"


class Generator:
    def __init__(self):
        self.sender = Sender(TOPIC)

    def run(self):
        mean = random.randint(0, 100)
        while True:
            # genera valore random del +/-10% intorno alla media
            value = int(random.random()*(1.2*mean - 0.8*mean) + 0.8*mean)
            now = datetime.datetime.now()
            self.sender.publish(now, value)
            print("Invio ", now, ", ", value)
            time.sleep(2)


if __name__ == "__main__":
    Generator().run()
