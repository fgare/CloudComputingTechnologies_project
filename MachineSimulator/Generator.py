import datetime
import time
from Sender import Sender
import random
import threading


class Generator(threading.Thread):
    def __init__(self, customer, machine):
        threading.Thread.__init__(self)
        self.customer = customer
        self.machine = machine
        self.topic = 'data/' + customer + '/' + machine
        self.sender = Sender(self.topic)

    def run(self):
        mean = random.randint(0, 100)
        while True:
            # genera valore random del +/-10% intorno alla media
            value = int(random.random()*(1.2*mean - 0.8*mean) + 0.8*mean)
            now = datetime.datetime.now()
            self.sender.publish(now, value)
            print("Invio ", now, ", ", value)
            time.sleep(5)


if __name__ == "__main__":
    Generator('customer1', 'machine1').run()
