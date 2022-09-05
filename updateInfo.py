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

######1033am
engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
metadata_object = db.MetaData()
connection = engine.connect()
metadata_object.reflect(bind = engine)

updateinfo_membership = Tk()
updateinfo_membership.title("Membership Update")
updateinfo_membership.configure(background = "white")
updateinfo_membership.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(updateinfo_membership, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "turquoise", width = 400)
header = Label(header_frame, text = "Please Enter Requested Information Below:", bg = "turquoise", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# extract name
def membershipID_from_previousPage():
        engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
        metadata_object = db.MetaData()
        connection = engine.connect()
        metadata_object.reflect(bind = engine)

        temporary = db.Table('Temporary', metadata_object, autoload=True, autoload_with=engine)
        with engine.connect() as connection:
            r1 = connection.execute(db.text("select * from Temporary"))
        with engine.connect() as connection:
            temporary_sel = temporary.select()
            temporary_sel_result = connection.execute(temporary_sel)
            for row in temporary_sel_result:
                    temp_id = row[0]
                    return row[0]


#Memb ID
membid_frame = Frame(bg = "SlateBlue1", width = 200, height = 200)
membid = Label(membid_frame, text = "Membership ID:", bg = "SlateBlue1", fg = "black", font = "Arial 18 bold")

membid_frame.place(x = 160, y = 115)
membid.pack(ipadx = 45, ipady = 18)

membid_entry = Entry(updateinfo_membership, width = 58, font = "Arial 15", highlightthickness = 4)
membid_entry.insert(0,membershipID_from_previousPage())
membid_entry.place(x = 470, y = 130)
membid_entry.config (state='disabled')


# Enter Name
name_frame = Frame(bg = "SlateBlue1", width = 200, height = 200)
name = Label(name_frame, text = "Name:", bg = "SlateBlue1", fg = "white", font = "Arial 18")

name_frame.place(x = 160, y = 190)
name.pack(ipadx = 100, ipady = 18)

name_entry = Entry(updateinfo_membership, width = 58, font = "Arial 15", highlightthickness = 4)
name_entry.insert(0, "Update Name")
name_entry.place(x = 470, y = 205)

# Enter Faculty
faculty_frame = Frame(bg = "SlateBlue1", width = 200, height = 200)
faculty = Label(faculty_frame, text = "Faculty:", bg = "SlateBlue1", fg = "white", font = "Arial 18")

faculty_frame.place(x = 160, y = 265)
faculty.pack(ipadx = 92, ipady = 18)

faculty_entry = Entry(updateinfo_membership, width = 58, font = "Arial 15", highlightthickness = 4)
faculty_entry.insert(0, "Update Faculty e.g., Computing, Engineering, Science, etc.")
faculty_entry.place(x = 470, y = 280)

# Enter Phone Number
number_frame = Frame(bg = "SlateBlue1", width = 200, height = 200)
number = Label(number_frame, text = "Phone Number:", bg = "SlateBlue1", fg = "white", font = "Arial 18")

number_frame.place(x = 160, y = 340)
number.pack(ipadx = 50, ipady = 18)

number_entry = Entry(updateinfo_membership, width = 58, font = "Arial 15", highlightthickness = 4)
number_entry.insert(0, "Update Phone Number")
number_entry.place(x = 470, y = 355)

# Enter Email Address
email_frame = Frame(bg = "SlateBlue1", width = 200, height = 200)
email = Label(email_frame, text = "Email Address:", bg = "SlateBlue1", fg = "white", font = "Arial 18")

email_frame.place(x = 160, y = 415)
email.pack(ipadx = 54, ipady = 18)

email_entry = Entry(updateinfo_membership, width = 58, font = "Arial 15", highlightthickness = 4)
email_entry.insert(0, "Update email address")
email_entry.place(x = 470, y = 430)

# back to main menu button
def backtomain():
    temp_id = str(membershipID_from_previousPage())
    engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
    metadata_object = db.MetaData()
    connection = engine.connect()
    metadata_object.reflect(bind = engine)
    connection.execute( """DELETE FROM Temporary
                        WHERE membershipID = (%s)
                        """, (temp_id))
    updateinfo_membership.destroy()
    os.system('python mainMembership.py')

btmm_frame_boarder = Frame(updateinfo_membership, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to\nMembership Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 550)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 10, ipady = 10)

