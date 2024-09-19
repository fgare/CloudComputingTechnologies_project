FROM python:3.12

WORKDIR /app

RUN pip install dnspython==2.6
RUN pip install minio
RUN pip install redis
RUN pip install Flask==2.0.1
RUN pip install Werkzeug==2.2.2

COPY . .

CMD ["python", "DataReceiver.py"]
