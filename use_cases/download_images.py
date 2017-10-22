from services import Downloader
from services import FaceExtractor
from services import ImageFile

import os
class DownloadImages(object):

    @classmethod
    def build(cls, image_file_path, base_path):
        return cls(ImageFile(image_file_path),Downloader(base_path),FaceExtractor()) 
    
    def __init__(self,image_file, downloader, face_extractor):
        self.image_file = image_file
        self.downloader = downloader
        self.face_extractor = face_extractor

    def execute(self):
        images_data = self.image_file.get_images_data()
        for image_data in images_data:
            try:
                print "downloading {0} ...".format(image_data['url'])
                path = self.downloader.download(image_data)
                self.face_extractor.extract_face(path)
                os.remove(path)
            except Exception as e:
                print 'Error Download'
                # print "Error downloading "+image_data['url']+" - "+e.message