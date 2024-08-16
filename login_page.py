from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import os
from signup_page import SignUp
import credentials as cr
from PIL import ImageTk, Image


#Creating a class for loginpage
class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("Teachers Login")
        # Set the window size
        # Here 0,0 represents the starting point of the window 
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        #Designing Part

        # 1)Entry Field & creating Buttons
        self.frame1 = Frame(self.window, bg = "black")#Creates a frame 
        self.frame1.place(x=450,y=0,relwidth=1, relheight=1) #Placing the frame and packing it by giving relative width and height

        self.frame2 = Frame(self.window, bg="black")
        self.frame2.place(x=0, y=0, width=450, relheight = 1)

        self.frame3 = Frame(self.frame1, bg="Black")
        self.frame3.place(x=140,y=150,width=500,height=450)

        # 2)Creating labels and entering data for username
        self.email_label = Label(self.frame3,text="Bennett Email Address", font=("helvetica",20,"bold"),bg="black", fg="White").place(x=50,y=40)
        self.email_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="black",fg="white")
        self.email_entry.place(x=50, y=80, width=300)

        # 3)Creating labels and entering data for password
        self.password_label = Label(self.frame3,text="Password", font=("helvetica",20,"bold"),bg="black", fg="White").place(x=50,y=120)
        self.password_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="black",fg="white",show="*")
        self.password_entry.place(x=50, y=160, width=300)

        # 4)Buttons for login,forget password and create account
        self.login_button = Button(self.frame3,text="Log In",command=self.login_func,font=("times new roman",15, "bold"),bd=0,bg="blue",fg="black").place(x=50,y=200,width=300)
        self.forgotten_pass = Button(self.frame3,text="Forgotten password?",command=self.forgot_func,font=("times new roman",10, "bold"),bd=0,bg="black",fg="white").place(x=125,y=260,width=150)
        self.create_button = Button(self.frame3,text="Create New Account",command=self.redirect_window,font=("times new roman",18, "bold"),bd=0,bg="green2",fg="white").place(x=80,y=320,width=250)

    #Defining a login page
    def login_func(self):
        if self.email_entry.get()=="" or self.password_entry.get()=="":#If the user do not enter anything shows error
            messagebox.showerror("Error!","All fields are required",parent=self.window)
            #Used execption handaling to avoid any error in code while executing
        else:
            try:
                #Below coomand is use to call and connect to the sql server
                connection=pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                #Command in mysql
                cur.execute("select * from teacher_register where email=%s and password=%s",(self.email_entry.get(),self.password_entry.get()))
                row=cur.fetchone()#Moves to the next row
                if row == None:
                    messagebox.showerror("Error!","Invalid username or password",parent=self.window)
                else:
                    messagebox.showinfo("Success","Logged in",parent=self.window)
                    # Clear all the entries
                    self.reset_fields()
                    '''os.system('cmd /k "qr.py"')'''
                    os.system('cmd /k "hello.py"')
                    
                    connection.close()

            except Exception as e:
                #Exeception is required because if the user did not create a table in mysql or 
                #did not install mysql would show this error
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)#Here e is for execeptions due to error

    #Defining for the forget password
    def forgot_func(self):
        if self.email_entry.get()=="":
            #Command for forget password to enter username
            messagebox.showerror("Error!", "Please enter your Email Id",parent=self.window)
        else:
            try:
                #Below coomand is use to call and connect to the sql server
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                #Commad in sql
                cur.execute("select * from teacher_register where email=%s", self.email_entry.get())
                row=cur.fetchone()#Moves to the next row
                if row == None:
                    messagebox.showerror("Error!", "Email Id doesn't exists")
                else:
                    connection.close()
                    
                    self.root=Toplevel()#Top level windows are used to redirect to the next window(In this case forget password)
                    self.root.title("Forget Password?")
                    self.root.geometry("400x440+450+200")
                    self.root.config(bg="white")
                    self.root.focus_force()
                    self.root.grab_set()

                    title3 = Label(self.root,text="Change your password",font=("times new roman",20,"bold"),bg="white").place(x=10,y=10)
                    title5 = Label(self.root, text="Select your question while creating the password", font=("times new roman", 15, "bold"), bg="white").place(x=10,y=85)
                    #The combobox is used to create a drop down menue and ttk is the module
                    self.sec_ques = ttk.Combobox(self.root,font=("times new roman",13),state='readonly',justify=CENTER)
                    #Entering values inside the dropbox(Submenue)
                    self.sec_ques['values'] = ("Select","What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
                    self.sec_ques.place(x=10,y=120, width=270)
                    #If newindex is supplied, sets the combobox value to the element at position newindex in the list of values. 
                    # Otherwise, returns the index of the current value in the list of values or -1 if the current value does not appear in the list.
                    self.sec_ques.current(0)
                    
                    #For answer label
                    title6 = Label(self.root, text="Answer", font=("times new roman", 15, "bold"), bg="white").place(x=10,y=160)
                    self.ans = Entry(self.root,font=("arial"))
                    self.ans.place(x=10,y=195,width=270)

                    #For New Password
                    title7 = Label(self.root, text="New Password", font=("times new roman", 15, "bold"), bg="white").place(x=10,y=235)
                    self.new_pass = Entry(self.root,font=("arial"))
                    self.new_pass.place(x=10,y=270,width=270)
                    #For Submit button
                    #Here change_pass is defined below which is used to change the password
                    self.create_button = Button(self.root,text="Submit",command=self.change_pass,font=("times new roman",18, "bold"),bd=0,bg="green2",fg="white").place(x=95,y=340,width=200)

            except Exception as e:
               #Exeception is required because if the user did not create a table in mysql or 
               #did not install mysql would show this error
               messagebox.showerror("Error", f"{e}")
                
    #Definig change_pass
    def change_pass(self):
        #If both the field is left blank shows error
        if self.email_entry.get() == "" or self.sec_ques.get() == "Select" or self.new_pass.get() == "":
            messagebox.showerror("Error!", "Please fill the all entry field correctly")
        else:
            try:
                #Used to call and connect mysql
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from teacher_register where email=%s and question=%s and answer=%s", (self.email_entry.get(),self.sec_ques.get(),self.ans.get()))
                row=cur.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "Please fill the all entry field correctly")
                else:
                    try:
                        cur.execute("update teacher_register set password=%s where email=%s", (self.new_pass.get(),self.email_entry.get()))
                        connection.commit()

                        messagebox.showinfo("Successful", "Password has changed successfully")
                        connection.close()
                        self.reset_fields()
                        self.root.destroy()
                    #If the database is not there but still you are trying to run it.
                    except Exception as er:
                        messagebox.showerror("Error!", f"{er}")
                        
            except Exception as er:
                        messagebox.showerror("Error!", f"{er}")
            
    #Defining Redirect window
    def redirect_window(self):
        self.window.destroy()
        # Importing the signup window.
        # The page must be in the same directory
        root = Tk()
        obj = SignUp(root)
        root.mainloop()
    #Defining to reset the field
    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)

# The main function
if __name__ == "__main__":
    root = Tk()#object initiation from tkinter module 
    obj = login_page(root) #Creating an object(Goes to the login_page class)
    root.mainloop()#Running the mainloop for tkinter









