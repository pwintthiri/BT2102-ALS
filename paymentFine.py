from re import T
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
from datetime import *
import pandas as pd
import os 

####1249AM

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

payfine = Tk()
payfine.title("Payment Fine")
payfine.configure(background = "white")
payfine.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(payfine, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "turquoise", width = 400)
header = Label(header_frame, text = "To Pay a Fine, Please Enter Information Below:", bg = "turquoise", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Membership ID
membid_frame = Frame(bg = "DeepSkyBlue3", width = 200, height = 200)
membid = Label(membid_frame, text = "Membership ID", bg = "DeepSkyBlue3", fg = "white", font = "Arial 18")

membid_frame.place(x = 160, y = 180)
membid.pack(ipadx = 40, ipady = 18)

membid_entry = Entry(payfine, width = 58, font = "Arial 15", highlightthickness = 4)
membid_entry.insert(0, "A unique alphanumeric id that distinguishes every member")
membid_entry.place(x = 470, y = 200)

# Payment Date
paydate_frame = Frame(bg = "DeepSkyBlue2", width = 200, height = 200)
paydate = Label(paydate_frame, text = "Payment Date:", bg = "DeepSkyBlue2", fg = "white", font = "Arial 18")

paydate_frame.place(x = 160, y = 270)
paydate.pack(ipadx = 63, ipady = 18)

paydate_entry = Entry(payfine, width = 58, font = "Arial 15", highlightthickness = 4)
paydate_entry.insert(0, "Date Payment Received, IN FORMAT YYYY_MM_DD")
paydate_entry.place(x = 470, y = 285)

# Payment Amount
payamount_frame = Frame(bg = "DeepSkyBlue1", width = 200, height = 200)
payamount = Label(payamount_frame, text = "Payment Amount:", bg = "DeepSkyBlue1", fg = "white", font = "Arial 18")

payamount_frame.place(x = 160, y = 360)
payamount.pack(ipadx = 47, ipady = 18)

payamount_entry = Entry(payfine, width = 58, font = "Arial 15", highlightthickness = 4)
payamount_entry.insert(0, "Total Fine amount")
payamount_entry.place(x = 470, y = 380)

# back to main menu button
def backtomain():
    payfine.destroy()
    os.system('python mainFines.py')

btmm_frame_boarder = Frame(payfine, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to\n Fines Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 550)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 25, ipady = 10)

def existing_member():
	engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
	metadata_object = db.MetaData()
	connection = engine.connect()
	metadata_object.reflect(bind = engine)

	with engine.connect() as connection:
		r1 = connection.execute(db.text("select * from Members"))

	with engine.connect() as connection:
		members_sel = members.select()
		members_sel_result = connection.execute(members_sel)
		for row in members_sel_result:
			if row[0] == membid_entry.get():
				return True
			else:
				continue
		return False

def has_fine():
    engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
    metadata_object = db.MetaData()
    connection = engine.connect()
    metadata_object.reflect(bind = engine)
    
    with engine.connect() as connection:
        r1 = connection.execute(db.text("select * from Fine"))
        
    with engine.connect() as connection:
        fine_sel = fine.select()
        fine_sel_result = connection.execute(fine_sel)
        for row in fine_sel_result:
            if row[0] == membid_entry.get():
                if row[2] == 0:
                    return False
                else:
                    return True
            continue
        return False

def fine_amt():
    engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
    metadata_object = db.MetaData()
    connection = engine.connect()
    metadata_object.reflect(bind = engine)
    
    with engine.connect() as connection:
        r1 = connection.execute(db.text("select * from Fine"))
        
    with engine.connect() as connection:
        fine_sel = fine.select()
        fine_sel_result = connection.execute(fine_sel)
        for row in fine_sel_result:
            if row[0] == membid_entry.get():
                payment_due = row[2]
                return payment_due
    
def paying_correct_amt():
    if payamount_entry.get().isnumeric() == True:

        if fine_amt() == int(payamount_entry.get()):
            return True
        else:
            return False
    else:
        return False



def check_day_and_amt_format():
    date_input = paydate_entry.get()
    if date_input[0:4].isnumeric() and date_input[5:6].isnumeric() and date_input[8:].isnumeric() and date_input[4] =="-" and date_input[7] =="-":
        return True
    else:
        return False 