def check_name():
    if len(name_entry.get()) == 0 or  len(name_entry.get()) > 30:
        return False
    else:
        return True

def check_faculty():
    if len(faculty_entry.get()) ==0 or len(faculty_entry.get()) >15:
        return False
    else:
        return True

def check_phone():
    if len(number_entry.get()) == 0 or len(number_entry.get()) > 10 :
        return False
    else:
        return True
def check_email():
    if len(email_entry.get()) == 0 or len(number_entry.get()) > 25 :
        return False
    else:
        return True

def total_check():
    if check_name() == False or check_faculty() == False or check_phone() == False or check_email() == False:
        return False
    else:
        return True


def update_Member_clicked_to_popups():
    if total_check() == True:
        def membershipID_from_previousPage1():
            engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
            metadata_object = db.MetaData()
            connection = engine.connect()
            metadata_object.reflect(bind = engine)
            temporary = db.Table('Temporary', metadata_object, autoload=True, autoload_with=engine)
            with engine.connect() as connection:
                r1 = connection.execute(db.text("select * from Temporary"))
            with engine.connect() as connection:
                temporary_sel = temporary.select()
                temporary_sel_result = connection.execute(temporary_sel)
                for row in temporary_sel_result:
                    return row[0]
                    
        temp_id = membershipID_from_previousPage1()
        toplevel1 = Toplevel(updateinfo_membership, bg="lawn green")
        toplevel1.geometry('500x550')
        l1_frame = Frame(toplevel1, bg = "lawn green", width = 400, height=50)
        l1=Label(l1_frame,text="Please Confirm Updated Details \nto Be Correct", font = "Arial 20 bold", fg="black", bg="lawn green")
        l1_frame.pack()
        l1.pack(ipadx = 20, ipady = 20)
    
        check_accessionnumber_frame = LabelFrame(toplevel1, text = "Member ID", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_accessionnumber = Label(check_accessionnumber_frame,text=temp_id , font = "Arial 12", fg="black", bg="lawn green")
        check_accessionnumber_frame.pack(fill=X)
        check_accessionnumber.pack(ipady = 5)

        check_booktitle_frame = LabelFrame(toplevel1, text = "Name", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_booktitle = Label(check_booktitle_frame,text= name_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
        check_booktitle_frame.pack(fill=X)
        check_booktitle.pack(ipady = 5)

        check_memberid_frame = LabelFrame(toplevel1, text = "Faculty", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_memberid = Label(check_memberid_frame,text= faculty_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
        check_memberid_frame.pack(fill=X)
        check_memberid.pack(ipady = 5)

        check_membername_frame = LabelFrame(toplevel1, text = "Phone Number", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_membername = Label(check_membername_frame,text=number_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
        check_membername_frame.pack(fill=X)
        check_membername.pack(ipady = 5)

        check_reservedate_frame = LabelFrame(toplevel1, text = "Email Address", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_reservedate = Label(check_reservedate_frame,text= email_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
        check_reservedate_frame.pack(fill=X)
        check_reservedate.pack(ipady = 5)

        blank_frame = Frame(toplevel1, bg = "lawn green", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="lawn green", bg="lawn green")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)
        def confirm_update_clicked():
            toplevel1.destroy()
            toplevel = Toplevel(updateinfo_membership, bg="lawn green")
            toplevel.geometry('300x300')
        
            successtxt_frame = Frame(toplevel, bg = "lawn green", width = 300, height=50)
            successtxt = Label(successtxt_frame,text="Success!", font = "Arial 40", fg="black", bg="lawn green")
            successtxt_frame.pack()
            successtxt.pack(ipadx = 20, ipady = 20)
        
            successmes_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
            successmes = Label(successmes_frame,text="ALS Membership Updated.", font = "Arial 10", fg="black", bg="lawn green")
            successmes_frame.pack()
            successmes.pack(ipadx = 15, ipady = 10)
        
            blank_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
            blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="lawn green", bg="lawn green")
            blank_frame.pack()
            blank.pack(ipadx = 15, ipady = 10)

            def update_Another_member_clicked():
                    toplevel.destroy()
                    updateinfo_membership.destroy()
                    os.system('python updateMember.py')
        
            leftbutton1_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
            leftbutton1 = Button(leftbutton1_frame,text="Update \n Another Member", bg = "powder blue", fg = "black", font = "Arial 10 bold", width=15, command = update_Another_member_clicked)
            leftbutton1_frame.place(x = 20, y = 200)
            leftbutton1.pack(ipadx = 10, ipady = 5)

            rightbutton1_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
            rightbutton1 = Button(rightbutton1_frame,text="Back to \n Update Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
            rightbutton1_frame.place(x = 160, y = 200)
            rightbutton1.pack(ipadx = 10, ipady = 5)

            engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
            metadata_object = db.MetaData()
            connection = engine.connect()
            metadata_object.reflect(bind = engine)
            connection.execute( """
                UPDATE Members
                SET MemberName = (%s)
                WHERE MembershipID = (%s)
            """, (name_entry.get(),temp_id))
            connection.execute( """
                UPDATE Members
                SET faculty = (%s)
                WHERE MembershipID = (%s)
            """, (faculty_entry.get(),temp_id))
            connection.execute( """
                UPDATE Members
                SET phoneNumber = (%s)
                WHERE MembershipID = (%s)
            """, (number_entry.get(),temp_id))
            connection.execute( """
                UPDATE Members
                SET emailAddress = (%s)
                WHERE MembershipID = (%s)
            """, (email_entry.get(),temp_id))

            engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
            metadata_object = db.MetaData()
            connection = engine.connect()
            metadata_object.reflect(bind = engine)
            connection.execute( """DELETE FROM Temporary
                        WHERE membershipID = (%s)
                        """, (temp_id))
            
        leftbutton_frame = Frame(toplevel1, bg = "red", width = 300, height=20)
        leftbutton = Button(leftbutton_frame,text="Confirm\nUpdate", bg = "powder blue", fg = "black", font = "Arial 10 bold", width=15, command = confirm_update_clicked)
        leftbutton_frame.place(x = 50, y = 450)
        leftbutton.pack(ipadx = 10, ipady = 5)

        
        rightbutton_frame = Frame(toplevel1, bg = "red", width = 300, height=20)
        rightbutton = Button(rightbutton_frame,text="Back to \n Update Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel1.destroy, width=15)
        rightbutton_frame.place(x = 300, y = 450)
        rightbutton.pack(ipadx = 10, ipady = 5)

    else: #red popup
        toplevel1 = Toplevel(updateinfo_membership, bg="red")
        toplevel1.geometry('300x300')
        
        errortxt_frame = Frame(toplevel1, bg = "red", width = 300, height=50)
        errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
        errortxt_frame.pack()
        errortxt.pack(ipadx = 20, ipady = 20)
        
        errcontent_frame = Frame(toplevel1, bg = "red", width = 300, height=20)
        errcontent = Label(errcontent_frame,text="Missing or \nIncomplete fields.", font = "Arial 10", fg="yellow", bg="red")
        errcontent_frame.pack()
        errcontent.pack(ipadx = 15, ipady = 10)
        
        blank_frame = Frame(toplevel1, bg = "red", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)

        button1_frame = Frame(toplevel1, bg = "red", width = 300, height=20)
        button1 = Button(button1_frame,text="Back to \n Update \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel1.destroy, width=15)
        button1_frame.pack()
        button1.pack(ipadx = 10, ipady = 5)
        
        
    

def temp_stored_memberID_deletion():
    engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
    metadata_object = db.MetaData()
    connection = engine.connect()
    metadata_object.reflect(bind = engine)
    connection.execute( """DELETE FROM Temporary
                        WHERE membershipID = (%s)
                        """, (temp_id))
 
        
# update member button
update_frame_boarder = Frame(updateinfo_membership, bg = "gold")
update_frame = Frame(update_frame_boarder, bg = "turquoise", width = 100)
update_button = Button(update_frame, text = "Update Member", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = update_Member_clicked_to_popups) # command = updatemember_2

update_frame_boarder.place(x = 350, y = 550)
update_frame.pack(padx = 5, pady = 5)
update_button.pack(ipadx = 35, ipady = 23)

updateinfo_membership.mainloop()
