from ast import AsyncFunctionDef
from asyncore import loop
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
from datetime import *
import datetime
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

returnloan = Tk()
returnloan.title("Return Loan")
returnloan.configure(background = "white")
returnloan.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(returnloan, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "turquoise", width = 400)
header = Label(header_frame, text = "To Return a Book, Please Enter Information Below:", bg = "turquoise", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Acession Number
anum_frame = Frame(bg = "DeepSkyBlue3", width = 200, height = 200)
anum = Label(anum_frame, text = "Accession Number:", bg = "DeepSkyBlue3", fg = "white", font = "Arial 18")

anum_frame.place(x = 160, y = 235)
anum.pack(ipadx = 40, ipady = 18)

anum_entry = Entry(returnloan, width = 58, font = "Arial 15", highlightthickness = 4)
anum_entry.insert(0, "Enter Accession Number")
anum_entry.place(x = 470, y = 250)

# Return Date
date_frame = Frame(bg = "DeepSkyBlue2", width = 200, height = 200)
date_label = Label(date_frame, text = "Return Date:", bg = "DeepSkyBlue2", fg = "white", font = "Arial 18")

date_frame.place(x = 160, y = 350)
date_label.pack(ipadx = 75, ipady = 18)

date_entry = Entry(returnloan, width = 58, font = "Arial 15", highlightthickness = 4)
date_entry.insert(0, "Date of Return in Format: YYYY-MM-DD")
date_entry.place(x = 470, y = 370)

# back to main menu button
def backtomain():
    returnloan.destroy()
    import mainLoans

btmm_frame_boarder = Frame(returnloan, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to Loans Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 550)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 10, ipady = 23)

#checkValidity of date 
def valid_date():
        date_input = date_entry.get()
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


##return fine amount 

def fine_amt():
    print("fine_amt()")
    engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
    metadata_object = db.MetaData()
    connection = engine.connect()
    metadata_object.reflect(bind = engine)

    with engine.connect() as connection:
        r1 = connection.execute(db.text("select * from Book"))

    with engine.connect() as connection:
        book_sel = book.select()
        book_sel_result = connection.execute(book_sel)
        fine_amount = connection.execute("""SELECT DATEDIFF((%s), b.dueDate) AS DiffDate
                                                FROM Book b
                                                WHERE b.membershipID = (%s);""",(date_entry.get(), info()[1]))
        fineamt = 0
        for row in fine_amount: 
            fineamt = int(row[0])
        print(fineamt)
    if fineamt > 0:
        print("if")
        print(fineamt)
        return fineamt
    else:
        print("else")
        print(fine_amt)
        return 0


#get membershipID and title
def info():
    with engine.connect() as connection:
        book_table = connection.execute(db.text("select * from Book"))
        with engine.connect() as connection:
            book_sel = book.select()
            book_sel_result = connection.execute(book_sel)
            for row in book_sel_result:
                if row[0] == anum_entry.get():
                    current_title = row[2]
                    current_memberid  = row[5]
                    return (current_title, current_memberid)
#get membername
def member_name():
    with engine.connect() as connection:
        members_table = connection.execute(db.text("select * from Members"))
        with engine.connect() as connection:
            members_sel = members.select()
            members_sel_result = connection.execute(members_sel)
            for row in members_sel_result:
                if row[0] == info()[1]:
                    return row[1]
#check if book exist
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
            if row[0] == anum_entry.get():
                    if row[5]!=None:
                        return True
                    else:
                        return False
            else:
                continue
        return False
    
def total_fine():
    if fine_amt() > 0:
        return fine_amt() + prev_fine()
    else:
        return prev_fine()

