from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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
        b2=Button(frame,image=self.photoimg,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b2.place(x=370,y=420,width=200)


#================function Declaration=================





    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Both password must be same",parent=self.root)
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

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()

