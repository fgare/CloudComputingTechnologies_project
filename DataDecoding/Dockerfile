# Usa una base image ufficiale di Python
FROM python:3.12

# Imposta la directory di lavoro nel container
WORKDIR /app

# Installa le dipendenze
RUN pip install dnspython==2.6
RUN pip install paho-mqtt==2.1.0
RUN pip install pymongo==4.8.0

# Copia il contenuto della directory attuale nella directory di lavoro nel container
COPY . .

RUN ls -l /app

# Definisce il comando di esecuzione predefinito
CMD ["python", "Receiver.py"]
