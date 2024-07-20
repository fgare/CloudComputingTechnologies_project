import paho.mqtt.client as mqtt
import datetime

'''
def _on_publish(client, userdata, mid):
    print("Published ")
'''


class Sender:
    def __init__(self, topic: str):
        self.broker = self._connect()
        self.topic = topic

    # si connette al server mqtt
    def _connect(self) -> mqtt.Client:
        client = mqtt.Client()
        # client.on_publish = _on_publish
        client.connect('localhost', 1883, 60)
        return client

    def publish(self, dt: datetime, value):
        self.broker.publish(self.topic, self._preparePacket(dt,value), qos=0)

    # converte le informazioni in esadecimale prima che vengano inviate
    def _preparePacket(self, dt: datetime, value: int):
        # Converti la data e l'ora in esadecimale
        data_ora_hex = dt.strftime('%Y%m%d%H%M%S')
        data_ora_hex = hex(int(data_ora_hex))[2:]  # rimuove 0x

        # Converti il numero in esadecimale
        numero_hex = hex(value)[2:]

        # Concatenazione dei valori esadecimali
        risultato = data_ora_hex + numero_hex

        return risultato