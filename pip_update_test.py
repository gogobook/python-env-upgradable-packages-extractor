import unittest
import os, shutil
from datetime import date
from pip_update import extract, CMD


class TestExtractMethods(unittest.TestCase):
    def setUp(self):
        extract(CMD,folder='pip-update-test')

    def test_cmd(self):
        self.assertEqual(CMD, 'pip list --outdated --format json')

    def test_create_folder(self):
        self.assertTrue(os.path.exists('./pip-update-test'))
    
    def test_create_file(self):
        today = date.today().strftime('%Y%m%d')
        self.assertTrue(os.path.exists('./pip-update-test/update.txt'))
        self.assertTrue(os.path.exists('./pip-update-test/current'+today+'.txt'))


    def tearDown(self):
        shutil.rmtree('./pip-update-test')

if __name__ == '__main__':
    unittest.main()