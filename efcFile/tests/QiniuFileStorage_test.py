import unittest
from efcFile.providers.QiniuFileStorage import QiniuFileStorage
from dotenv import load_dotenv
import os


class Test文件储存桶qn(unittest.TestCase):

    def test_qn(self):
        load_dotenv()
        storage = QiniuFileStorage(
            access_key=os.getenv('qiniu_access_key'),
            secret_key=os.getenv('qiniu_access_secret'),
            domain=os.getenv('qiniu_domain'),
            bucket_name='testgoefun',
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
