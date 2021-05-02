# -*- coding: utf-8 -*-
"""
Created on Sun May  2 00:11:29 2021

@author: subha
"""
import os
import numpy as np
from flask import request
from flask import Flask
from flask import render_template
#import keras
from keras.preprocessing import image
from keras.models import load_model

app = Flask(__name__)
UPLOAD_FOLDER = "C:/Users/subha/OneDrive/Desktop/COVID-19/static"

@app.route("/", methods=["GET","POST"])
def upload_predict():
    if request.method=="POST":
        model=load_model('C:/Users/subha/OneDrive/Desktop/COVID-19/model_covid.h5')
        print('model loaded successfully')
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(
                UPLOAD_FOLDER,
                image_file.filename
            )
            image_file.save(image_location)
            print(image_location)
            #model=keras.models.load_model('model_covid.h5')
            img = image.load_img(path=image_location, target_size=(224,224))
            img = np.expand_dims(img, axis=0)
            pred = model.predict_classes(img)
            prob = pred[0]
            if prob == 1:
                a= 'Your report says you are COVID-19 -ve'
            else:
                a='Your report says you are COVID-19 +ve'
            print(pred[0])
            #prediction = pred[0]
            return render_template("index.html", prediction=a, image_loc=image_file.filename)
    
    return render_template("index.html", prediction=0, image_loc=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,threaded=False)