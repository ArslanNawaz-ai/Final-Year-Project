import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
from time import strftime
from datetime import datetime
import os
import mysql.connector
from students import Student
from train import Train
from face_recognition import Face_Recognition
from social import Social
from mask import Mask
from attendance import Attendance


class Health_Compliance_System:
    def  __init__(self,root):
        self.root=root

        self.root.geometry("1530x790+0+0")
        self.root.title("Health Compliance System")


        #firstimg
        img1=Image.open(r"C:\Users\Arslan Nawaz\3D Objects\Mergered FYP\Imges/Img1.3.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #secondimg
        img2=Image.open(r"Imges\Img1.9.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)



        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)


        #thirdimg
        img3=Image.open(r"Imges\sc.PNG")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)



        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        #bgimg
        img4=Image.open(r"Imges\dev.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)



        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="Health Compliance System for Post COVID-19",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=65)

#===============time=============================

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,width=110,height=50)
        time()

        #Button1 Face Mask Dtection
        img5=Image.open(r"Imges\Img2.0.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.mask_det,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Mask Detecton",command=self.mask_det,cursor="hand2",font=("times new roman",15,"bold"),bg="brown",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Button2 Train Face
        img6=Image.open(r"Imges\Img1.1.PNG")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.train_data,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Train Face",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="brown",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        #Button3 face Detction
        img7=Image.open(r"Imges\img1.6.PNG")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.face_data,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detecton",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="brown",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)



        #Button4 Detect Social Distance
        img8=Image.open(r"Imges\dd2.PNG")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.social_dis,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Distance Dtection",command=self.social_dis,cursor="hand2",font=("times new roman",15,"bold"),bg="brown",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #Button5 Student Details
        img9=Image.open(r"Imges\smart-attendance.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Students Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="brown",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)

        #Button 6 Photos
        img10=Image.open(r"Imges\Photos.PNG")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="brown",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)

        #Button 7 Attendace 
        img11=Image.open(r"Imges\girl.jpeg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.student_attendance,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",command=self.student_attendance,cursor="hand2",font=("times new roman",15,"bold"),bg="brown",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)

        #Button 8 Exit
        img12=Image.open(r"Imges\exit.jpg")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,command=self.iExit,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="brown",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)
    def open_img(self):
        os.startfile("Data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Health Compliance System","Are you sure to exit the project",parent=self.root)
        if  self.iExit>0:
            self.root.destroy()
        else:
            return

#=======================function==================================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def social_dis(self):
        self.new_window=Toplevel(self.root)
        self.app=Social(self.new_window)


    def mask_det(self):
        self.new_window=Toplevel(self.root)
        self.app=Mask(self.new_window)
    

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def student_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)











if __name__=="__main__":
    root=Tk()
    obj=Health_Compliance_System(root)
    root.mainloop()
