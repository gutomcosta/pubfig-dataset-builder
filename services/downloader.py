import requests
import os


class Downloader(object):

    def __init__(self, base_path):
        self.base_path = base_path
    
    def download(self,image_data):
        try:
            path= '{0}/{1}'.format(self.base_path, image_data["name"])
            url = image_data['url']
            file_name = url.split("/")[-1]
            if not os.path.exists(path):
                os.makedirs(path)
            complete_path = path+"/"+file_name 
            file = open(complete_path, 'wb')
            file.write(requests.get(image_data['url']).content)
            file.close()
            return complete_path
        except Exception as e:
            print "Error downloading: {0} - {1} ".format(image_data["url"], e.message)