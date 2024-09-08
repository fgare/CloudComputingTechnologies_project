import datetime
import time
import uuid
from io import BytesIO
from minio import Minio
from Useful import Useful

minio_url = "minio:9000"  # URL del server MinIO
access_key = "federico"  # Chiave di accesso MinIO
secret_key = "federico"  # Chiave segreta MinIO


class StoreConnector:
    def __init__(self, customer_name: str, machine_name: str, obj: str):
        self.client = self._connect()
        self.bucket_name = customer_name
        self.machine_name = machine_name
        self.object = obj
        self.logger = Useful.getLogger('StoreConnector')
        self.logger.info("Connected to Minio")

    def _connect(self) -> Minio:
        while True:
            try:
                return Minio(minio_url, access_key=access_key, secret_key=secret_key, secure=False)
            except Exception as e:
                self.logger.error("Connection failed")
                self.logger.error(e)
                time.sleep(5)

    def create_bucket(self) -> bool:
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)
            return True
        return False

    def write_string(self, bucket_name: str, data: str):
        object_as_stream = BytesIO(data.encode('utf-8'))
        object_name = self._generate_unique_filename()
        self.client.put_object(bucket_name, object_name, object_as_stream, len(data), content_type="text/plain")

    def _generate_unique_filename(self) -> str:
        current_time = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        unique_id = uuid.uuid4()
        return f"{self.machine_name}_{current_time}_{unique_id}"

    def run(self):
        # print("Started")
        self.create_bucket()
        self.write_string(self.bucket_name, self.object)
        print("Written")


if __name__ == "__main__":
    i = 0
    while True:
        StoreConnector("customertest", "machinetest", f"value_{i}").run()
        i+=1
        time.sleep(5)

