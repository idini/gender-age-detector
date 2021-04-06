from facelib import FaceDetector, AgeGenderEstimator
from facelib import special_draw
import cv2
import torch

class GenderAgeEstimatorOffline:
	def __init__(self, device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")):
		print('loading ...') 
		self.face_detector		 = FaceDetector(device=device)
		self.age_gender_detector = AgeGenderEstimator(device=device)

	def __mapAge(self, age):
        bins = [0, 10, 18, 25, 35, 45, 55, 65]
        names = ['<10', '10-18', '18-25', '25-35', '35-45', '45-55', '55-65', '65+']
        d = dict(enumerate(names, 1))
        return str(np.vectorize(d.get)(np.digitize(age, bins)))

	def predict(self, image, draw=False):
		faces, boxes, scores, landmarks = self.face_detector.detect_align(image)
		genders, ages 					= self.age_gender_detector.detect(faces)

		if draw:
			if len(faces.shape) > 1:
				frame = image.copy()
				for i, b in enumerate(boxes):
					# create new image and draw on it
					special_draw(frame, b, landmarks[i], name=genders[i]+' '+str(self.__mapAge(ages[i])))
			cv2.imshow('frame', frame)
			if cv2.waitKey(1) == ord('q'):
				cv2.destroyAllWindows()

		return genders, ages