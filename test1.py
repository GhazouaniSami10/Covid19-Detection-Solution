import tensorflow as tf
import cv2
from tensorflow.keras.optimizers import Adam
import numpy as np
import argparse
import os
from tensorflow import keras
from tensorflow.keras import layers


# Reload the model from the 2 files we saved
with open('model/model.json') as json_file:
    json_config = json_file.read()
new_model = keras.models.model_from_json(json_config)
new_model.load_weights('model/model2.h5')
print("Loaded Model from disk")

# compile and evaluate loaded model

new_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

              
              
path = r'D:\corona\detect-covid19\a.png'
path1 = r'D:\corona\detect-covid19\aa.png'


img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(224,224))
img = np.reshape(img,[1,224,224,3])
labels_str = ['covid', 'normal']
predIdxs = new_model.predict(img, batch_size=1)
predIdxs = np.argmax(predIdxs, axis=1)
txt_show=labels_str[predIdxs[0]]
font=cv2.FONT_HERSHEY_SIMPLEX


img2=cv2.imread(path)
img2=cv2.resize(img2,(500,500))
cv2.putText(img2,str(txt_show),(400,30),font,.7,(255,255,0),3,cv2.LINE_AA)



while True:
    cv2.imshow('X ray image',img2)
    cv2.imwrite(path1,img2)
    k = cv2.waitKey(0)
    print(k)
    if k == ord('q'):
            break
print('Successfully saved')
cv2.destroyAllWindows()


#print(labels_str[predIdxs[0]])
