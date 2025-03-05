import os
import unittest
import shutil
import hashlib
from bw64packer import unpack, pack

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
TEMP_DIR = os.path.join(os.path.dirname(__file__), "temp")

UNPACKED_FILE_NAMES = ["adm.xml", "audio", "chna.json", "format.json"]

class UnpackTests(unittest.TestCase):

    def setUp(self):
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)
        os.makedirs(TEMP_DIR)

    def test_unpack(self):
        file_path = os.path.join(DATA_DIR, "test_bwf.wav")
        unpack(file_path, os.path.join(TEMP_DIR, "test_bwf"))
        self._assert_unpacked("test_bwf.wav")

    def test_pack(self):
        file_path = os.path.join(DATA_DIR, "test_bwf.wav")
        unpacked_dir = os.path.join(TEMP_DIR, "test_bwf")
        repacked_file_path = os.path.join(TEMP_DIR, "test_bwf.wav")
        unpack(file_path, unpacked_dir)
        pack(unpacked_dir, repacked_file_path)

        self._assert_file_sizes_are_the_same(file_path, repacked_file_path)


    def _assert_unpacked(self, src_file_name):
        dirname = os.path.splitext(src_file_name)[0]
        expected_file_path = os.path.join(TEMP_DIR, dirname)
        self.assertTrue(os.path.exists(expected_file_path))

        for file_path in UNPACKED_FILE_NAMES:
            self.assertTrue(os.path.exists(os.path.join(expected_file_path, file_path)))

    def _assert_file_sizes_are_the_same(self, file_one, file_two):
        size_1 = os.path.getsize(file_one)
        size_2 = os.path.getsize(file_two)
        self.assertEqual(size_1, size_2)


    def _assert_file_are_the_same(self, file_one, file_two):

        hash_1 =  self._file_sha(file_one)
        hash_2 =  self._file_sha(file_two)
        self.assertEqual(hash_1, hash_2)

    def _file_sha(self, file_path):

        BUF_SIZE = 65536

        sha1 = hashlib.sha1()

        with open(file_path, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)

        return sha1.hexdigest()