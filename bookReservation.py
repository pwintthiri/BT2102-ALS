from ast import AsyncFunctionDef
from tkinter import *
from unittest import findTestCases
from venv import create
from PIL import ImageTk, Image
import tkinter.messagebox
from datetime import *
import datetime
import tkinter as tk
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Column
import pymysql
import pymysql.cursors
import tkinter.font as tkFont
from dateutil.parser import parse
import pandas as pd
import os 
engine = engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
metadata_object = db.MetaData()
connection = engine.connect()
metadata_object.reflect(bind = engine)

#Tables Created
book = db.Table('Book', metadata_object, autoload=True, autoload_with=engine)
members = db.Table('Members', metadata_object, autoload=True, autoload_with=engine)
authors = db.Table('Authors', metadata_object, autoload=True, autoload_with=engine)
fine = db.Table('Fine', metadata_object, autoload=True, autoload_with=engine)
reservation = db.Table('Reservation', metadata_object, autoload=True, autoload_with=engine)

book_reservation = Tk()
book_reservation.title("Reservation 2nd Page")
book_reservation.configure(background = "white")
book_reservation.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(book_reservation, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "turquoise", width = 400)
header = Label(header_frame, text = "To Reserve a Book, Please Enter Information Below:", bg = "turquoise", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 30, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 100, ipady = 20)

# Accession Number
accessionnumber_frame = Frame(bg = "DeepSkyBlue3", width = 200, height = 200)
accessionnumber = Label(accessionnumber_frame, text = "Accession Number:", bg = "DeepSkyBlue3", fg = "white", font = "Arial 18")

accessionnumber_frame.place(x = 150, y = 130)
accessionnumber.pack(ipadx = 40, ipady = 30)

accessionnumber_entry = Entry(book_reservation, width = 35, font = "Arial 25", highlightthickness = 4)
accessionnumber_entry.place(x = 470, y = 150)

# Membership ID
memberid_frame = Frame(bg = "blue", width = 200, height = 200)
memberid = Label(memberid_frame, text = "Membership ID:", bg = "blue", fg = "white", font = "Arial 18")

memberid_frame.place(x = 150, y = 260)
memberid.pack(ipadx = 60, ipady = 30)

memberid_entry = Entry(book_reservation, width = 35, font = "Arial 25", highlightthickness = 4)
memberid_entry.place(x = 470, y = 280)

# Reserve Date Label
reservedate_frame = Frame(bg = "SlateBlue3", width = 150, height = 200)
reservedate = Label(reservedate_frame, text = "Reserve Date:", bg = "SlateBlue3", fg = "white", font = "Arial 18")

reservedate_frame.place(x = 150, y = 390)
reservedate.pack(ipadx = 70, ipady = 30)

reservedate_entry = Entry(book_reservation, width = 35, font = "Arial 25", highlightthickness = 4)
reservedate_entry.insert(0, "Reservation Date in format: YYYY-MM-DD")
reservedate_entry.place(x = 470, y = 410)

def book_in_library():
    engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
    metadata_object = db.MetaData()
    connection = engine.connect()
    metadata_object.reflect(bind = engine)

    with engine.connect() as connection:
        r1 = connection.execute(db.text("select * from Book"))

    with engine.connect() as connection:
        example_sel = book.select()
        example_sel_result = connection.execute(example_sel)
        for row in example_sel_result:
            if row[0] == accessionnumber_entry.get():
                return True
            else:
                continue
        return False

def not_reserved():
    engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
    metadata_object = db.MetaData()
    connection = engine.connect()
    metadata_object.reflect(bind = engine)

    with engine.connect() as connection:
        r1 = connection.execute(db.text("select * from Reservation"))

    with engine.connect() as connection:
        reservation_sel = reservation.select()
        reservation_sel_result = connection.execute(reservation_sel)
        for row in reservation_sel_result:
                        if row[0] == accessionnumber_entry.get():
                                return False
                        else:
                                return True

def no_outstanding_fine():
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
            if row[0] == memberid_entry.get():
                if row[2] == 0:
                    return True
                else:
                    return False
            continue
        return True

def not_exceeded_quota():
        engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
        metadata_object = db.MetaData()
        connection = engine.connect()
        metadata_object.reflect(bind = engine)
        
        with engine.connect() as connection:
                r1 = connection.execute(db.text("select * from Reservation"))
                
        with engine.connect() as connection:
                reservation_sel = reservation.select()
                reservation_sel_result = connection.execute(reservation_sel)
                reservations = []
                for row in reservation_sel_result:
                        if row[1] == memberid_entry.get():
                                reservations.append(row[0])
                if len(reservations) < 2:
                        return True
                else:
                        return False
    
def fine_amt():
    with engine.connect() as connection:
        fine_table = connection.execute(db.text("select * from Fine"))
        with engine.connect() as connection:
            fine_sel = fine.select()
            fine_sel_result = connection.execute(fine_sel)

            for row in fine_sel_result:
                if row[0] == memberid_entry.get():
                                        return row[2]

