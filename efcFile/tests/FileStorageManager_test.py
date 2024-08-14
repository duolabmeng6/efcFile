import unittest
from efcFile.providers.LocalFileStorage import LocalFileStorage
from efcFile.managers.FileStorageManager import FileStorageManager

class Test文件存储管理器(unittest.TestCase):

    def test_文件储存器(self):
        local_storage = LocalFileStorage("./storage/")
        manager = FileStorageManager(default_storage="local")
        manager.set_storage("local", local_storage)
        s1 = LocalFileStorage("./s1/")
        manager.set_storage("s1", s1)
        manager.disk("s1").put("example.txt", b"This is a test file")
        manager.put("example.txt", b"This is a test file")

        # manager.put("example.txt", b"This is a test file")
        # print(manager.get("example.txt"))
        # print(manager.exists("example.txt"))
        # print(manager.size("example.txt"))
        # print(manager.mime_type("example.txt"))
        # print(manager.list(""))
        # manager.move("example.txt", "example_moved.txt")
        # print(manager.exists("example_moved.txt"))
        # manager.delete("example_moved.txt")