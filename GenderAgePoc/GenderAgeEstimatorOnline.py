from facelib import FaceDetector
from facelib import AgeGenderEstimator
from facelib import special_draw
import torch
import cv2
import numpy as np

class GenderAgeEstimatorOnline:
    def __init__(self, device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")):
        print('loading ...') 
        self.face_detector       = FaceDetector(device=device)
        self.age_gender_detector = AgeGenderEstimator(device=device)

    def __mapAge(self, age):
        bins = [0, 10, 18, 25, 35, 45, 55, 65]
        names = ['<10', '10-18', '18-25', '25-35', '35-45', '45-55', '55-65', '65+']
        d = dict(enumerate(names, 1))
        return str(np.vectorize(d.get)(np.digitize(age, bins)))


    def run(self, camera_index=0):
        cap = cv2.VideoCapture(camera_index)
        cap.set(3, 640)
        cap.set(4, 480)
        print('type q for exit')
        while cap.isOpened():
            ret, frame = cap.read()
            if ret == False:
                raise Exception('the camera not recognized: change camera_index param to ' + str(0 if camera_index == 1 else 1))
            faces, boxes, scores, landmarks = self.face_detector.detect_align(frame)
            if len(faces.shape) > 1:
                genders, ages = self.age_gender_detector.detect(faces)
                print(genders, ages)
                for i, b in enumerate(boxes):
                    special_draw(frame, b, landmarks[i], name=genders[i]+' '+str(self.__mapAge(ages[i])))

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break

        cv2.destroyAllWindows()
