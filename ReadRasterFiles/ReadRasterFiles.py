import os

from osgeo import gdal

gdal.UseExceptions()


class ReadRasterFiles():
    '''
    Reads Multiband or Single Band Raster files.
    Assings bands interpretation when its possible, and let the user change it.
    '''
    
    def __init__(self):
        self.satellite = ""
        self.__rpath = ""

    def read_raster(self, 
                    rpath:str, 
                    satellite:str="landsat", 
                    file_type:str='tif'):
        self.satellite = satellite
        self.__rpath = rpath
        if self.__is_folder_path():
            self.__read_singleband_rasters()
            rmerged = self.__merge_singleband_raster()
        else:
            rmerged = self.__read_multiband_raster()

    def __is_folder_path(self):
        if os.path.isdir(self.__rpath):
            return True
        if os.path.isfile(self.__rpath):
            return False
        if not os.path.isdir(self.__rpath) and not os.path.isdir(self.__rpath):
            raise TypeError("Invalid path")

    def __read_singleband_rasters(self):
        pass

    def __merge_single_band_layers(self):
        pass

    def __read_multiband_raster(self):
        mbraster = gdal.Open(self.__rpath)
        if not isinstance(mbraster, gdal.Dataset):
            raise TypeError("Invalid Raster")
        return mbraster

    def __is_valid_directory(self):
        if not os.path.isdir(self.__folder_path):
            self.__folder_path = ""
            raise TypeError("Path to folder expected. Please provide a valid path to the folder.")
        return True
