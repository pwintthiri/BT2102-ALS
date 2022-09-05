from ast import AsyncFunctionDef
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
import os
import pandas as pd

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

bookwithdraw = Tk()
bookwithdraw.title("Withdraw Book")
bookwithdraw.configure(background = "white")
bookwithdraw.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(bookwithdraw, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "turquoise", width = 400)
header = Label(header_frame, text = "To Remove Outdated Books From System, Please Enter Required Information Below:", bg = "turquoise", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Enter Accession Number
anum_frame = Frame(bg = "DeepSkyBlue3", width = 200, height = 200)
anum = Label(anum_frame, text = "Accession Number", bg = "DeepSkyBlue3", fg = "white", font = "Arial 18")

anum_frame.place(x = 160, y = 235)
anum.pack(ipadx = 50, ipady = 18)

anum_entry = Entry(bookwithdraw, width = 58, font = "Arial 15", highlightthickness = 4)
anum_entry.insert(0, "Used to identify an instance of Book")
anum_entry.place(x = 470, y = 250)

# back to main menu button
def backtomain():
	bookwithdraw.destroy()
	os.system('python mainBooks.py')

btmm_frame_boarder = Frame(bookwithdraw, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to Books Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 550)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 10, ipady = 20)

#create Book table 
with engine.connect() as connection:
    r1 = connection.execute(db.text("select * from Book"))
with engine.connect() as connection:
    book_sel = book.select()
    book_sel_result = connection.execute(book_sel)


def book_info():
	with engine.connect() as connection:
		book_table = connection.execute(db.text("select * from Book"))
		with engine.connect() as connection:
			book_sel = book.select()
			book_sel_result = connection.execute(book_sel)
			for row in book_sel_result:
				if row[0] == anum_entry.get():
					current_title = row[1]
					current_isbn = row[2]
					current_publisher = row[3]
					current_pubyear = row[4]
					return (row[1], row[2], row[3], row[4])


def not_on_loan():
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

		# If book is on Loan - cannot withdraw
			if row[0] == anum_entry.get():
				if row[5] == None:
					return True
				else:
					return False
				
def this_authors():
	with engine.connect() as connection:
		authors_table = connection.execute(db.text("select * from Authors"))
	with engine.connect() as connection:
			authors_sel = authors.select()
			authors_sel_result = connection.execute(authors_sel)
			author_names = []
			for row in authors_sel_result:
				if row[1] == anum_entry.get():
					author_names.append(row[0])
			anames = author_names[0]
			if len(author_names) > 1:
				for i in range(0, len(author_names) - 1):
					anames += ", "
					anames += author_names[i + 1]
			return anames


def not_reserved():
	engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
	metadata_object = db.MetaData()
	connection = engine.connect()
	metadata_object.reflect(bind = engine)

	with engine.connect() as connection:
		r1 = connection.execute(db.text("select * from Reservation"))

	with engine.connect() as connection:
		example_sel = reservation.select()
		example_sel_result = connection.execute(example_sel)
		for row in example_sel_result:
		# If book is reserved - cannot withdraw
			if row[0] == anum_entry.get():
				if row[1] == None:
					return True
				else:
					return False
		return True

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
				return True
			else:
				continue
		return False
			

