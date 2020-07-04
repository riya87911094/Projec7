from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("login system")
        self.root.geometry("1350x700+0+0")
         

        self.bg_icons=ImageTk.PhotoImage(file="images/bg.jpeg")
        self.user_icon=PhotoImage(file="images/user.png")
        self.pass_icon=PhotoImage(file="images/lock.png")
        self.logo_icon=PhotoImage(file="images/logoo.jpg")
        #.......Variable...
        self.uname=StringVar()
        self.pass_=StringVar()       
        bg_lbl=Label(self.root,image=self.bg_icons).pack()

        title=Label(self.root,text="Login System",font=("times new roman",20,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="pink")
        Login_Frame.place(x=400,y=150)
        
        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=20)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",10)).grid(row=1,column=1,padx=5)

        lblpass=Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=20)
        txtpass=Entry(Login_Frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=("",10)).grid(row=2,column=1,padx=5)


        btn_log=Button(Login_Frame,text="Login",width=15,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,padx=10)  
        

    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
           messagebox.showerror("Error","all fields are required!")
        elif self.uname.get()=="riya" and self.pass_.get()=="123":
           messagebox.showerror("Succesful",f"welcome{self.uname.get()}")
        else:
            messagebox.showerror("Error","invalid username or password")     

           

   
        
root = Tk()
obj  = Login_System(root)
root.mainloop()

     