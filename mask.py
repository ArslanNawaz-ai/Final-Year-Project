# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time
from tkinter import messagebox
import mysql.connector
import imutils

class Mask:
    def  __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Mask Detection")



        
        #bgimg
        img4=Image.open(r"Imges\facemaskbg.PNG")
        img4=img4.resize((1530,790),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)



        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img,text="Face Mask Detection",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=65)


        #Button Mask Detection
        img6=Image.open(r"Imges\img1.7.PNG")
        img6=img6.resize((400,400),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=600,y=200,width=400,height=400)

        b1_1=Button(bg_img,text="Detect Face Mask",command=mask_detect,cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
        b1_1.place(x=600,y=600,width=400,height=80)



def mask_detect():
    def detect_and_predict_mask(frame, faceNet, maskNet): #define a function detect_and_predict_mask with 3 arguments
        # grab the dimensions of the frame and then construct a blob
        # from it
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
            (104.0, 177.0, 123.0))

        # pass the blob through the network and obtain the face detections
        faceNet.setInput(blob)
        detections = faceNet.forward()
        print(detections.shape)

        # initialize our list of faces, their corresponding locations,
        # and the list of predictions from our face mask network
        faces = []
        locs = []
        preds = []

        # loop over the detections
        for i in range(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with
            # the detection
            confidence = detections[0, 0, i, 2]

            # filter out weak detections by ensuring the confidence is
            # greater than the minimum confidence
            if confidence > 0.5:
                # compute the (x, y)-coordinates of the bounding box for
                # the object
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # ensure the bounding boxes fall within the dimensions of
                # the frame
                (startX, startY) = (max(0, startX), max(0, startY))
                (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

                # extract the face ROI, convert it from BGR to RGB channel
                # ordering, resize it to 224x224, and preprocess it
                face = frame[startY:endY, startX:endX]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = cv2.resize(face, (224, 224))
                face = img_to_array(face)
                face = preprocess_input(face)

                # add the face and bounding boxes to their respective
                # lists
                faces.append(face)
                locs.append((startX, startY, endX, endY))

        # only make a predictions if at least one face was detected
        if len(faces) > 0:
            # for faster inference we'll make batch predictions on *all*
            # faces at the same time rather than one-by-one predictions
            # in the above `for` loop
            faces = np.array(faces, dtype="float32")
            preds = maskNet.predict(faces, batch_size=32)

        # return a 2-tuple of the face locations and their corresponding
        # locations
        return (locs, preds) #locs is rectangle in face & predict is aquracy of mask in %

    # load our serialized face detector model from disk
    prototxtPath = r"face_detector\deploy.prototxt"
    weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel" #face detection model 
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath) #using method of cv2 readNet (Deep nero network(dnn))

    # load the face mask detector model from disk
    maskNet = load_model("mask_detector.model")#Deep learning mask_detector model

    # initialize the video stream
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start() #src=0 is primary camer, start()load the camer 

    # loop over the frames from the video stream
    while True:
        # grab the frame from the threaded video stream and resize it
        # to have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame, width=400) #images that look like a video

        # detect faces in the frame and determine if they are wearing a
        # face mask or not
        (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)#Frame for video,faceNet is for face_detector & maskNet is for mask_detector

        # loop over the detected face locations and their corresponding
        # locations
        for (box, pred) in zip(locs, preds):
            # unpack the bounding box and predictions
            (startX, startY, endX, endY) = box
            (mask, withoutMask) = pred #making a box in image

            # determine the class label and color we'll use to draw
            # the bounding box and text
            label = "Mask" if mask > withoutMask else "No Mask"
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)#BGR

            # include the probability in the label
                                                    #90%     #10%
            label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100) #% of mask 

            # display the label and bounding box rectangle on the output
            # frame
            cv2.putText(frame, label, (startX, startY - 10),#10 is pixels of fonts
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2) #FONT_HERSHEY_SIMPLEX font name
            cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2) #2 is thickness of rectangle
            
        # show the output frame
        cv2.imshow("Frame", frame)#sequence of image in Frame
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()
    #webcam = cv2.VideoCapture(0)
    #webcam.release()




		


if __name__=="__main__":
    root=Tk()
    obj=Mask(root)
    root.mainloop() 
