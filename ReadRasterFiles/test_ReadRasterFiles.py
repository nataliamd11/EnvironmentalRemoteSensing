import os
import unittest

from dotenv import load_dotenv
from osgeo import gdal

from ReadRasterFiles import ReadRasterFiles

load_dotenv() 

class TestReadRasterFilesGdal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._instance = ReadRasterFiles()
        cls._test_folder_path = os.environ.get('FOLDER_PATH')
        cls._test_file_path = os.environ.get('FILE_PATH')
        cls._test_wrong_file_type = os.environ.get('WRONG_FILE_TYPE')
        cls._test_wrong_path = "This is not a path"
        

    def tearDown(self):
        self._instance._ReadRasterFiles__rpath = ""

    def test__is_folder_path(self):
        ''' test if True when path is a folder, False if it is a file path, or
        raise and error when path is invalid '''

        is_folder = self._instance._ReadRasterFiles__is_folder_path

        # empty path
        with self.assertRaises(TypeError):
            is_folder()

        # folder path
        self._instance._ReadRasterFiles__rpath = self._test_folder_path
        self.assertTrue(is_folder())

        # file path
        self._instance._ReadRasterFiles__rpath = self._test_file_path
        self.assertFalse(is_folder())

        # wrong path
        self._instance._ReadRasterFiles__rpath = self._test_wrong_path
        with self.assertRaises(TypeError):
            is_folder()

        # wrong file type
        self._instance._ReadRasterFiles__rpath = self._test_wrong_file_type
        self.assertFalse(is_folder())


    def test_read_singleband_rasters(self):
        read_multiband = self._instance._ReadRasterFiles__read_multiband_raster

        self._instance._ReadRasterFiles__rpath = self._test_wrong_file_type
        with self.assertRaises(RuntimeError):
            read_multiband()

        self._instance._ReadRasterFiles__rpath = self._test_file_path
        self.assertIsInstance(read_multiband(), gdal.Dataset)



if __name__ == '__main__':
    unittest.main()
