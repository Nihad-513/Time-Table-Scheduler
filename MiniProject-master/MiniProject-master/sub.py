#=============================================================================#
                              #subject                                   
#=============================================================================#

from tkinter import *
import tkinter as tk
import tkinter.messagebox as msb
import mysql.connector as my
from tkinter import ttk

# GA imports
from GA.assets import Attributes as att

#create window
app=Tk('Manage Subjects')
app.title("TIME TABLE SCHEDULER")
app.geometry("950x430")
app.configure(background='RoyalBlue4')

#icon for the window
#app.iconbitmap("images_ERc_icon.ico")

#craete database if not exist
mycon=my.connect(host='localhost',user='root',passwd='mysql')
cur=mycon.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS tts")
mycon.close()

#Create 'subject' table if not exist
mycon=my.connect(host='localhost',user='root',passwd='mysql',database='tts')
cur=mycon.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS  subject(scode VARCHAR(20) PRIMARY KEY,
            name VARCHAR(40),faculty VARCHAR(40),hour INT(4),sem VARCHAR(40))""")
mycon.close()

#To show the subject details in the Treeview
def show():
    mycon=my.connect(host='localhost',user='root',
                     passwd='mysql',database='tts')
    cur=mycon.cursor()
    qr1="select * from subject"
    cur.execute(qr1)
    lis=cur.fetchall()
    for i in lis:
        tv.insert("",END,values=i)
    mycon.close()

#bind select to insert the details in the treeview to the Entry
def select(event):
    cursor_r=tv.focus()
    content=tv.item(cursor_r)
    row=content["values"]
    scode_var.set(row[0])
    name_var.set(row[1])
    hour_var.set(row[3])
    semcomb_var.set(row[4])

#to add subject details into subject table
def add():
    #To get the values in the Entry
    mycon=my.connect(host='localhost',user='root',
                     passwd='mysql',database='tts')
    cur=mycon.cursor()
    scode=scode_ent.get()
    name=name_ent.get()
    faculty=faculty_var.get()
    hour=hour_ent.get()
    sem=semcomb_var.get()
    if(scode=="" or name=="" or sem=="" or hour=="" or faculty==""):
        #if the entries are empty this message will be shown
        msb.showinfo("Insert status","All fields are required") 
    else:
            mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
            cur=mycon.cursor()
            #to insert subject details into subject table
            tup=(scode,name,faculty,hour,sem)
            att.Subject(name, scode,faculty, hour, sem)
            qr1="insert into subject(scode,name,faculty,hour,sem) values(%s,%s,%s,%s,%s)"
            cur.execute(qr1,tup)
            mycon.commit()
            #insert the subject details to treeview
            row=(scode,name,faculty,hour,sem)
            tv.insert("",END,values=row)
            #clear entries
            scode_ent.delete(0,'end')
            name_ent.delete(0,'end')
            hour_ent.delete(0,'end')
            msb.showinfo("STATUS","succesfully added")


#to update subject details
def update():
    #get the entry values
    scode=scode_ent.get()
    name=name_ent.get()
    faculty=faculty_var.get()
    sem=semcomb_var.get()
    hour=hour_ent.get()
    if(scode=="" or name=="" or sem=="" or faculty=="" or hour==""):
        #if the entries are empty this message will be shown
        msb.showinfo("update status","All fields are required")    
    else:
        mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
        cur=mycon.cursor()
        #to update subject table
        tup=(name,faculty,hour,sem,scode)
        qr6="update subject set name=%s,faculty=%s,hour=%s,sem=%s where scode=%s"
        cur.execute(qr6,tup)
        mycon.commit()
        #delete the selected subject from treeview and show the full the details
        tv.delete(*tv.get_children())
        show()
        #to clear entries
        scode_ent.delete(0,'end')
        name_ent.delete(0,'end')
        hour_ent.delete(0,'end')
        msb.showinfo("update status","succesfully updated")
        mycon.close()

#to delete subject information
def remove():
    #to get the entry values
    scode=scode_ent.get()
    name=name_ent.get()
    faculty=faculty_var.get()
    hour=hour_ent.get()
    sem=semcomb_var.get()
    if(scode==""):
         #if the entry is empty this message will be shown
        msb.showinfo("DELETE STATUS","employee id  is compalsary for delete") 
    else:
        mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
        cur=mycon.cursor()
        #to delete the subject information from subject table
        tup=(scode,)
        qr5="delete from subject where scode=%s"
        cur.execute(qr5,tup)
        mycon.commit()
        #to clear the entries
        scode_ent.delete(0,'end')
        name_ent.delete(0,'end')
        hour_ent.delete(0,'end')
        #to delete the selected subject from treeview
        selected_item=tv.selection()[0] 
        tv.delete(selected_item)
        msb.showinfo("delete status","succesfully deleted")
        mycon.close()

def inp_fac():
        mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
        cur=mycon.cursor()
        qr6="select name from faculty"
        cur.execute(qr6)
        rows = cur.fetchall()
        cur.close()
        mycon.close()
        return rows  

#to clear entries
def clear():
    scode_ent.delete(0,'end')
    name_ent.delete(0,'end')
    
#to search  a subject
def find():
     tv.delete()                      #delete the information in treeview
     #to get the combobox,searchentry values               
     comb=comb_var.get()
     ent=csearch_var.get()
     mycon=my.connect(host='localhost',user='root',
                      passwd='mysql',database='tts')
     cur=mycon.cursor()
     tup=(comb,ent)
     if(comb=='SUB CODE'):                              #search by emp id
         tv.delete(*tv.get_children())
         tup=(ent,)
         qr1="select * from subject where scode='%s'"
         cur.execute(qr1%tup)
         lis1=cur.fetchall()
         for i in lis1:
             tv.insert("",END,values=i)     #insert teh result into treeview
         mycon.close()
     elif(comb=='SUB Name'):                #search by emp name
        tv.delete(*tv.get_children())
        tup2=(ent,)
        qr2="select * from subject where name='%s'"
        cur.execute(qr2%tup2)
        lis2=cur.fetchall()
        for j in lis2:
            tv.insert("",END,values=j)    #insert teh result into treeview
        mycon.close()

#to delete the searched information and insert full details of cars
def refresh():
    tv.delete(*tv.get_children())
    show()

#to close the window
def close():
    clos=msb.askyesno("ELTTS-Subject","do you want to exit")
    if clos > 0:
        app.destroy()
        return

#frame1
fr1=Frame(app,width=960,height=30)
fr1.place(x=0,y=0)
lbl1=Label(app,text='SUBJECT DETAILS',font=80)
lbl1.place(x=360,y=0)

#scode textvariable,label,entry
scode_var=StringVar()
scode_lb=Label(app,text="SUB CODE",bg='RoyalBlue4')
scode_lb.place(x=10,y=50)
scode_ent=Entry(app,textvariable=scode_var)
scode_ent.place(x=100,y=50)
#name  textvariable,label,entry
name_var=StringVar()
name_lb=Label(app,text="NAME",bg='RoyalBlue4')
name_lb.place(x=10,y=100)
name_ent=Entry(app,textvariable=name_var)
name_ent.place(x=100,y=100)


#hour  textvariable,label,entry
hour_var=StringVar()
hour_lb=Label(app,text="HOURS REQ",bg='RoyalBlue4')
hour_lb.place(x=10,y=150)
hour_ent=Entry(app,textvariable=hour_var)
hour_ent.place(x=100,y=150)
# semester textvariable,label,entry,combobox
sem_var=StringVar()
sem_lb=Label(app,text="SEMESTER",bg='RoyalBlue4')
sem_lb.place(x=10,y=200)
semcomb_var=StringVar()
semcomb=ttk.Combobox(app,textvariable=semcomb_var,state='readonly')
semcomb['values']=('S1','S2','S3','S4','S5','S6','S7','S8')
semcomb.place(x=100,y=200)

# faculty textvariable,label,entry,combobox
faculty_var=StringVar()
faculty_lb=Label(app,text="FACULTY",bg='RoyalBlue4')
faculty_lb.place(x=10,y=250)
facultycomb_var=StringVar()
facultycomb=ttk.Combobox(app,textvariable=faculty_var,state='readonly')
values=inp_fac()
data_tuple = tuple(values)
facultycomb['values']= data_tuple
facultycomb.place(x=100,y=250)

#add button
addbt=Button(app,text='ADD',width=12,command=add)
addbt.place(x=10,y=350)

#update button
updatebt=Button(app,text='UPDATE',width=12,command=update)
updatebt.place(x=120,y=350)

#remove button
removebt=Button(app,text='REMOVE',width=12,command=remove)
removebt.place(x=10,y=390)

#clear button
clearbt=Button(app,text='CLEAR INPUT',width=12,command=clear)
clearbt.place(x=120,y=390)

#cloase button
closbt=Button(app,text='Close',width=12,command=close)
closbt.place(x=840,y=390)

#combobox for options to search for a subject
comb_var=StringVar()
comb=ttk.Combobox(app,textvariable=comb_var,state='readonly')
comb['values']=('SUB CODE','SUB Name')
comb.place(x=250,y=80)

cmlb=Label(app,text="Search by:",bg='RoyalBlue4')
cmlb.place(x=250,y=50)
#search entry
csearch_var=StringVar()
csearchent=Entry(app,textvariable=csearch_var)
csearchent.place(x=400,y=80)
#search button
findbt=Button(app,text='Search',width=12,command=find)
findbt.place(x=540,y=80)

#treeview to display pending customer details
tv=ttk.Treeview(app,column=(1,2,3,4,5),show="headings",height='11')
tv.place(x=250,y=110)
#heading for each calumn
tv.heading(1,text="SUB CODE")
tv.heading(2,text="NAME")
tv.heading(3,text="FACULTY")
tv.heading(4,text="HOUR REQUIRED")
tv.heading(5,text="SEMESTER")
tv.column(1,width=120)
tv.column(2,width=160)
tv.column(3,width=160)
tv.column(4,width=100)
tv.column(5,width=80)

#scrollbar for treeview
scrollbar=ttk.Scrollbar(app)
scrollbar.place(x=880,y=150)
#set scroll to listbox
tv.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=tv.yview)

#refresh button for treeview
refbt=Button(app,text='<<',width=5,command=refresh)
refbt.place(x=880,y=210)
    
#bind select to insert details in the treeview to entries
tv.bind('<<TreeviewSelect>>',select)

#to insert the car details the treeview
show()

app.mainloop()