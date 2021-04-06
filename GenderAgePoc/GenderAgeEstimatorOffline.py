from facelib import FaceDetector, AgeGenderEstimator
from utils import draw_boxes
import cv2

class GenderAgeEstimatorOffline:
    def __init__(self, device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")):
        print('loading ...') 
        self.face_detector = FaceDetector(device=device)
        self.age_gender_detector = AgeGenderEstimator(device=device)

    def predict(self, image, show=False):


		faces, boxes, scores, landmarks = self.face_detector.detect_align(image)
		genders, ages = self.age_gender_detector.detect(faces)

		 
        if draw:
        	if len(faces.shape) > 1:
        		frame = image.copy()
	            for i, b in enumerate(boxes):
	            	# create new image and draw on it
	                draw_boxes(frame, b, landmarks[i], name=genders[i]+' '+str(ages[i]))
	        cv2.imshow('frame', frame)
	        if cv2.waitKey(1) == ord('q'):
				cv2.destroyAllWindows()


		return genders, ages