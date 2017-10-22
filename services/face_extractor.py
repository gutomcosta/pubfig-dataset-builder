import cv2

from skimage.feature import hog
from skimage import data, color, exposure
from skimage import io
from skimage import img_as_ubyte
import os

import dlib


class FaceExtractor(object):

    def extract_face(self, path):
        image = io.imread(path)
        cv_image = img_as_ubyte(image)
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        detector = dlib.get_frontal_face_detector()
        detected_faces = detector(gray)
        print("I found {} faces in the file".format(len(detected_faces)))
        faces = []
        for i, face_rect in enumerate(detected_faces):
            img = image[face_rect.top():face_rect.bottom(), face_rect.left():face_rect.right()]
            faces.append(img)

        self.save_faces(faces, path)


    def save_faces(self, faces, path):
        path_splited = path.split("/")
        file_name = path_splited[-1]
        file_name = file_name+"_face"
        for i, img in enumerate(faces):
            name = "{0}{1}.jpg".format(file_name,str(i))
            complete_path = "{0}/{1}/{2}".format(path_splited[0],path_splited[1],name)
            cv2.imwrite(complete_path, img)


















