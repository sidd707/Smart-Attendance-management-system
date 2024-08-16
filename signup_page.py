from tkinter import *
from tkinter import ttk, messagebox
import pymysql, os
import credentials as cr

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Teachers Sign Up")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "black")

        #Createing frames for the sign up window
        frame = Frame(self.window, bg="white")
        frame.place(x=350,y=100,width=500,height=550)

        title1 = Label(frame, text="Sign Up", font=("times new roman",25,"bold"),bg="white").place(x=20, y=10)
    
        #Creating Labels for first name and last name
        f_name = Label(frame, text="First name", font=("helvetica",15,"bold"),bg="white").place(x=20, y=100)
        l_name = Label(frame, text="Last name", font=("helvetica",15,"bold"),bg="white").place(x=240, y=100)

        #Entry for for first and last name
        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        #Creating label for email
        email = Label(frame, text="Bennett Email", font=("helvetica",15,"bold"),bg="white").place(x=20, y=180)

        #Entry for email section
        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        #Creating label for security questions
        sec_question = Label(frame, text="Security questions", font=("helvetica",15,"bold"),bg="white").place(x=20, y=260)
        answer = Label(frame, text="Answer", font=("helvetica",15,"bold"),bg="white").place(x=240, y=260)

        #Creating a submenue for security questions
        self.questions = ttk.Combobox(frame,font=("helvetica",13),state='readonly',justify=CENTER)
        self.questions['values'] = ("Select","What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
        self.questions.place(x=20,y=290,width=200)
        self.questions.current(0)

        #Entry for answering the security question
        self.answer_txt = Entry(frame,font=("arial"))
        self.answer_txt.place(x=240, y=290, width=200)

        #Creating label for new password
        password =  Label(frame, text="New password", font=("helvetica",15,"bold"),bg="white").place(x=20, y=340)

        #Entery for the new password
        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=370, width=420)

        self.terms = IntVar()#Terms and condition to be followed

        #Creating a checkbutoon for terms and conditions
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=20,y=420)
        
        #Creating a button for sign up. Here signup_func is definned below which would do the task
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=120,y=470,width=250)

    def signup_func(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="" or self.questions.get()=="Select" or self.answer_txt.get()=="" or self.password_txt.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            try:
                #Used to call and connect mysql
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from teacher_register where email=%s",self.email_txt.get())
                row=cur.fetchone()

                # Check if the entered email id is already exists or not.
                if row!=None:
                    messagebox.showerror("Error!","The email id is already exists, please try again with another email id",parent=self.window)
                else:
                    cur.execute("insert into teacher_register (f_name,l_name,email,question,answer,password) values(%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.fname_txt.get(),
                                        self.lname_txt.get(),
                                        self.email_txt.get(),
                                        self.questions.get(),
                                        self.answer_txt.get(),
                                        self.password_txt.get()
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    self.reset_fields()#Defined below
            #If the database is not there but still you are trying to run it.
            except Exception as es:
                messagebox.showerror("Error!",f"Error due to {es}",parent=self.window)

    #Defining reset fields
    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.questions.current(0)
        self.answer_txt.delete(0, END)
        self.password_txt.delete(0, END)
#The main function
if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()
