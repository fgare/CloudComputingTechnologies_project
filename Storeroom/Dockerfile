# Usa una base image ufficiale di Python
FROM python:3.12

# Imposta la directory di lavoro nel container
WORKDIR /app

# Installa le dipendenze
RUN pip install dnspython==2.6
RUN pip install paho-mqtt==2.1.0
RUN pip install minio

# Copia il contenuto della directory attuale nella directory di lavoro nel container
COPY . .

# Definisce il comando di esecuzione predefinito
CMD ["python", "DataReceiver.py"]
