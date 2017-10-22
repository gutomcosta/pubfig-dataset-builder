import csv 

class ImageFile(object):

    def __init__(self,path):
        self.path = path
    
    def get_images_data(self):
        images_data = []
        try:
            file = open(self.path, 'r')
            lines = csv.reader(file,delimiter='\t') 
            for line in lines:
                images_data.append(
                    {
                    "name": line[0],
                    "url": line[2],
                    "box": line[3]
                    }
                )
            return images_data
            file.close()
        except Exception as e:
            print "error "+e.message