#leadingto popup    
def return_book():
    if valid_date() and book_in_library(): #all entry valid
        this_title = info()[0]
        this_memberid = info()[1]
        memberid = this_memberid
        this_membername = member_name()  
        this_fine = fine_amt()
        store_fine = this_fine
            
        toplevel = Toplevel(returnloan, bg="lawn green")
        toplevel.geometry('500x550')
        l1_frame = Frame(toplevel, bg = "lawn green", width = 400, height=50)
        l1=Label(l1_frame,text="Confirm Return Details \n To Be Correct", font = "Arial 20 bold", fg="black", bg="lawn green")
        l1_frame.pack()
        l1.pack(ipadx = 20, ipady = 20)
            
        check_accessionnumber_frame = LabelFrame(toplevel, text = "Accession Number", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_accessionnumber = Label(check_accessionnumber_frame,text= anum_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
        check_accessionnumber_frame.pack(fill=X)
        check_accessionnumber.pack(ipady = 5)
            
        check_booktitle_frame = LabelFrame(toplevel, text = "Book Title", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_booktitle = Label(check_booktitle_frame,text= this_title, font = "Arial 12", fg="black", bg="lawn green")
        check_booktitle_frame.pack(fill=X)
        check_booktitle.pack(ipady = 5)
            
        check_memberid_frame = LabelFrame(toplevel, text = "Membership ID", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_memberid = Label(check_memberid_frame,text= this_memberid, font = "Arial 12", fg="black", bg="lawn green")
        check_memberid_frame.pack(fill=X)
        check_memberid.pack(ipady = 5)
            
        check_membername_frame = LabelFrame(toplevel, text = "Member Name", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_membername = Label(check_membername_frame,text= this_membername, font = "Arial 12", fg="black", bg="lawn green")
        check_membername_frame.pack(fill=X)
        check_membername.pack(ipady = 5)
            
        check_reservedate_frame = LabelFrame(toplevel, text = "Return Date", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_reservedate = Label(check_reservedate_frame,text= date_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
        check_reservedate_frame.pack(fill=X)
        check_reservedate.pack(ipady = 5)

        check_reservedate_frame = LabelFrame(toplevel, text = "Fine", font = "Arial 12 bold", bg = "lawn green", height = 4)
        check_reservedate = Label(check_reservedate_frame,text= "$" + str(this_fine), font = "Arial 12", fg="black", bg="lawn green")
        check_reservedate_frame.pack(fill=X)
        check_reservedate.pack(ipady = 5)
            
        blank_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="lawn green", bg="lawn green")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)



        

        def has_previous_fine():
            engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
            metadata_object = db.MetaData()
            connection = engine.connect()
            metadata_object.reflect(bind = engine)

            with engine.connect() as connection:
                fine_table = connection.execute(db.text("select * from Fine"))
            with engine.connect() as connection:
                fine_sel = fine.select()
                fine_sel_result = connection.execute(fine_sel)
        
                for row in fine_sel_result:
                    if row[0] == memberid:
                        return True
                return False
#get total previous fine amount 
        def prev_fine():
            with engine.connect() as connection:
                fine_table = connection.execute(db.text("select * from Fine"))
            with engine.connect() as connection:
                fine_sel = fine.select()
                fine_sel_result = connection.execute(fine_sel)

                prev_fine_amt = 0
                for row in fine_sel_result:
                    if row[0] == info()[1]:
                        prev_fine_amt += memberid

                    return int(prev_fine_amt)


        

        def whether_red_or_not():
            print("red or not")
            toplevel.destroy()
            engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
            metadata_object = db.MetaData()
            connection = engine.connect()
            metadata_object.reflect(bind = engine)
            connection.execute("""
            UPDATE Book
            SET returnDate = (%s), dueDate = NULL, borrowDate = NULL, membershipID = NULL
            WHERE accessionNumber = (%s)""", (date_entry.get(), anum_entry.get()))
            if store_fine > 0: #returned late, need warning table
                print("store_fine > 0")
                if has_previous_fine():
                    print("has prev fine")
                    engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
                    metadata_object = db.MetaData()
                    connection = engine.connect()
                    metadata_object.reflect(bind = engine)

                    connection.execute("""
                    UPDATE Fine
                    SET paymentDate = NULL, paymentAmount = (%s)
                    WHERE membershipID = (%s)""", (str(prev_fine() + store_fine), memberid))
            
                else:
            # if person did not have a fine previously, insert a new row
                    print("no prev fine")
                    engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
                    metadata_object = db.MetaData()
                    connection = engine.connect()
                    metadata_object.reflect(bind = engine)

                    connection.execute("""
                            INSERT INTO Fine VALUES (%s, NULL, %s)
                                """, (memberid, store_fine))
                toplevel1 = Toplevel(returnloan, bg="red")
                toplevel1.geometry('300x300')
            
                errortxt_frame = Frame(toplevel1, bg = "red", width = 300, height=50)
                errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
                errortxt_frame.pack()
                errortxt.pack(ipadx = 20, ipady = 20)

                errcontent_frame = Frame(toplevel1, bg = "red", width = 300, height=20)
                errcontent = Label(errcontent_frame,text="Book returned successfully \n but has fines.", font = "Arial 10", fg="yellow", bg="red")
                errcontent_frame.pack()
                errcontent.pack(ipadx = 15, ipady = 10)

                blank_frame = Frame(toplevel1, bg = "red", width = 300, height=20)
                blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
                blank_frame.pack()
                blank.pack(ipadx = 15, ipady = 10)

                button1_frame = Frame(toplevel1, bg = "red", width = 300, height=20)
                button1 = Button(button1_frame,text= "Back to \n Return \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button1_frame.pack()
                button1.pack(ipadx = 10, ipady = 5)

            else: # no fine now
                print("no fine now")
                toplevel.destroy()
                toplevel2 = Toplevel(returnloan, bg="red")
                toplevel2.geometry('300x300')
            
                errortxt_frame = Frame(toplevel2, bg = "lawn green", width = 300, height=50)
                errortxt = Label(errortxt_frame,text="Success!", font = "Arial 40", fg="yellow", bg="red")
                errortxt_frame.pack()
                errortxt.pack(ipadx = 20, ipady = 20)
    
                errcontent_frame = Frame(toplevel2, bg = "lawn green", width = 300, height=20)
                errcontent = Label(errcontent_frame,text="Book returned successfully.", font = "Arial 10", fg="yellow", bg="red")
                errcontent_frame.pack()
                errcontent.pack(ipadx = 15, ipady = 10)
    
                blank_frame = Frame(toplevel2, bg = "lawn green", width = 300, height=20)
                blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
                blank_frame.pack()
                blank.pack(ipadx = 15, ipady = 10)
    
                button1_frame = Frame(toplevel2, bg = "lawn green", width = 300, height=20)
                button1 = Button(button1_frame,text= "Back to \n Return \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                button1_frame.pack()
                button1.pack(ipadx = 10, ipady = 5)

                #button for first green confirmation popup 
        button1_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
        button1 = Button(button1_frame,text="Confirm \n Return", bg = "powder blue", fg = "black", font = "Arial 10 bold", command= whether_red_or_not, width=15)
        button1_frame.pack(padx = 50, pady = 15, side = LEFT)
        button1.pack(ipadx = 10, ipady = 5)
            
        button2_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
        button2 = Button(button2_frame,text="Back to \n Return \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        button2_frame.pack(padx = 50, pady = 15, side = LEFT)
        button2.pack(ipadx = 10, ipady = 5)

        

    elif book_in_library() == False:
        toplevel = Toplevel(returnloan, bg="red")
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
        button1 = Button(button1_frame,text="Back to \n Return \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        button1_frame.pack(padx = 50, pady = 15, side = LEFT)
        button1.pack(ipadx = 10, ipady = 5)
    
    elif valid_date() == False:
        toplevel = Toplevel(returnloan, bg="red")
        toplevel.geometry('300x300')
        
        errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
        errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
        errortxt_frame.pack()
        errortxt.pack(ipadx = 20, ipady = 20)
        
        errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        errcontent = Label(errcontent_frame,text="Incorrect Return Date Format.", font = "Arial 10", fg="yellow", bg="red")
        errcontent_frame.pack()
        errcontent.pack(ipadx = 15, ipady = 10)
        
        blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)
        
        button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        button1 = Button(button1_frame,text="Back to \n Return \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        button1_frame.pack()
        button1.pack(ipadx = 10, ipady = 5)




# return book button
delete_frame_boarder = Frame(returnloan, bg = "gold")
delete_frame = Frame(delete_frame_boarder, bg = "turquoise", width = 100)
delete_button = Button(delete_frame, text = "Return Book", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = return_book)

delete_frame_boarder.place(x = 350, y = 550)
delete_frame.pack(padx = 5, pady = 5)
delete_button.pack(ipadx = 35, ipady = 23)


returnloan.mainloop()
