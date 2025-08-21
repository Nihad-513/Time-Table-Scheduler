from tkinter import *
import tkinter as tk
import tkinter.messagebox as msb
import mysql.connector as my
from tkinter import ttk

# import GA
from GA import GeneticAlgorithm as ga

#create window
app=Tk("Scheduler")
app.title("TIME TABLE SCHEDULER")
app.geometry("820x280")
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

def generate():
   sem_s=comb_var.get()
   mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
   cur=mycon.cursor()
   reset = "delete from s3"
   cur.execute(reset)
   mycon.commit()
   reset = "delete from s5"
   cur.execute(reset)
   mycon.commit()
   sem =comb_var.get()
   sched1 = ga.generate_timetable('S3')
   sched2 = ga.generate_timetable('S5')
   print(sched1)
   print(sched2)
   ga.xlsgenersting(sched1,sched2)
#    tt1,tt2 = ga.fitness(sched1,sched2)
   for i in sched1:
       tup=tuple(i)
       qr1="insert into s3(hour1,hour2,hour3,hour4,hour5,hour6) values(%s,%s,%s,%s,%s,%s)"
       cur.execute(qr1,tup)
       mycon.commit()
       
   for j in sched2:
       tup=tuple(j)
       qr2="insert into s5(hour1,hour2,hour3,hour4,hour5,hour6) values(%s,%s,%s,%s,%s,%s)"
       cur.execute(qr2,tup)
       mycon.commit()
   if(sem_s=="S3"):
           mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
           cur=mycon.cursor()
           qr1="select * from s3"
           cur.execute(qr1)
           lis=cur.fetchall()
           for i in lis:
              tv.insert("",END,values=i)
           mycon.close()
   elif(sem_s=="S5"):
        mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
        cur=mycon.cursor()
        qr1="select * from s5"
        cur.execute(qr1)
        lis=cur.fetchall()
        for i in lis:
              tv.insert("",END,values=i)
        mycon.close()
   

#to delete the generateed information and insert full details of cars
def refresh():
    tv.delete(*tv.get_children())
    # show()

#to close the wimndow
def close():
    clos=msb.askyesno("ELTTS-Scheduler","do you want to exit")
    if clos > 0:
        app.destroy()
        return


#frame1
fr1=Frame(app,width=820,height=30)
fr1.place(x=0,y=0)
lbl1=Label(fr1,text='SCHEDULE TIMETABLE',font=('times',16))
lbl1.place(x=280,y=0)

fr3=Frame(app,width=820,height=425,bd=3,relief=RIDGE,bg='RoyalBlue4')
fr3.place(x=0,y=30)

#combobox for options to generate timetable
comb_var=StringVar()
comb=ttk.Combobox(fr3,textvariable=comb_var,state='readonly')
comb['values']=('S3','S5')
comb.place(x=5,y=30)


cmlb=Label(fr3,text="Generate for:",bg='RoyalBlue4')
cmlb.place(x=5,y=5)
#entry for generate
cgenerate_var=StringVar()
cgenerateent=Entry(fr3,textvariable=cgenerate_var)
cgenerateent.place(x=155,y=30)
#button for generate
generatebt=Button(fr3,text='GENERATE',width=11,command=generate)
generatebt.place(x=290,y=30)

#treeview to display timetable
tvd=ttk.Treeview(fr3,column=(1),show="headings",height='5')
tvd.place(x=5,y=70)
tvd.heading(1,text="DAY")
tvd.column(1,width=100)
lis=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']
for i in lis:
    tvd.insert("",END,values=i)


#treeview to display timetable
tv=ttk.Treeview(fr3,column=(1,2,3,4,5,6),show="headings",height='5')
tv.place(x=99,y=70)
 
tv.heading(1,text="HOUR 1")
tv.heading(2,text="HOURR 2")
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

#refresh button for treeview
refbt=Button(fr3,text='REFRESH',width=12,command=refresh)
refbt.place(x=710,y=190)

#exit button
closebt=Button(fr3,text='CLOSE',width=12,command=close)
closebt.place(x=710,y=220)

#to insert the car details the treeview


app.mainloop()
