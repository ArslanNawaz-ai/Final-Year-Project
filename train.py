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

class Train:
    def  __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Faces")



        
        #bgimg
        img4=Image.open(r"Imges\face train.jpg")
        img4=img4.resize((1530,790),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)



        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img,text="Train Faces",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=65)


        #Button2 Train Face
        img6=Image.open(r"Imges\img1.4.PNG")
        img6=img6.resize((400,400),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.train_classifier,cursor="hand2")
        b1.place(x=600,y=200,width=400,height=400)

        b1_1=Button(bg_img,text="Train Face",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
        b1_1.place(x=600,y=600,width=400,height=80)

#==================classifier======================
    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #greyscale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
#======================train Classifier=========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training DataSet Completed",parent=self.root)


       

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop() 
