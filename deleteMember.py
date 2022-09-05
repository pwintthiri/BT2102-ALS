from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
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


###### FRIDAY 914AM
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


delete_membership = Tk()
delete_membership.title("Membership Deletion")
delete_membership.configure(background = "white")
delete_membership.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(delete_membership, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "turquoise", width = 400)
header = Label(header_frame, text = "To Delete Member, Please Enter Membership ID:", bg = "turquoise", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Enter Memb ID
membid_frame = Frame(bg = "DeepSkyBlue3", width = 200, height = 200)
membid = Label(membid_frame, text = "Membership ID:", bg = "DeepSkyBlue3", fg = "white", font = "Arial 18")

membid_frame.place(x = 160, y = 235)
membid.pack(ipadx = 50, ipady = 18)

membid_entry = Entry(delete_membership, width = 58, font = "Arial 15", highlightthickness = 4)
membid_entry.insert(0, "Enter Membership ID")
membid_entry.place(x = 470, y = 250)

# back to main menu button
def backtomain():
	delete_membership.destroy()
	os.system('python mainMembership.py')

btmm_frame_boarder = Frame(delete_membership, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to\nMembership Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 550)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 10, ipady = 10)


####book table data 
with engine.connect() as connection:
    book_table = connection.execute(db.text("select * from Book"))
with engine.connect() as connection:
    book_sel = book.select()
    book_sel_result = connection.execute(book_sel)

####fine table data
with engine.connect() as connection:
    fine_table = connection.execute(db.text("select * from Fine"))
with engine.connect() as connection:
    fine_sel = fine.select()
    fine_sel_result = connection.execute(fine_sel)

## member table data

    
# to check if member has any borrowed book not returned 
def is_a_member():
    with engine.connect() as connection:
        member_table = connection.execute(db.text("select * from Members"))
    with engine.connect() as connection:
        member_sel = members.select()
        member_sel_result = connection.execute(member_sel)
    for row in member_sel_result:
        if row[0] == membid_entry.get():
            current_name = row[1]
            current_faculty = row[2]
            current_phone = row[3]
            current_email = row[4]
            return (row[1], row[2], row[3], row[4])
    return "fal"


def book_all_returned():
    for row in book_sel_result:
        if row[5] == membid_entry.get():
                return False
    return True


                
def fine_paid():
    for row in fine_sel_result:
        if row[0] == membid_entry.get() and row[-1] != 0:
                return False
    return True




def cancel_reservation(membid):
    engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
    metadata_object = db.MetaData()
    connection = engine.connect()
    metadata_object.reflect(bind = engine)
    with engine.connect() as connection:
        reservation_table = connection.execute(db.text("select * from Reservation"))
    with engine.connect() as connection:
        reservation_sel = reservation.select()
        reservation_sel_result = connection.execute(reservation_sel)
        for row in reservation_sel_result:
            if row[1] == membid_entry.get():
                
                connection.execute( """DELETE FROM Reservation
                                            WHERE membershipID = (%s)
                                        """, (membid))
                
def deletemember():
    if is_a_member() != "fal" and book_all_returned() == True and fine_paid() == True:
        cancel_reservation(membid_entry.get())
        temp_member_info = is_a_member()
        current_name = temp_member_info[0]
        current_faculty = temp_member_info[1]
        current_phone = temp_member_info[2]
        current_email = temp_member_info[3]

        toplevel = Toplevel(delete_membership, bg="lawn green")
        toplevel.geometry('500x550')
        l1_frame = Frame(toplevel, bg = "lawn green", width = 400, height=50)
        l1=Label(l1_frame,text="Please Confirm Details to\n Be Correct", font = "Arial 20 bold", fg="black", bg="lawn green")
        l1_frame.pack()
        l1.pack(ipadx = 20, ipady = 20)
    
        check_accessionnumber_frame = LabelFrame(toplevel, text = "Member ID", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_accessionnumber = Label(check_accessionnumber_frame,text= membid_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
        check_accessionnumber_frame.pack(fill=X)
        check_accessionnumber.pack(ipady = 5)

        check_booktitle_frame = LabelFrame(toplevel, text = "Name", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_booktitle = Label(check_booktitle_frame,text= current_name, font = "Arial 12", fg="black", bg="lawn green")
        check_booktitle_frame.pack(fill=X)
        check_booktitle.pack(ipady = 5)

        check_memberid_frame = LabelFrame(toplevel, text = "Faculty", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_memberid = Label(check_memberid_frame,text= current_faculty, font = "Arial 12", fg="black", bg="lawn green")
        check_memberid_frame.pack(fill=X)
        check_memberid.pack(ipady = 5)

        check_membername_frame = LabelFrame(toplevel, text = "Phone Number", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_membername = Label(check_membername_frame,text=current_phone, font = "Arial 12", fg="black", bg="lawn green")
        check_membername_frame.pack(fill=X)
        check_membername.pack(ipady = 5)

        check_reservedate_frame = LabelFrame(toplevel, text = "Email Address", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_reservedate = Label(check_reservedate_frame,text= current_email, font = "Arial 12", fg="black", bg="lawn green")
        check_reservedate_frame.pack(fill=X)
        check_reservedate.pack(ipady = 5)

        blank_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="lawn green", bg="lawn green")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)
        def actual_member_deletion():
            engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
            metadata_object = db.MetaData()
            connection = engine.connect()
            metadata_object.reflect(bind = engine)
            connection.execute( """DELETE FROM Members
                                            WHERE membershipID = (%s)
                                        """, (membid_entry.get()))

            toplevel.destroy()
            delete_membership.destroy()
            os.system('python root.py')

                # confirm reservation button # command missing
        leftbutton_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        leftbutton = Button(leftbutton_frame,text="Confirm\nDeletion", bg = "powder blue", fg = "black", font = "Arial 10 bold", width=15, command = actual_member_deletion)
        leftbutton_frame.place(x = 50, y = 450)
        leftbutton.pack(ipadx = 10, ipady = 5)

                # back to reserve button
        rightbutton_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        rightbutton = Button(rightbutton_frame,text="Back to \n Delete Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        rightbutton_frame.place(x = 300, y = 450)
        rightbutton.pack(ipadx = 10, ipady = 5)



    else:
        toplevel = Toplevel(delete_membership, bg="red")
        toplevel.geometry('300x300')
        l1_frame = Frame(toplevel, bg = "red", width = 300, height=50)
        l1=Label(l1_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
        l1_frame.pack()
        l1.pack(ipadx = 20, ipady = 20)
        l2_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        l2=Label(l2_frame,text="Member has loans \n reservations or outstanding fines.", font = "Arial 10", fg="yellow", bg="red")
        l2_frame.pack()
        l2.pack(ipadx = 15, ipady = 10)
        l3_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        l3=Label(l3_frame,text="                         ", font = "Arial 10", fg="yellow", bg="red")
        l3_frame.pack()
        l3.pack(ipadx = 15, ipady = 10)
        b1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        b1=Button(b1_frame,text="Back to \n Delete Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        b1_frame.pack()
        b1.pack(ipadx = 10, ipady = 5)

            

# delete member button
delete_frame_boarder = Frame(delete_membership, bg = "gold")
delete_frame = Frame(delete_frame_boarder, bg = "turquoise", width = 100)
delete_button = Button(delete_frame, text = "Delete Member", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = deletemember) 

delete_frame_boarder.place(x = 350, y = 550)
delete_frame.pack(padx = 5, pady = 5)
delete_button.pack(ipadx = 35, ipady = 23)

delete_membership.mainloop()
