#=============================================================================#
                              #faculty                                   
#=============================================================================#

from tkinter import *
import tkinter as tk
import tkinter.messagebox as msb
import mysql.connector as my
from tkinter import ttk
#  GA imports 
from GA.assets import Attributes as att


#create window
app=Tk("Manage Faculties")
app.title("TIME TABLE SCHEDULER")
app.geometry("810x430")
app.configure(background='RoyalBlue4')

#icon for the window
#app.iconbitmap("images_ERc_icon.ico")

#craete database if not exist
mycon=my.connect(host='localhost',user='root',passwd='mysql')
cur=mycon.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS tts")
mycon.close()

#Create 'faculty' table if not exist
mycon=my.connect(host='localhost',user='root',passwd='mysql',database='tts')
cur=mycon.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS  faculty(fid VARCHAR(20) PRIMARY KEY,
            name VARCHAR(40),dept VARCHAR(40))""")
mycon.close()

#To show the faculty details in the Treeview
def show():
    mycon=my.connect(host='localhost',user='root',
                     passwd='mysql',database='tts')
    cur=mycon.cursor()
    qr1="select * from faculty"
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
    fid_var.set(row[0])
    name_var.set(row[1])
    deptcomb_var.set(row[4])

#to add faculty details into faculty table
def add():
    #To get the values in the Entry
    mycon=my.connect(host='localhost',user='root',
                     passwd='mysql',database='tts')
    cur=mycon.cursor()
    fid=fid_ent.get()
    name=name_ent.get()
    dept=deptcomb_var.get()
    if(fid=="" or name=="" or dept==""):
        #if the entries are empty this message will be shown
        msb.showinfo("Insert status","All fields are required") 
    else:
            mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
            cur=mycon.cursor()
            #to insert faculty details into faculty table
            tup=(fid,name,dept)
            att.Faculty(name, fid, dept)
            qr1="insert into faculty(fid,name,dept) values(%s,%s,%s)"
            cur.execute(qr1,tup)
            mycon.commit()
            #insert the faculty details to treeview
            row=(fid,name,dept)
            tv.insert("",END,values=row)
            #clear entries
            fid_ent.delete(0,'end')
            name_ent.delete(0,'end')
            msb.showinfo("STATUS","succesfully added")


#to update faculty details
def update():
    #get the entry values
    fid=fid_ent.get()
    name=name_ent.get()
    dept=deptcomb_var.get()
    if(fid=="" or name=="" or dept==""):
        #if the entries are empty this message will be shown
        msb.showinfo("update status","All fields are required")    
    else:
        mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
        cur=mycon.cursor()
        #to update faculty table
        tup=(name,dept,fid)
        qr6="update faculty set name=%s,dept=%s where fid=%s"
        cur.execute(qr6,tup)
        mycon.commit()
        #delete the selected faculty from treeview and show the full the details
        tv.delete(*tv.get_children())
        show()
        #to clear entries
        fid_ent.delete(0,'end')
        name_ent.delete(0,'end')
        msb.showinfo("update status","succesfully updated")
        mycon.close()

#to delete faculty information
def remove():
    #to get the entry values
    fid=fid_ent.get()
    name=name_ent.get()
    dept=deptcomb_var.get()
    if(fid==""):
         #if the entry is empty this message will be shown
        msb.showinfo("DELETE STATUS","Faculty Id  is compulsory for delete") 
    else:
        mycon=my.connect(host='localhost',user='root',
                         passwd='mysql',database='tts')
        cur=mycon.cursor()
        #to delete the faculty information from faculty table
        tup=(fid,)
        qr5="delete from faculty where fid=%s"
        cur.execute(qr5,tup)
        mycon.commit()
        #to clear the entries
        fid_ent.delete(0,'end')
        name_ent.delete(0,'end')
        #to delete the selected faculty from treeview
        selected_item=tv.selection()[0] 
        tv.delete(selected_item)
        msb.showinfo("delete status","succesfully deleted")
        mycon.close()


#to clear entries
def clear():
    fid_ent.delete(0,'end')
    name_ent.delete(0,'end')
    
#to search  a faculty
def find():
     tv.delete()                      #delete the information in treeview
     #to get the combobox,searchentry values               
     comb=comb_var.get()
     ent=csearch_var.get()
     mycon=my.connect(host='localhost',user='root',
                      passwd='mysql',database='tts')
     cur=mycon.cursor()
     tup=(comb,ent)
     if(comb=='EMP ID'):                              #search by emp id
         tv.delete(*tv.get_children())
         tup=(ent,)
         qr1="select * from faculty where fid='%s'"
         cur.execute(qr1%tup)
         lis1=cur.fetchall()
         for i in lis1:
             tv.insert("",END,values=i)     #insert teh result into treeview
         mycon.close()
     elif(comb=='EMP Name'):                #search by emp name
        tv.delete(*tv.get_children())
        tup2=(ent,)
        qr2="select * from faculty where name='%s'"
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
    clos=msb.askyesno("ELTTS-Faculty","do you want to exit")
    if clos > 0:
        app.destroy()
        return

#frame1
fr1=Frame(app,width=910,height=30)
fr1.place(x=0,y=0)
lbl1=Label(app,text='FACULTY DETAILS',font=80)
lbl1.place(x=310,y=0)

#fid textvariable,label,entry
fid_var=StringVar()
fid_lb=Label(app,text="FACULTY ID",bg='RoyalBlue4')
fid_lb.place(x=10,y=50)
fid_ent=Entry(app,textvariable=fid_var)
fid_ent.place(x=100,y=50)
#name  textvariable,label,entry
name_var=StringVar()
name_lb=Label(app,text="NAME",bg='RoyalBlue4')
name_lb.place(x=10,y=100)
name_ent=Entry(app,textvariable=name_var)
name_ent.place(x=100,y=100)
# dpartment textvariable,label,entry,combobox
dept_var=StringVar()
dept_lb=Label(app,text="DEPARTMENT",bg='RoyalBlue4')
dept_lb.place(x=10,y=150)
deptcomb_var=StringVar()
deptcomb=ttk.Combobox(app,textvariable=deptcomb_var,state='readonly')
deptcomb['values']=('IT','CSE','MCA','MATHS','ECE','EEE','MECHANICAL','CE')
deptcomb.place(x=100,y=150)

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
closbt.place(x=710,y=390)

#combobox for options to search for a faculty
comb_var=StringVar()
comb=ttk.Combobox(app,textvariable=comb_var,state='readonly')
comb['values']=('EMP ID','EMP Name')
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
tv=ttk.Treeview(app,column=(1,2,3),show="headings",height='11')
tv.place(x=250,y=110)
#heading for each calumn
tv.heading(1,text="FAC_ID")
tv.heading(2,text="NAME")
tv.heading(3,text="DEPARTMENT")
tv.column(1,width=160)
tv.column(2,width=160)
tv.column(3,width=160)

#scrollbar for treeview
scrollbar=ttk.Scrollbar(app)
scrollbar.place(x=740,y=150)
#set scroll to listbox
tv.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=tv.yview)

#refresh button for treeview
refbt=Button(app,text='<<',width=5,command=refresh)
refbt.place(x=740,y=210)
    
#bind select to insert details in the treeview to entries
tv.bind('<<TreeviewSelect>>',select)

#to insert the car details the treeview
show()

app.mainloop()