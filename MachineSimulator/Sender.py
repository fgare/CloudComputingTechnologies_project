from multiprocessing.connection import Client

import paho.mqtt.client as mqtt
import datetime


class Sender:
    def __init__(self, topic: str):
        self.broker = self._connect()
        self.topic = topic

    # si connette al server mqtt
    def _connect(self) -> mqtt.Client:
        try:
            client = mqtt.Client()
            client.on_publish = self._on_publish
            client.on_connect = self._on_connect
            client.on_connect_fail = self._on_connect_fail
            client.connect('localhost', 1883, 60)
            # client.username_pw_set(username='federico', password='mosquitto')
            print(f"Connected to MQTT Broker\n{client}")
            return client
        except Exception as e:
            print("Failed connecting to MQTT broker\n" + str(e))
            return None

    def publish(self, dt: datetime, value):
        self.broker.publish(self.topic, self._preparePacket(dt,value), qos=1)

    @staticmethod
    def _on_publish(client, userdata, mid):
        print(f"Published {mid}")

    @staticmethod
    def _on_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT Broker with result code "+str(rc))

    def _on_connect_fail(self, client, userdata, flags, rc):
        print("Connection to MQTT broker failed")

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