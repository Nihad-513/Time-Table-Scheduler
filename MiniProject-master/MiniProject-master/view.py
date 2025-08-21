from tkinter import *
import tkinter as tk
import tkinter.messagebox as msb
import mysql.connector as my
from tkinter import ttk
#create window
app=Tk()
app.title("Time Table")
app.geometry("820x450")
app.configure(background='RoyalBlue4')


#create database if not exist 
mycon=my.connect(host='localhost',user='root',passwd='mysql')
cur=mycon.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS tts")
mycon.close()

#Create 's3' table if not exist
mycon=my.connect(host='localhost',user='root',passwd='mysql',database='tts')
cur=mycon.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS  s3(hour1 VARCHAR(40),
            hour2 VARCHAR(40),hour3 VARCHAR(40),hour4 VARCHAR(40),hour5 VARCHAR(40),hour6 VARCHAR(40))""")
mycon.close()

#Create 's5' table if not exist
mycon=my.connect(host='localhost',user='root',passwd='mysql',database='tts')
cur=mycon.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS  s5(hour1 VARCHAR(40),
            hour2 VARCHAR(40),hour3 VARCHAR(40),hour4 VARCHAR(40),hour5 VARCHAR(40),hour6 VARCHAR(40))""")
mycon.close()

#To show the subject details in the Treeview
def show_s3():
    mycon=my.connect(host='localhost',user='root',
                     passwd='mysql',database='tts')
    cur=mycon.cursor()
    qr1="select * from s3"
    cur.execute(qr1)
    lis=cur.fetchall()
    for i in lis:
        tv.insert("",END,values=i)
    mycon.close()
    
#To show the subject details in the Treeview
def show_s5():
    mycon=my.connect(host='localhost',user='root',
                     passwd='mysql',database='tts')
    cur=mycon.cursor()
    qr1="select * from s5"
    cur.execute(qr1)
    lis=cur.fetchall()
    for i in lis:
        tv1.insert("",END,values=i)
    mycon.close()

#frame1
fr1=Frame(app,width=820,height=30)
fr1.place(x=0,y=0)
lbl1=Label(fr1,text='VIEW TIME TABLE',font=('times',16))
lbl1.place(x=280,y=0)
#frame3
fr3=Frame(app,width=820,height=200,bd=3,relief=RIDGE,bg='RoyalBlue4')
fr3.place(x=0,y=35)
cmlb=Label(fr3,text="S3:",bg='RoyalBlue4')
cmlb.place(x=5,y=5)
#treeview to display timetable
tvd=ttk.Treeview(fr3,column=(1),show="headings",height='5')
tvd.place(x=5,y=35)
tvd.heading(1,text="DAY")
tvd.column(1,width=100)
lis=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']
for i in lis:
    tvd.insert("",END,values=i)
#treeview to display timetable
tv=ttk.Treeview(fr3,column=(1,2,3,4,5,6),show="headings",height='5')
tv.place(x=99,y=35)
 
tv.heading(1,text="HOUR 1")
tv.heading(2,text="HOUR 2")
tv.heading(3,text="HOUR 3")
tv.heading(4,text="HOUR 4")
tv.heading(5,text="HOUR 5")
tv.heading(6,text="HOUR 6")
tv.column(1,width=100)
tv.column(2,width=100)
tv.column(3,width=100)
tv.column(4,width=100)
tv.column(5,width=100)
tv.column(6,width=100)

#frame4
fr4=Frame(app,width=820,height=200,bd=3,relief=RIDGE,bg='RoyalBlue4')
fr4.place(x=0,y=240)
cmlb=Label(fr4,text="S5:",bg='RoyalBlue4')
cmlb.place(x=5,y=5)
#treeview to display timetable
tvd=ttk.Treeview(fr4,column=(1),show="headings",height='5')
tvd.place(x=5,y=35)
tvd.heading(1,text="DAY")
tvd.column(1,width=100)
lis=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']
for i in lis:
    tvd.insert("",END,values=i)
#treeview to display timetable
tv1=ttk.Treeview(fr4,column=(1,2,3,4,5,6),show="headings",height='5')
tv1.place(x=99,y=35)
 
tv1.heading(1,text="HOUR 1")
tv1.heading(2,text="HOURR 2")
tv1.heading(3,text="HOUR 3")
tv1.heading(4,text="HOUR 4")
tv1.heading(5,text="HOUR 5")
tv1.heading(6,text="HOUR 6")
tv1.column(1,width=100)
tv1.column(2,width=100)
tv1.column(3,width=100)
tv1.column(4,width=100)
tv1.column(5,width=100)
tv1.column(6,width=100)

show_s3()
show_s5()
app.mainloop()
