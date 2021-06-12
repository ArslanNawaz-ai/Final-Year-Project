from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
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
from main import Health_Compliance_System



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def  __init__(self,root):
        self.root=root
        self.root.geometry("1540x790+0+0")
        self.root.title("Login")

        #bgimg
        img0=Image.open(r"Imges\login.jpg")
        img0=img0.resize((1530,790),Image.ANTIALIAS)
        self.photoimg0=ImageTk.PhotoImage(img0)
        bg_img=Label(self.root,image=self.photoimg0)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(bg_img,bd=2,bg="white")
        frame.place(x=610,y=40,width=350,height=450)

        img1=Image.open(r"Imges\lg1.PNG")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lb_img1=Label(self.root,image=self.photoimg1)
        lb_img1.place(x=730,y=45,width=100,height=100)

        get_str=Label(frame,bg="white",fg="black",text="Get Started",font=("times new roman",20,"bold"))
        get_str.place(x=95,y=100)

        #label
        #username
        username_label=Label(frame,text="UserName",font=("times new roman",15,"bold"),bg="white")
        username_label.place(x=70,y=150)

        self.txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        #pass
    
        password_label=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password_label.place(x=70,y=210)

        self.txtpass=ttk.Entry(frame,show='*',font=("times new roman",13,"bold"))
        self.txtpass.place(x=40,y=240,width=270)


        img2=Image.open(r"Imges\u1.PNG")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lb_img2=Label(frame,image=self.photoimg2,borderwidth=0)
        lb_img2.place(x=40,y=150,width=25,height=25)

        img3=Image.open(r"Imges\p1.PNG")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lb_img3=Label(frame,image=self.photoimg3,borderwidth=0)
        lb_img3.place(x=40,y=210,width=25,height=25)
        
        
        #login
        loginbtn=Button(frame,command=self.login,text="Login",cursor="hand2",font=("times new roman",15,"bold"),bg="grey",fg="black",bd=3,relief=RIDGE)
        loginbtn.place(x=110,y=280,width=120,height=35)

        or_label=Label(frame,text="OR",font=("times new roman",8,"bold"),bg="white")
        or_label.place(x=160,y=320)


        #CreateAccount
        createbtn=Button(frame,command=self.register_window,text="Create Account",cursor="hand2",font=("times new roman",10,"bold"),bg="green",fg="black",borderwidth=0)
        createbtn.place(x=60,y=340,width=220,height=30)

        #Forget Button
        forgetbtn=Button(frame,text="Forgotten Password",command=self.forget_password_window,cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="white",)
        forgetbtn.place(x=20,y=400,width=300,height=25)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are Required")
        elif self.txtuser.get()=="Arslan" and self.txtpass.get()=="123":
            messagebox.showinfo("Success","Welcome to HSCS")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facerecognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                            
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username Or Password")
            else:
                open_main=messagebox.askyesno("YesNO","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Health_Compliance_System(self.new_window)
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()
#==================Reset password==========================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Enter Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the new Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facerecognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the correct Security Answer",parent=self.root2)
            else:
                quer=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(quer,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset. Please Login with new Password",parent=self.root2)
                self.root2.destroy()
            

#================forget password Window====================
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to reset the Password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facerecognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Please Enter the valid user name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="green",fg="black",bd=3,relief=RIDGE)
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"))
                security_Q.place(x=50,y=80)
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Pet Name","First Car Name you Owned")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"))
                security_A.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
                self.txt_security.place(x=50,y=180,width=250)
                

                new_pass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"))
                new_pass.place(x=50,y=220)
                self.txt_newpass=ttk.Entry(self.root2,show='*',font=("times new roman",13,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290,width=150)


                





class Register:
    
    def  __init__(self,root):
        self.root=root
        self.root.geometry("1540x790+0+0")
        self.root.title("Register")
#==================variables================

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        img0=Image.open(r"Imges\login5.jpg")
        img0=img0.resize((1530,790),Image.ANTIALIAS)
        self.photoimg0=ImageTk.PhotoImage(img0)
        bg_img=Label(self.root,image=self.photoimg0)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=480,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=20,y=20)

        #fname
        fname_label=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname_label.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",13,"bold"))
        fname_entry.place(x=50,y=130,width=250) 
        #lname
        lname_label=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname_label.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",13,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
####################
        #contact
        contact_label=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="white")
        contact_label.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",13,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)    
        #email
        email_label=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email_label.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",13,"bold"))
        self.txt_email.place(x=370,y=200,width=250)


######################
        #security
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Pet Name","First Car Name you Owned")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",13,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

############################
        #Password
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",13,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        #Confirm Password
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",13,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
######################CheckButton#######################################

        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)


#======================butttons=================
        img01=Image.open(r"Imges\register1.PNG")
        img01=img01.resize((200,55),Image.ANTIALIAS)
        self.photoimg01=ImageTk.PhotoImage(img01)
        b1=Button(frame,image=self.photoimg01,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=40,y=420,width=200)


        img=Image.open(r"Imges\loginbtn.PNG")
        img=img.resize((200,45),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        b2=Button(frame,command=self.return_login,image=self.photoimg,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b2.place(x=370,y=420,width=200)


#================function Declaration=================





    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Both password must me same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our terms and Conditions",parent=self.root)
        else: 
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facerecognition")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,Please try with different Email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()


                
                                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","You are Registered Successfully",parent=self.root)
            self.root.destroy()
    def return_login(self):
        self.root.destroy()
       
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
    main()
    # root=Tk()
    # obj=Login_Window(root)
    # root.mainloop()
