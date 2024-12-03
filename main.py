import os

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# # Cargar el dataset MNIST
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
#
# # Normalizar los datos de entrada al rango [0, 1]
# x_train = x_train.astype("float32") / 255
# x_test = x_test.astype("float32") / 255
#
# # Redimensionar las imágenes a un formato compatible (28x28x1)
# x_train = x_train[..., tf.newaxis]
# x_test = x_test[..., tf.newaxis]
#
# # Convertir las etiquetas en categorías (one-hot encoding)
# y_train = to_categorical(y_train, 10)
# y_test = to_categorical(y_test, 10)
#
# # Crear el modelo de la red neuronal
# model = models.Sequential([
#     layers.Flatten(input_shape=(28,28)),
#     layers.Dense(512,activation='relu'),
#     layers.Dense(512,activation='relu'),
#     layers.Dense(256,activation='relu'),
#     layers.Dense(256, activation='relu'),
#     layers.Dense(128,activation='relu'),
#     layers.Dense(64,activation='relu'),
#     layers.Dense(32,activation='relu'),
#     layers.Dense(64,activation='relu'),
#     layers.Dense(128,activation='relu'),
#     layers.Dense(256,activation='relu'),
#     layers.Dense(256, activation='relu'),
#     layers.Dense(512, activation='relu'),
#     layers.Dense(512, activation='relu'),
#     layers.Dense(10,activation='softmax'),
#     # layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
#     # layers.MaxPooling2D((2, 2)),
#     # layers.Conv2D(64, (3, 3), activation="relu"),
#     # layers.MaxPooling2D((2, 2)),
#     # layers.Conv2D(64, (3, 3), activation="relu"),
#     # layers.Flatten(),
#     # layers.Dense(64, activation="relu"),
#     # layers.Dense(10, activation="softmax")
# ])
#
# # Compilar el modelo
# model.compile(optimizer="adam",
#               loss="categorical_crossentropy",
#               metrics=["accuracy"])
#
# # Entrenar el modelo
# model.fit(x_train, y_train, epochs=50, batch_size=516, validation_split=0.1)
#
# # Evaluar el modelo en el conjunto de prueba
# test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
# print(f"Accuracy en el conjunto de prueba: {test_acc:.4f}")
#
# # Guardar el modelo entrenado (opcional)
# model.save("mnist_model.h5")

model = tf.keras.models.load_model("mnist_model.h5")
img = cv2.imread(f"8.png")[:,:,0]
img = np.invert(np.array([img]))
prediction = model.predict(img)
print(np.argmax(prediction))