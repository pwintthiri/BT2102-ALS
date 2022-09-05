from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
from datetime import date
import tkinter as tk
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Column
import pymysql
import pymysql.cursors
import tkinter.font as tkFont
import pandas as pd
import os

#### 355pm
engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
metadata_object = db.MetaData()
connection = engine.connect()
metadata_object.reflect(bind = engine)

#Tables Created
book = db.Table('Book', metadata_object, autoload=True, autoload_with=engine)
members = db.Table('Members', metadata_object, autoload=True, autoload_with=engine)
authors = db.Table('Authors', metadata_object, autoload=True, autoload_with=engine)
fine = db.Table('Fine', metadata_object, autoload=True, autoload_with=engine)
reservation = db.Table('Reservation', metadata_object, autoload=True, autoload_with=engine)


create_membership = Tk()
create_membership.title("Membership Creation")
create_membership.configure(background = "white")
create_membership.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(create_membership, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "turquoise", width = 400)
header = Label(header_frame, text = "To Create Member, Please Enter Requested Information Below:", bg = "turquoise", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 30, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 100, ipady = 20)

# refer to codemy codes on creating input fielda
# Enter Memb ID
membid_frame = Frame(bg = "DeepSkyBlue3", width = 200, height = 200)
membid = Label(membid_frame, text = "Membership ID:", bg = "DeepSkyBlue3", fg = "white", font = "Arial 18")

membid_frame.place(x = 160, y = 115)
membid.pack(ipadx = 50, ipady = 18)

membid_entry = Entry(create_membership, width = 58, font = "Arial 15", highlightthickness = 4)
membid_entry.insert(0, "Enter Membership ID")
membid_entry.place(x = 470, y = 130)

# Enter Name
name_frame = Frame(bg = "DeepSkyBlue2", width = 200, height = 200)
name = Label(name_frame, text = "Name:", bg = "DeepSkyBlue2", fg = "white", font = "Arial 18")

name_frame.place(x = 160, y = 190)
name.pack(ipadx = 100, ipady = 18)

name_entry = Entry(create_membership, width = 58, font = "Arial 15", highlightthickness = 4)
name_entry.insert(0, "Enter Name")
name_entry.place(x = 470, y = 205)

# Enter Faculty
faculty_frame = Frame(bg = "SteelBlue1", width = 200, height = 200)
faculty = Label(faculty_frame, text = "Faculty:", bg = "SteelBlue1", fg = "white", font = "Arial 18")

faculty_frame.place(x = 160, y = 265)
faculty.pack(ipadx = 92, ipady = 18)

faculty_entry = Entry(create_membership, width = 58, font = "Arial 15", highlightthickness = 4)
faculty_entry.insert(0, "e.g., Computing, Engineering, Science, etc.")
faculty_entry.place(x = 470, y = 280)

# Enter Phone Number
number_frame = Frame(bg = "SkyBlue2", width = 200, height = 200)
number = Label(number_frame, text = "Phone Number:", bg = "SkyBlue2", fg = "white", font = "Arial 18")

number_frame.place(x = 160, y = 340)
number.pack(ipadx = 50, ipady = 18)

number_entry = Entry(create_membership, width = 58, font = "Arial 15", highlightthickness = 4)
number_entry.insert(0, "e.g., 91234567, 81093487, 92054981, etc.")
number_entry.place(x = 470, y = 355)

# Enter Email Address
email_frame = Frame(bg = "SkyBlue1", width = 200, height = 200)
email = Label(email_frame, text = "Email Address:", bg = "SkyBlue1", fg = "white", font = "Arial 18")

email_frame.place(x = 160, y = 415)
email.pack(ipadx = 54, ipady = 18)

email_entry = Entry(create_membership, width = 58, font = "Arial 15", highlightthickness = 4)
email_entry.insert(0, "e.g., ALSuser@als.edu")
email_entry.place(x = 470, y = 430)

