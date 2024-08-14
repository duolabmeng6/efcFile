import os
import unittest
from efcFile.providers.S3FileStorage import S3FileStorage
from dotenv import load_dotenv


class Test文件储存桶s3(unittest.TestCase):

    def test_s3(self):
        load_dotenv()
        storage = S3FileStorage(
            access_key=os.getenv('s3_access_key'),
            secret_key=os.getenv('s3_access_secret'),
            endpoint_url=os.getenv('s3_endpoint_url'),
            bucket_name='llef',
            path_prefix='test/'
        )
        storage.put("example.txt", b"This is a test file")
        print(storage.get("example.txt"))
        print(storage.exists("example.txt"))
        print(storage.size("example.txt"))
        print(storage.mime_type("example.txt"))
        print(storage.list(""))
        storage.move("example.txt", "example_moved.txt")
        print(storage.exists("example_moved.txt"))
        storage.delete("example_moved.txt")
