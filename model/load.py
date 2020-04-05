# imports
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# opening and store file in a variable


def init(): 
# Reload the model from the 2 files we saved
   with open('model.json') as json_file:
       json_config = json_file.read()
   new_model = keras.models.model_from_json(json_config)
   new_model.load_weights('model2.h5')
   print("Loaded Model from disk")

# compile and evaluate loaded model

   new_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
   graph = tf.get_default_graph()
   return loaded_model