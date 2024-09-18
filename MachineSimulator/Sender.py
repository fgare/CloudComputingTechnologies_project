import redis
import datetime


class Sender:
    def __init__(self, topic: str):
        self.server:redis.Redis = self._connect()
        self.topic = topic

    def __del__(self):
        self.server.close()

    # si connette al server redis
    def _connect(self) -> redis.Redis:
        try:
            r = redis.Redis(
                host='localhost',
                port=6379,
                username='customer',
                password='customerpass',
                db=0,
                decode_responses=True)
            print(f"Connected to Redis server\n{r}")
            return r
        except Exception as e:
            print("Failed connecting to MQTT broker\n" + str(e))
            return None

    def publish(self, dt: datetime, value:int):
        self.server.publish(self.topic, self._prepare_packet(dt, value))
        print("Published ", value, " on topic ", self.topic)

    # converte le informazioni in esadecimale prima che vengano inviate
    @staticmethod
    def _prepare_packet(dt: datetime, value: int) -> hex:
        # Converti la data e l'ora in esadecimale
        data_ora_hex = dt.strftime('%Y%m%d%H%M%S')
        data_ora_hex = hex(int(data_ora_hex))[2:]  # rimuove 0x

        # Converti il numero in esadecimale
        numero_hex = hex(value)[2:]

        # Concatenazione dei valori esadecimali
        risultato = data_ora_hex + numero_hex

        return risultato