#=============================================================================#
                              #login(main).py                                     
#=============================================================================#

from tkinter import *
import tkinter as tk
from subprocess import call
import tkinter.messagebox as msb                           
import mysql.connector as my

#create a window
app=Tk()
app.title("TIME TABLE SCHEDULER")
app.geometry("450x460")              
app.configure(background='RoyalBlue4')

#icon for the window
#app.iconbitmap("images_ERc_icon.ico")

#Create a database if not exist 
mycon=my.connect(host='localhost',user='root',passwd='mysql')
cur=mycon.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS tts")
mycon.close()

#Create 'adminlogin' table if not exist 
mycon=my.connect(host='localhost',user='root',passwd='mysql',database='tts')
cur=mycon.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS  adminlogin(user VARCHAR(20),
            password varchar(20) DEFAULT'password' )""")
mycon.close() 


#connecting to mysql database for the login purpose
mycon=my.connect(host='localhost',user='root',passwd='mysql',database='tts')
cur=mycon.cursor()
qr1="select * from adminlogin"
cur.execute(qr1)
lis=cur.fetchall()
#Signin option will be shown if the adminligin table is empty    
if(lis==[]):                   
    def add():
        usr=user.get()
        passw=passwd.get()
        if(usr=="" or passw==""):
            msb.showinfo("insert status","all fields are required")            
        else:
            mycon=my.connect(host='localhost',user='root',
                             passwd='mysql',database='tts')
            cur=mycon.cursor()
            tup=(usr,passw)
            #new username and password will be inserted to adminlogin table
            qr1="insert into adminlogin values('%s','%s')"     
            cur.execute(qr1%tup)
            mycon.commit()
            msb.showinfo("Admin Login","New admin added")
            app.destroy()
            #adminlogin window will pop up after destoying the previous window
            call(["python","home.py"])                 

        
    def close():                    #To close the window                        
        clos=msb.askyesno("login","do you want to exit")
        if clos > 0:
            app.destroy()
            return


    #frame1
    fr2=Frame(app,width=500,height=250,relief=RIDGE,bg='RoyalBlue4')
    fr2.place(x=0,y=0)
     
    #To insert image into the window
    im1=PhotoImage(file="logo.png")
    iml=Label(fr2,image=im1)
    iml.place(x=100,y=10)


    #frame2
    fr3=Frame(app,width=370,height=240,relief=RIDGE,bg='RoyalBlue4')
    fr3.place(x=10,y=250)

    label=Label(fr3,
                text='Please create an admin account to use this application',
                bg='grey',font=('Helvetica',10))
    label.place(x=50,y=10)

    #text variable for username and password   
    user=StringVar()
    passwd=StringVar()

    #label and entry for username
    lbl1=Label(fr3,text='User name:',bg='RoyalBlue4',font=('Helvetica',10))
    lbl1.place(x=50,y=60)
    ent1=Entry(fr3,textvariable=user)
    ent1.place(x=140,y=60)

    #label and entry for password
    lbl2=Label(fr3,text='Password:',bg='RoyalBlue4',font=('Helvetica',10))
    lbl2.place(x=50,y=100)
    ent2=Entry(fr3,textvariable=passwd,show="*")
    ent2.place(x=140,y=100)

    #exit button
    bt1=Button(fr3,text="Exit",width=10,command=close,bg='SkyBlue4')  
    bt1.place(x=50,y=170)
    
    #signin button
    bt2=Button(fr3,text="Sign in",width=10,command=add,bg='SkyBlue4')
    bt2.place(x=230,y=170)

    app.mainloop()
    
    
#login option will be shown if adminlogin table is not empty    
else:                                         
    def login():
        uname=ent1.get()
        passw=ent2.get()
        mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
        cur=mycon.cursor()
        qr1="select * from adminlogin where user='%s'"
        tup=(uname,)
        cur.execute(qr1%tup)
        lis=cur.fetchall()
        #Checking wheather username and password exist in adminlogintable
        for i in lis:                     
            user=i[0]
            passwd=i[1]
            if(uname==user and passw==passwd):         
                app.destroy()
        #adminlogin window will pop up after destoying the previous window 
                call(["python","home.py"])        
                #break
                pass
            else:
                #If username or password is incorrect message will be shown
                msb.showinfo("app info",
                         " user name or password is incorrect")  
                break
        mycon.close()   
        
    def close():                                    #To close the window
        clos=msb.askyesno("app","do you want to exit")
        if clos > 0:
            app.destroy()
            return


    #frame1
    fr2=Frame(app,width=500,height=250,relief=RIDGE,bg='RoyalBlue4')
    fr2.place(x=0,y=0)
     
    #To insert image into the window
    im1=PhotoImage(file="logo.png")
    iml=Label(fr2,image=im1)
    iml.place(x=100,y=10)


    #frame2
    fr3=Frame(app,width=400,height=240,relief=RIDGE,bg='RoyalBlue4')
    fr3.place(x=10,y=250)
    
    #text variable for username and password   
    user=StringVar()
    passwd=StringVar()

    #label and entry for username
    lbl1=Label(fr3,text='User name:',bg='RoyalBlue4',font=('Helvetica',10))
    lbl1.place(x=90,y=10)
    ent1=Entry(fr3,textvariable=user)
    ent1.place(x=180,y=10)

    #label and password for password
    lbl2=Label(fr3,text='Password:',bg='RoyalBlue4',font=('Helvetica',10))
    lbl2.place(x=90,y=70)
    ent2=Entry(fr3,textvariable=passwd,show="*")
    ent2.place(x=180,y=70)

    #exit button
    bt1=Button(fr3,text="Exit",width=10,command=close,bg='SkyBlue4')  
    bt1.place(x=120,y=110)

    #login button
    bt2=Button(fr3,text="login",width=10,command=login,bg='SkyBlue4')
    bt2.place(x=220,y=110)

    label=Label(fr3,
                text='To create a new admin please contact ADMINISTRATOR',
                bg='grey',font=('Helvetica',10))
    label.place(x=50,y=180)

    app.mainloop()