# back to main menu button
def backtomain():
    create_membership.destroy()
    os.system('python root.py')

btmm_frame_boarder = Frame(create_membership, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to\nMain Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 550)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 10, ipady = 10)


def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("1280x720")

#create membership table 
with engine.connect() as connection:
    r1 = connection.execute(db.text("select * from Members"))
with engine.connect() as connection:
    member_sel = members.select()
    member_sel_result = connection.execute(member_sel)

def membership_uniqueness():
        if len(membid_entry.get()) == 0 or len(membid_entry.get()) > 6:
                print ('length wrong')
                return False
        for rows in member_sel_result:
                
            if rows[0] == membid_entry.get():
                return False
        return True
def name_length():
    if len(name_entry.get())== 0 or len(name_entry.get())  > 30:
        return False
    else:
        return True

def faculty_length():
    if len(faculty_entry.get()) > 15 or len(faculty_entry.get()) == 0 :
        return False
    else:
        return True
        
def phone_length():
    if len(number_entry.get()) > 10 or len(number_entry.get()) ==0:
        return False
    else:
        return True
def email_length():
    if len(email_entry.get()) > 25 or len(email_entry.get()) == 0:
        return False
    else:
        return True

def actual_member_insertion():
        if membership_uniqueness() == True and name_length() == True and faculty_length() == True and  phone_length() == True and email_length() == True:
                engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
                metadata_object = db.MetaData()
                connection = engine.connect()
                metadata_object.reflect(bind = engine)
                connection.execute( """
INSERT INTO Members VALUES (%s,%s,%s,%s,%s)
            """, (membid_entry.get(), name_entry.get(), faculty_entry.get(),number_entry.get(), email_entry.get()))

        # Green window
                toplevel = Toplevel(create_membership, bg="lawn green")
                toplevel.geometry('300x300')
        
                successtxt_frame = Frame(toplevel, bg = "lawn green", width = 300, height=50)
                successtxt = Label(successtxt_frame,text="Success!", font = "Arial 40", fg="black", bg="lawn green")
                successtxt_frame.pack()
                successtxt.pack(ipadx = 20, ipady = 20)
        
                successmes_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
                successmes = Label(successmes_frame,text="ALS Membership Created.", font = "Arial 10", fg="black", bg="lawn green")
                successmes_frame.pack()
                successmes.pack(ipadx = 15, ipady = 10)
        
                blank_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
                blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="lawn green", bg="lawn green")
                blank_frame.pack()
                blank.pack(ipadx = 15, ipady = 10)
        
                button2_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
                button2 = Button(button2_frame,text="Back to \n Create \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button2_frame.pack()
                button2.pack(ipadx = 10, ipady = 5)
        
        else:
                toplevel = Toplevel(create_membership, bg="red")
                toplevel.geometry('300x300')
        
                errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
                errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
                errortxt_frame.pack()
                errortxt.pack(ipadx = 20, ipady = 20)
        
                errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                errcontent = Label(errcontent_frame,text="Member already exist; Missing or \n  Incomplete fields.", font = "Arial 10", fg="yellow", bg="red")
                errcontent_frame.pack()
                errcontent.pack(ipadx = 15, ipady = 10)
        
                blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
                blank_frame.pack()
                blank.pack(ipadx = 15, ipady = 10)
        
                button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                button1 = Button(button1_frame,text="Back to \n Create \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button1_frame.pack()
                button1.pack(ipadx = 10, ipady = 5)



# create member button
create_frame_boarder = Frame(create_membership, bg = "gold")
create_frame = Frame(create_frame_boarder, bg = "turquoise", width = 100)
create_button = Button(create_frame, text = "Create Member", bg = "turquoise", fg = "black", font = "Arial 15 bold",
                       command = actual_member_insertion) #command = createmember
create_frame_boarder.place(x = 350, y = 550)
create_frame.pack(padx = 5, pady = 5)
create_button.pack(ipadx = 35, ipady = 23)

create_membership.mainloop()
