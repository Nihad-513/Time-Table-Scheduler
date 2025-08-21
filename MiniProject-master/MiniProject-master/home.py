#=============================================================================#
                              #HOME PAGE                                 
#=============================================================================#

from tkinter import *
import tkinter as tk
import tkinter.messagebox as msb
import mysql.connector as my
from subprocess import call

#create window
app=Tk()
app.title("TIME TABLE SCHEDULER")
app.geometry("825x380")
app.configure(background='RoyalBlue4')


# window willpop up and the  previous window will be hidden
def add_fac():
    app.withdraw()
    call(["python","faculty.py"])          
    app.deiconify()                        #previous window will pop up agian

 #'customerpending' window willpop up and the  previous window will be hidden    
def sub():
    app.withdraw()
    call(["python","sub.py"])      
    app.deiconify()                       #previous window will pop up agian
    
 # window willpop up and the  previous window will be hidden
def sct():
    app.withdraw()
    call(["python","schedule.py"])                 
    app.deiconify()                       #previous window will pop up agian

# window willpop up and the  previous window will be hidden
def view():
    app.withdraw()
    call(["python","view.py"])                
    app.deiconify()                       #previous window will pop up agian


def close():                              #To close the present window
    clos=msb.askyesno("ELTTS","do you want to exit")
    if clos > 0:
        app.destroy()
        return   

#frame1
fr1=Frame(app,width=910,height=30)
fr1.place(x=0,y=0)
lbl1=Label(fr1,text='HOME',font=('times',16))
lbl1.place(x=360,y=0)

#To insert image into the window
im1=PhotoImage(file="PIC.png")
iml=Label(app,image=im1)
iml.place(x=320,y=50)

#button for 'cars awailable'
bt1=Button(app,text="ADD FACULTY",
           width=30,height=2,command=add_fac,bg='SkyBlue4')
bt1.place(x=5,y=50)

#button for 'cars to be returned'
bt2=Button(app,text="ADD SUBJECT",
           width=30,height=2,command=sub,bg='SkyBlue4')
bt2.place(x=5,y=110)

#button for 'purcahase car'
bt3=Button(app,text="SCHEDULE TIME TABLE",
           width=30,height=2,command=sct,bg='SkyBlue4')
bt3.place(x=5,y=170)

#button for 'return car'
bt4=Button(app,text="VIEW TIME TABLE",width=30,height=2,command=view,bg='SkyBlue4')
bt4.place(x=5,y=230)

#exit butoon
bt5=Button(app,text="EXIT",width=30,height=2,command=close,bg='SkyBlue4')
bt5.place(x=5,y=290)

app.mainloop()
