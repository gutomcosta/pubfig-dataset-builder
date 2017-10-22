# coding: utf-8
from datetime import date, datetime

from mock import patch, Mock

import unittest

from use_cases import DownloadImages

class DownloadImagesTest(unittest.TestCase):

    def setUp(self):
        self.image_file = Mock()
        self.downloader = Mock()
        self.image_repository = Mock()
        self.use_case = DownloadImages(self.image_file,self.downloader, self.image_repository)
        self.image_data = { "name": 'Abhishek Bachan', "url": 'http://1.bp.blogspot.com/_Y7rzCyUABeI/SNIltEyEnjI/AAAAAAAABOg/E1keU_52aFc/s400/ash_abhishek_365x470.jpg'}
        self.downloader.download.return_value='image1'
        self.image_file.get_images_data.return_value = [ self.image_data ]
    def test_it_read_urls_from_file(self):
        self.use_case.execute()
        self.image_file.get_images_data.assert_called_with()
    
    def test_for_each_image_data_it_download_image(self):
        self.use_case.execute()
        self.downloader.download.assert_called_with('http://1.bp.blogspot.com/_Y7rzCyUABeI/SNIltEyEnjI/AAAAAAAABOg/E1keU_52aFc/s400/ash_abhishek_365x470.jpg')

    def test_for_each_image_downloaded_it_write_in_disk(self):
        self.use_case.execute()
        self.image_repository.save.assert_called_with(self.image_data, 'image1')