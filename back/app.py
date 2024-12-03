
import cv2
from io import BytesIO
from PIL import Image
import tensorflow as tf
from tensorflow.keras import layers
from flask import Flask, request, jsonify
import io
import matplotlib.pyplot as plt

app = Flask(__name__)




from PIL import Image, ImageOps
import numpy as np


def save_preprocessed_image(blob,save_path):
    image = Image.open(io.BytesIO(blob))

    image = image.resize((28, 28), Image.BILINEAR)
    image_with_backround = Image.new("RGB", image.size,(255,255,255))
    image_with_backround.paste(image, (0, 0), image)


    image_with_backround.save(save_path, format='PNG')
    return image_with_backround





@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/model', methods=['POST', 'GET'])
def process():

    save_preprocessed_image(request.files['image'].read(), "recieved_digit.png")

    model = tf.keras.models.load_model("mnist_model.h5")
    img = cv2.imread(f"recieved_digit.png")[:, :, 0]
    img = np.invert(np.array([img]))
    img = img / 255
    prediction = model.predict(img)
    return jsonify({"result": f"{str(np.argmax(prediction))}"})

if __name__ == '__main__':
    app.run(debug=True)

