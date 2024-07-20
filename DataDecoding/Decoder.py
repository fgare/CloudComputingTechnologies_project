import datetime


class Decoder:
    def __init__(self):
        pass

    def decode_hex(hex_str):
        # Estrai la parte della stringa che rappresenta la data e l'ora
        data_ora_hex = hex_str[:12]
        numero_hex = hex_str[12:]

        # Converti la parte della data e dell'ora in un intero
        data_ora_int = int(data_ora_hex, 16)

        # Converti l'intero in una stringa che rappresenta la data e l'ora
        data_ora_str = str(data_ora_int).zfill(14)  # Aggiungi zeri iniziali se necessario

        # Estrai i componenti della data e dell'ora
        anno = int(data_ora_str[:4])
        mese = int(data_ora_str[4:6])
        giorno = int(data_ora_str[6:8])
        ora = int(data_ora_str[8:10])
        minuto = int(data_ora_str[10:12])
        secondo = int(data_ora_str[12:14])

        # Crea un oggetto datetime
        data_ora = datetime.datetime(anno, mese, giorno, ora, minuto, secondo)

        # Converti la parte del numero esadecimale in un intero
        numero = int(numero_hex, 16)
        print(data_ora, numero)

        return data_ora, numero