def book_title():
    with engine.connect() as connection:
        book_table = connection.execute(db.text("select * from Book"))
        with engine.connect() as connection:
            book_sel = book.select()
            book_sel_result = connection.execute(book_sel)
            for row in book_sel_result:
                if row[0] == accessionnumber_entry.get():
                    return row[1]
        
def member_name():
    with engine.connect() as connection:
        members_table = connection.execute(db.text("select * from Members"))
        with engine.connect() as connection:
            members_sel = members.select()
            members_sel_result = connection.execute(members_sel)
            for row in members_sel_result:
                if row[0] == memberid_entry.get():
                    return row[1]
                continue

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
            if row[0] == memberid_entry.get():
                return True
            else:
                continue
        return False



def valid_date():
        date_input = reservedate_entry.get()
        if date_input[0:4].isnumeric() and date_input[5:7].isnumeric() and date_input[8:10].isnumeric() and date_input[4] =="-" and date_input[7] =="-":
                answer = None
                year = int(date_input[0:4])
                month = int(date_input[5:7])
                day = int(date_input[8:10])
                try:
                        newDate = datetime.datetime(year, month, day)
                        answer = True
                except ValueError:
                        answer = False
                return answer
        else:
                return False 


def resbook():
        if book_in_library() and not_reserved() and not_exceeded_quota() and no_outstanding_fine() and existing_member() and valid_date():
                current_title = book_title()
                current_membname = member_name()
                
                toplevel = Toplevel(book_reservation, bg="lawn green")
                toplevel.geometry('500x550')
                l1_frame = Frame(toplevel, bg = "lawn green", width = 400, height=50)
                l1=Label(l1_frame,text="Confirm Reservation \n Details To Be Correct", font = "Arial 20 bold", fg="black", bg="lawn green")
                l1_frame.pack()
                l1.pack(ipadx = 20, ipady = 20)
                
                check_accessionnumber_frame = LabelFrame(toplevel, text = "Accession Number", font = "Arial 12 bold", bg = "lawn green", height = 4)
                check_accessionnumber = Label(check_accessionnumber_frame,text= accessionnumber_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
                check_accessionnumber_frame.pack(fill=X)
                check_accessionnumber.pack(ipady = 5)
                
                check_booktitle_frame = LabelFrame(toplevel, text = "Book Title", font = "Arial 12 bold", bg = "lawn green", height = 4)
                check_booktitle = Label(check_booktitle_frame,text= current_title, font = "Arial 12", fg="black", bg="lawn green")
                check_booktitle_frame.pack(fill=X)
                check_booktitle.pack(ipady = 5)
                
                check_memberid_frame = LabelFrame(toplevel, text = "Membership ID", font = "Arial 12 bold", bg = "lawn green", height = 4)
                check_memberid = Label(check_memberid_frame,text= memberid_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
                check_memberid_frame.pack(fill=X)
                check_memberid.pack(ipady = 5)
                
                check_membername_frame = LabelFrame(toplevel, text = "Member Name", font = "Arial 12 bold", bg = "lawn green", height = 4)
                check_membername = Label(check_membername_frame,text = current_membname, font = "Arial 12", fg="black", bg="lawn green")
                check_membername_frame.pack(fill=X)
                check_membername.pack(ipady = 5)
                
                check_reservedate_frame = LabelFrame(toplevel, text = "Reserve Date", font = "Arial 12 bold", bg = "lawn green", height = 4)
                check_reservedate = Label(check_reservedate_frame,text= reservedate_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
                check_reservedate_frame.pack(fill=X)
                check_reservedate.pack(ipady = 5)
                
                blank_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
                blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="lawn green", bg="lawn green")
                blank_frame.pack()
                blank.pack(ipadx = 15, ipady = 10)

        # Reserve Book
                def reserve_book():
                        engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
                        metadata_object = db.MetaData()
                        connection = engine.connect()
                        metadata_object.reflect(bind = engine)

            #add membership to Book table
                        connection.execute("""
                        INSERT INTO Reservation VALUES (%s, %s, %s)
            """, (accessionnumber_entry.get(), memberid_entry.get(), reservedate_entry.get()))
                        
                        toplevel.destroy()
                        
                button1_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
                button1 = Button(button1_frame,text="Confirm \n Reservation", bg = "powder blue", fg = "black", font = "Arial 10 bold", command= reserve_book, width=15)
                button1_frame.pack(padx = 50, pady = 15, side = LEFT)
                button1.pack(ipadx = 10, ipady = 5)
                
                button2_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
                button2 = Button(button2_frame,text="Back to \n Reserve \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button2_frame.pack(padx = 50, pady = 15, side = LEFT)
                button2.pack(ipadx = 10, ipady = 5)
    
    # Book is reserved
        elif not_reserved() == False:
                toplevel = Toplevel(book_reservation, bg="red")
                toplevel.geometry('300x300')
                
                errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
                errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
                errortxt_frame.pack()
                errortxt.pack(ipadx = 20, ipady = 20)
                
                errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=2)
                errcontent = Label(errcontent_frame,text= "Book is currently reserved by another Member.", font = "Arial 10", fg="yellow", bg="red")
                errcontent_frame.pack()
                errcontent.pack(ipadx = 15, ipady = 10)
                
                blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
                blank_frame.pack()
                blank.pack(ipadx = 15, ipady = 10)
                
                button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                button1 = Button(button1_frame,text="Back to \n Reserve \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button1_frame.pack()
                button1.pack(ipadx = 10, ipady = 5)

    # Exceeded Reservation Quota
        elif not_exceeded_quota() == False:
                toplevel = Toplevel(book_reservation, bg="red")
                toplevel.geometry('300x300')
                
                errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
                errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
                errortxt_frame.pack()
                errortxt.pack(ipadx = 20, ipady = 20)
                
                errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=2)
                errcontent = Label(errcontent_frame,text= "Member currently has \n 2 Books on Reservation.", font = "Arial 10", fg="yellow", bg="red")
                errcontent_frame.pack()
                errcontent.pack(ipadx = 15, ipady = 10)
                
                blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
                blank_frame.pack()
                blank.pack(ipadx = 15, ipady = 10)
                
                button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                button1 = Button(button1_frame,text="Back to \n Reserve \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button1_frame.pack()
                button1.pack(ipadx = 10, ipady = 5)

    # Member has outstanding fine
        elif no_outstanding_fine() == False:
                toplevel = Toplevel(book_reservation, bg="red")
                toplevel.geometry('300x300')
                
                errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
                errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
                errortxt_frame.pack()
                errortxt.pack(ipadx = 20, ipady = 20)
                
                errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=2)
                fine_text = "Member has Outstanding Fine of: \n $" + str(fine_amt())
                errcontent = Label(errcontent_frame,text= fine_text, font = "Arial 10", fg="yellow", bg="red")
                errcontent_frame.pack()
                errcontent.pack(ipadx = 15, ipady = 10)
                
                blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
                blank_frame.pack()
                blank.pack(ipadx = 15, ipady = 10)
                
                button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                button1 = Button(button1_frame,text="Back to \n Reserve \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button1_frame.pack()
                button1.pack(ipadx = 10, ipady = 5)

    # Book is not in Library
        elif book_in_library() == False:
                toplevel = Toplevel(book_reservation, bg="red")
                toplevel.geometry('300x300')
                
                errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
                errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
                errortxt_frame.pack()
                errortxt.pack(ipadx = 20, ipady = 20)
                
                errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=2)
                errcontent = Label(errcontent_frame,text= "Book does not exist in Library.", font = "Arial 10", fg="yellow", bg="red")
                errcontent_frame.pack()
                errcontent.pack(ipadx = 15, ipady = 10)
                
                blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
                blank_frame.pack()
                blank.pack(ipadx = 15, ipady = 10)
                
                button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                button1 = Button(button1_frame,text="Back to \n Reserve \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button1_frame.pack(padx = 50, pady = 15, side = LEFT)
                button1.pack(ipadx = 10, ipady = 5)

        elif existing_member() == False:
                toplevel = Toplevel(book_reservation, bg="red")
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
                button1 = Button(button1_frame,text="Back to \n Reserve \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button1_frame.pack()
                button1.pack(ipadx = 10, ipady = 5)

        elif valid_date() == False:
                toplevel = Toplevel(book_reservation, bg="red")
                toplevel.geometry('300x300')
                
                errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
                errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
                errortxt_frame.pack()
                errortxt.pack(ipadx = 20, ipady = 20)
                
                errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                errcontent = Label(errcontent_frame,text="Incorrect Reservation Date Format.", font = "Arial 10", fg="yellow", bg="red")
                errcontent_frame.pack()
                errcontent.pack(ipadx = 15, ipady = 10)
                
                blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
                blank_frame.pack()
                blank.pack(ipadx = 15, ipady = 10)
                
                button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                button1 = Button(button1_frame,text="Back to \n Reserve \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button1_frame.pack()
                button1.pack(ipadx = 10, ipady = 5)



# Reserve Book Button
create_frame_boarder = Frame(book_reservation, bg = "gold")
create_frame = Frame(create_frame_boarder, bg = "turquoise", width = 100)
create_button = Button(create_frame, text = "Reserve Book", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = resbook)

create_frame_boarder.place(x = 350, y = 500)
create_frame.pack(padx = 5, pady = 5)
create_button.pack(ipadx = 35, ipady = 10)

# Back to Main Reservations Button
def backtomain():
        book_reservation.destroy()
        os.system('python mainReservation.py')

btmm_frame_boarder = Frame(book_reservation, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to Main Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 500)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 10, ipady = 10)


book_reservation.mainloop()