def pay_fine():
    if existing_member() == False:
        toplevel = Toplevel(payfine, bg="red")
        toplevel.geometry('300x300')
        
        errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
        errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
        errortxt_frame.pack()
        errortxt.pack(ipadx = 20, ipady = 20)
        
        errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        errcontent = Label(errcontent_frame,text="Member does not exist.", font = "Arial 10", fg="yellow", bg="red")
        errcontent_frame.pack()
        errcontent.pack(ipadx = 15, ipady = 10)
        
        blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)
        
        button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        button1 = Button(button1_frame,text="Back to \n Payment \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        button1_frame.pack()
        button1.pack(ipadx = 10, ipady = 5)

    elif check_day_and_amt_format() == False:
        toplevel = Toplevel(payfine, bg="red")
        toplevel.geometry('300x300')
        
        errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
        errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
        errortxt_frame.pack()
        errortxt.pack(ipadx = 20, ipady = 20)
        
        errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        errcontent = Label(errcontent_frame,text="Incorrect payment date format.", font = "Arial 10", fg="yellow", bg="red")
        errcontent_frame.pack()
        errcontent.pack(ipadx = 15, ipady = 10)
        
        blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)
        
        button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        button1 = Button(button1_frame,text="Back to \n Payment \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        button1_frame.pack()
        button1.pack(ipadx = 10, ipady = 5)

    elif has_fine() == False:
        toplevel = Toplevel(payfine, bg="red")
        toplevel.geometry('300x300')
        
        errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
        errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
        errortxt_frame.pack()
        errortxt.pack(ipadx = 20, ipady = 20)
        
        errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        errcontent = Label(errcontent_frame,text="Member has no fine.", font = "Arial 10", fg="yellow", bg="red")
        errcontent_frame.pack()
        errcontent.pack(ipadx = 15, ipady = 10)
        
        blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)
        
        button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        button1 = Button(button1_frame,text="Back to \n Payment \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        button1_frame.pack()
        button1.pack(ipadx = 10, ipady = 5)
    
    elif paying_correct_amt() == False:
        toplevel = Toplevel(payfine, bg="red")
        toplevel.geometry('300x300')
        
        errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
        errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
        errortxt_frame.pack()
        errortxt.pack(ipadx = 20, ipady = 20)
        
        errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        errcontent = Label(errcontent_frame,text="Incorrect fine payment amount.", font = "Arial 10", fg="yellow", bg="red")
        errcontent_frame.pack()
        errcontent.pack(ipadx = 15, ipady = 10)
        
        blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)
        
        button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        button1 = Button(button1_frame,text="Back to \n Payment \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        button1_frame.pack()
        button1.pack(ipadx = 10, ipady = 5)



    
    else:
        payment_amt = fine_amt()
        payment_date = paydate_entry.get()
        
        toplevel = Toplevel(payfine, bg="lawn green")
        toplevel.geometry('500x550')
        l1_frame = Frame(toplevel, bg = "lawn green", width = 400, height=50)
        l1=Label(l1_frame,text="Please Confirm Details to\n Be Correct", font = "Arial 20 bold", fg="black", bg="lawn green")
        l1_frame.pack()
        l1.pack(ipadx = 20, ipady = 20)
        
        check_accessionnumber_frame = LabelFrame(toplevel, text = "Payment Due: ", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_accessionnumber = Label(check_accessionnumber_frame,text= payment_amt, font = "Arial 12", fg="black", bg="lawn green")
        check_accessionnumber_frame.pack(fill=X)
        check_accessionnumber.pack(ipady = 5)

        check_accessionnumber_frame = LabelFrame(toplevel, text = "MemberID", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_accessionnumber = Label(check_accessionnumber_frame,text= membid_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
        check_accessionnumber_frame.pack(fill=X)
        check_accessionnumber.pack(ipady = 5)

        check_accessionnumber_frame = LabelFrame(toplevel, text = "Exact Fee Only", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_accessionnumber = Label(check_accessionnumber_frame,text= payamount_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
        check_accessionnumber_frame.pack(fill=X)
        check_accessionnumber.pack(ipady = 5)

        check_accessionnumber_frame = LabelFrame(toplevel, text = "Payment Date ", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_accessionnumber = Label(check_accessionnumber_frame,text= payment_date, font = "Arial 12", fg="black", bg="lawn green")
        check_accessionnumber_frame.pack(fill=X)
        check_accessionnumber.pack(ipady = 5)
        
        blank_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="lawn green", bg="lawn green")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)

		# remove book from Book
        def actual_pay_fine():
            engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
            metadata_object = db.MetaData()
            connection = engine.connect()
            metadata_object.reflect(bind = engine)
            
            connection.execute("""
            UPDATE Fine SET paymentDate = (%s), paymentAmount = 0 WHERE membershipID = (%s)
            """, (payment_date, membid_entry.get()))
            
            toplevel.destroy()
            payfine.destroy()
            os.system('python root.py')
            
        button1_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
        button1 = Button(button1_frame,text="Confirm \n Payment", bg = "powder blue", fg = "black", font = "Arial 10 bold", command= actual_pay_fine, width=15)
        button1_frame.pack(padx = 50, pady = 15, side = LEFT)
        button1.pack(ipadx = 10, ipady = 5)
        
        button2_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
        button2 = Button(button2_frame,text="Back to \n Payment \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        button2_frame.pack(padx = 50, pady = 15, side = LEFT)
        button2.pack(ipadx = 10, ipady = 5)


# cancel reservation button
delete_frame_boarder = Frame(payfine, bg = "gold")
delete_frame = Frame(delete_frame_boarder, bg = "turquoise", width = 100)
delete_button = Button(delete_frame, text = "Pay Fine", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = pay_fine) 

delete_frame_boarder.place(x = 350, y = 550)
delete_frame.pack(padx = 5, pady = 5)
delete_button.pack(ipadx = 50, ipady = 23)

payfine.mainloop()