def actual_withdraw():
	if not_on_loan() and not_reserved() and book_in_library():

		this_book = book_info()
		current_title = this_book[0]
		current_isbn = this_book[1]
		current_publisher = this_book[2]
		current_pubyear = this_book[3]
		
		toplevel = Toplevel(bookwithdraw, bg="lawn green")
		toplevel.geometry('500x550')
		l1_frame = Frame(toplevel, bg = "lawn green", width = 400, height=50)
		l1=Label(l1_frame,text="Please Confirm Details to\n Be Correct", font = "Arial 20 bold", fg="black", bg="lawn green")
		l1_frame.pack()
		l1.pack(ipadx = 20, ipady = 20)
		
		check_accessionnumber_frame = LabelFrame(toplevel, text = "Accession Number", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_accessionnumber = Label(check_accessionnumber_frame,text= anum_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
		check_accessionnumber_frame.pack(fill=X)
		check_accessionnumber.pack(ipady = 5)
		
		check_booktitle_frame = LabelFrame(toplevel, text = "Title", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_booktitle = Label(check_booktitle_frame,text= current_title, font = "Arial 12", fg="black", bg="lawn green")
		check_booktitle_frame.pack(fill=X)
		check_booktitle.pack(ipady = 5)
		
		check_memberid_frame = LabelFrame(toplevel, text = "Authors", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_memberid = Label(check_memberid_frame,text= this_authors(), font = "Arial 12", fg="black", bg="lawn green")
		check_memberid_frame.pack(fill=X)
		check_memberid.pack(ipady = 5)
		
		check_membername_frame = LabelFrame(toplevel, text = "ISBN", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_membername = Label(check_membername_frame,text=current_isbn, font = "Arial 12", fg="black", bg="lawn green")
		check_membername_frame.pack(fill=X)
		check_membername.pack(ipady = 5)
		
		check_reservedate_frame = LabelFrame(toplevel, text = "Publisher", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_reservedate = Label(check_reservedate_frame,text= current_publisher, font = "Arial 12", fg="black", bg="lawn green")
		check_reservedate_frame.pack(fill=X)
		check_reservedate.pack(ipady = 5)

		check_reservedate_frame = LabelFrame(toplevel, text = "Year", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_reservedate = Label(check_reservedate_frame,text= current_pubyear, font = "Arial 12", fg="black", bg="lawn green")
		check_reservedate_frame.pack(fill=X)
		check_reservedate.pack(ipady = 5)
		
		blank_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
		blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="lawn green", bg="lawn green")
		blank_frame.pack()
		blank.pack(ipadx = 15, ipady = 10)

		# remove book from Book
		def withdraw_book():
			engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
			metadata_object = db.MetaData()
			connection = engine.connect()
			metadata_object.reflect(bind = engine)

			connection.execute("""
			DELETE FROM Book b WHERE b.accessionNumber = (%s)""", (anum_entry.get()))

			toplevel.destroy()
			#bookwithdraw.destroy()
			

		
		button1_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
		button1 = Button(button1_frame,text="Confirm \n Withdrawal", bg = "powder blue", fg = "black", font = "Arial 10 bold", command= withdraw_book, width=15)
		button1_frame.pack(padx = 50, pady = 15, side = LEFT)
		button1.pack(ipadx = 10, ipady = 5)

		
		button2_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
		button2 = Button(button2_frame,text="Back to \n Withdrawal \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button2_frame.pack(padx = 50, pady = 15, side = LEFT)
		button2.pack(ipadx = 10, ipady = 5)


	# Book is on loan
	elif not_on_loan() == False:
		toplevel = Toplevel(bookwithdraw, bg="red")
		toplevel.geometry('300x300')
		
		errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
		errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
		errortxt_frame.pack()
		errortxt.pack(ipadx = 20, ipady = 20)
		
		errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		errcontent = Label(errcontent_frame,text="Book is currently on Loan.", font = "Arial 10", fg="yellow", bg="red")
		errcontent_frame.pack()
		errcontent.pack(ipadx = 15, ipady = 10)
		
		blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
		blank_frame.pack()
		blank.pack(ipadx = 15, ipady = 10)
		
		button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		button1 = Button(button1_frame,text="Return to \n Withdrawal \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button1_frame.pack()
		button1.pack(ipadx = 10, ipady = 5)
	

	elif not_reserved() == False:
		toplevel = Toplevel(bookwithdraw, bg="red")
		toplevel.geometry('300x300')
		
		errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
		errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
		errortxt_frame.pack()
		errortxt.pack(ipadx = 20, ipady = 20)
		
		errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		errcontent = Label(errcontent_frame,text="Book is currently Reserved.", font = "Arial 10", fg="yellow", bg="red")
		errcontent_frame.pack()
		errcontent.pack(ipadx = 15, ipady = 10)
		
		blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
		blank_frame.pack()
		blank.pack(ipadx = 15, ipady = 10)
		
		button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		button1 = Button(button1_frame,text="Return to \n Withdrawal \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button1_frame.pack()
		button1.pack(ipadx = 10, ipady = 5)
	
	else:
		toplevel = Toplevel(bookwithdraw, bg="red")
		toplevel.geometry('300x300')
		
		errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
		errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
		errortxt_frame.pack()
		errortxt.pack(ipadx = 20, ipady = 20)
		
		errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		errcontent = Label(errcontent_frame,text="Book does not exist in System.", font = "Arial 10", fg="yellow", bg="red")
		errcontent_frame.pack()
		errcontent.pack(ipadx = 15, ipady = 10)
		
		blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
		blank_frame.pack()
		blank.pack(ipadx = 15, ipady = 10)
		
		button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		button1 = Button(button1_frame,text="Return to \n Withdrawal \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button1_frame.pack()
		button1.pack(ipadx = 10, ipady = 5)
			


# delete Book button
delete_frame_boarder = Frame(bookwithdraw, bg = "gold")
delete_frame = Frame(delete_frame_boarder, bg = "turquoise", width = 100)
delete_button = Button(delete_frame, text = "Withdraw Book", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = actual_withdraw)

delete_frame_boarder.place(x = 350, y = 550)
delete_frame.pack(padx = 5, pady = 5)
delete_button.pack(ipadx = 35, ipady = 23)

bookwithdraw.mainloop()
