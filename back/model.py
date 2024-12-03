import cv2
import tensorflow as tf
import numpy as np



class Model:
    def __init__(self,model_path):
        self.model = None
        self.load_model(model_path)

    def load_model(self, model_path):
        try:
            self.model = tf.keras.models.load_model(model_path)
        except Exception:
            raise Exception("model couldn't be loaded")

    def classify(self, image_path):
        img = cv2.imread(image_path)[:, :, 0]
        img = np.invert(np.array([img]))
        img = img / 255
        prediction = self.model.predict(img)
        return np.argmax(prediction)