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
from datetime import *
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

bookborrow = Tk()
bookborrow.title("Book Borrowing")
bookborrow.configure(background = "white")
bookborrow.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(bookborrow, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "turquoise", width = 400)
header = Label(header_frame, text = "To Borrow a Book, Please Enter Information Below:", bg = "turquoise", fg = "black", font = "Arial 18 bold")
header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Acession Number
anum_frame = Frame(bg = "DeepSkyBlue3", width = 200, height = 200)
anum = Label(anum_frame, text = "Accession Number:", bg = "DeepSkyBlue3", fg = "white", font = "Arial 18")

anum_frame.place(x = 160, y = 235)
anum.pack(ipadx = 40, ipady = 18)

anum_entry = Entry(bookborrow, width = 58, font = "Arial 15", highlightthickness = 4)
anum_entry.insert(0, "Enter Accession Number")
anum_entry.place(x = 470, y = 250)

# Enter Memb ID
membid_frame = Frame(bg = "DeepSkyBlue2", width = 200, height = 200)
membid = Label(membid_frame, text = "Membership ID:", bg = "DeepSkyBlue2", fg = "white", font = "Arial 18")

membid_frame.place(x = 160, y = 350)
membid.pack(ipadx = 60, ipady = 18)

membid_entry = Entry(bookborrow, width = 58, font = "Arial 15", highlightthickness = 4)
membid_entry.insert(0, "Enter Membership ID")
membid_entry.place(x = 470, y = 370)

# back to main menu button
def backtomain():
	bookborrow.destroy()
	os.system('python mainLoans.py')

btmm_frame_boarder = Frame(bookborrow, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to Loans Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 550)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 10, ipady = 23)


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

		# If book is on Loan - cannot borrow
			if row[0] == anum_entry.get():
				if row[5] == None:
					return True
				else:	
					return False
		return 

# either not reserved or reserve by self
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
		# If book is reserved - cannot withdraw
			if row[0] == anum_entry.get():
				if row[1] == None or row[1] == membid_entry.get():
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
			if row[0] == membid_entry.get():
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
		r1 = connection.execute(db.text("select * from Book"))

	with engine.connect() as connection:
		book_sel = book.select()
		book_sel_result = connection.execute(book_sel)
		books_borrowed = []
		for row in book_sel_result:
			if row[5] == membid_entry.get():
				books_borrowed.append(row[1])
		num_borrowed = len(books_borrowed)
		if num_borrowed < 2:
			return True
		else:
			return False

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
		
def member_name():
	with engine.connect() as connection:
		members_table = connection.execute(db.text("select * from Members"))
		with engine.connect() as connection:
			members_sel = members.select()
			members_sel_result = connection.execute(members_sel)
			for row in members_sel_result:
				if row[0] == membid_entry.get():
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
			if row[0] == membid_entry.get():
				return True
			else:
				continue
		return False


def due_date():
	due_date = date.today() + timedelta(days = 14)
	return due_date

def reserved_by_self():
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
		# If book
			if row[0] == anum_entry.get():
				if row[1] == membid_entry.get():
					return True
				else:
					return False
		return True	

def borrow():
	if not_on_loan() and not_reserved() and book_in_library() and no_outstanding_fine() and not_exceeded_quota() and existing_member():

		this_book = book_info()
		current_title = this_book[0]
		borrow_date = date.today()
		membname = member_name()
		duedate = due_date()
		
		toplevel = Toplevel(bookborrow, bg="lawn green")
		toplevel.geometry('500x550')
		l1_frame = Frame(toplevel, bg = "lawn green", width = 400, height=50)
		l1=Label(l1_frame,text="Confirm Loan Details to\n Be Correct", font = "Arial 20 bold", fg="black", bg="lawn green")
		l1_frame.pack()
		l1.pack(ipadx = 20, ipady = 20)
		
		check_accessionnumber_frame = LabelFrame(toplevel, text = "Accession Number", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_accessionnumber = Label(check_accessionnumber_frame,text= anum_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
		check_accessionnumber_frame.pack(fill=X)
		check_accessionnumber.pack(ipady = 5)
		
		check_booktitle_frame = LabelFrame(toplevel, text = "Book Title", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_booktitle = Label(check_booktitle_frame,text= current_title, font = "Arial 12", fg="black", bg="lawn green")
		check_booktitle_frame.pack(fill=X)
		check_booktitle.pack(ipady = 5)
		
		check_memberid_frame = LabelFrame(toplevel, text = "Borrow Date", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_memberid = Label(check_memberid_frame,text= borrow_date, font = "Arial 12", fg="black", bg="lawn green")
		check_memberid_frame.pack(fill=X)
		check_memberid.pack(ipady = 5)
		
		check_membername_frame = LabelFrame(toplevel, text = "Membership ID", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_membername = Label(check_membername_frame,text = membid_entry.get(), font = "Arial 12", fg="black", bg="lawn green")
		check_membername_frame.pack(fill=X)
		check_membername.pack(ipady = 5)
		
		check_reservedate_frame = LabelFrame(toplevel, text = "Member Name", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_reservedate = Label(check_reservedate_frame,text= membname, font = "Arial 12", fg="black", bg="lawn green")
		check_reservedate_frame.pack(fill=X)
		check_reservedate.pack(ipady = 5)

		check_reservedate_frame = LabelFrame(toplevel, text = "Due Date", font = "Arial 12 bold", bg = "lawn green", height = 4)
		check_reservedate = Label(check_reservedate_frame,text= duedate, font = "Arial 12", fg="black", bg="lawn green")
		check_reservedate_frame.pack(fill=X)
		check_reservedate.pack(ipady = 5)
		
		blank_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
		blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="lawn green", bg="lawn green")
		blank_frame.pack()
		blank.pack(ipadx = 15, ipady = 10)

		# Loan Book
		def borrow_book():
			engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
			metadata_object = db.MetaData()
			connection = engine.connect()
			metadata_object.reflect(bind = engine)

			#add membership to Book table
			connection.execute("""
			UPDATE Book b 
			SET membershipID = (%s), borrowDate = (%s), dueDate = (%s) 
			WHERE b.accessionNumber = (%s)
			""", (membid_entry.get(), date.today(), due_date(), anum_entry.get()))

			if reserved_by_self():
				engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
				metadata_object = db.MetaData()
				connection = engine.connect()
				metadata_object.reflect(bind = engine)

				# remove reservation
				connection.execute("""
				DELETE FROM Reservation WHERE accessionNumber = (%s)
				""", (anum_entry.get()))


			toplevel.destroy()
			

		
		button1_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
		button1 = Button(button1_frame,text="Confirm \n Loan", bg = "powder blue", fg = "black", font = "Arial 10 bold", command= borrow_book, width=15)
		button1_frame.pack(padx = 50, pady = 15, side = LEFT)
		button1.pack(ipadx = 10, ipady = 5)

		
		button2_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
		button2 = Button(button2_frame,text="Back to \n Borrow \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button2_frame.pack(padx = 50, pady = 15, side = LEFT)
		button2.pack(ipadx = 10, ipady = 5)
	
	# Book is on loan
	elif not_on_loan() == False:
		toplevel = Toplevel(bookborrow, bg="red")
		toplevel.geometry('300x300')
		
		errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
		errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
		errortxt_frame.pack()
		errortxt.pack(ipadx = 20, ipady = 20)
		
		errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		# Formatting the date
		day = due_date().day
		month = due_date().month
		year = due_date().year
		final_date = "%s/%s/%s" %(day, month, year)
	

		bookloan =  "Book currently on Loan until" + "\n" + final_date

		errcontent = Label(errcontent_frame,text= bookloan, font = "Arial 10", fg="yellow", bg="red")
		errcontent_frame.pack()
		errcontent.pack(ipadx = 15, ipady = 10)
		
		blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
		blank_frame.pack()
		blank.pack(ipadx = 15, ipady = 10)
		
		button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		button1 = Button(button1_frame,text="Back to \n Borrow \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button1_frame.pack()
		button1.pack(ipadx = 10, ipady = 5)


	elif not_exceeded_quota() == False:
		toplevel = Toplevel(bookborrow, bg="red")
		toplevel.geometry('300x300')
		
		errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
		errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
		errortxt_frame.pack()
		errortxt.pack(ipadx = 20, ipady = 20)
		
		errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		errcontent = Label(errcontent_frame,text= "Member loan quota exceeded", font = "Arial 10", fg="yellow", bg="red")
		errcontent_frame.pack()
		errcontent.pack(ipadx = 15, ipady = 10)
		
		blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
		blank_frame.pack()
		blank.pack(ipadx = 15, ipady = 10)
		
		button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		button1 = Button(button1_frame,text="Back to \n Borrow \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button1_frame.pack()
		button1.pack(ipadx = 10, ipady = 5)

	elif not_reserved() == False:
		toplevel = Toplevel(bookborrow, bg="red")
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
		button1 = Button(button1_frame,text="Return to \n Borrow \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button1_frame.pack()
		button1.pack(ipadx = 10, ipady = 5)
	
	elif book_in_library() == False:
		toplevel = Toplevel(bookborrow, bg="red")
		toplevel.geometry('300x300')
		
		errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
		errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
		errortxt_frame.pack()
		errortxt.pack(ipadx = 20, ipady = 20)
		
		errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		errcontent = Label(errcontent_frame,text="Book does not exist in Library.", font = "Arial 10", fg="yellow", bg="red")
		errcontent_frame.pack()
		errcontent.pack(ipadx = 15, ipady = 10)
		
		blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
		blank_frame.pack()
		blank.pack(ipadx = 15, ipady = 10)
		
		button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		button1 = Button(button1_frame,text="Return to \n Borrow \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button1_frame.pack()
		button1.pack(ipadx = 10, ipady = 5)
		
	elif existing_member() == False:
		toplevel = Toplevel(bookborrow, bg="red")
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
		button1 = Button(button1_frame,text="Return to \n Borrow \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button1_frame.pack()
		button1.pack(ipadx = 10, ipady = 5)


	# outstanding fines
	else:
		toplevel = Toplevel(bookborrow, bg="red")
		toplevel.geometry('300x300')
		
		errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
		errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
		errortxt_frame.pack()
		errortxt.pack(ipadx = 20, ipady = 20)
		
		errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		errcontent = Label(errcontent_frame,text= "Member has outstanding fines.", font = "Arial 10", fg="yellow", bg="red")
		errcontent_frame.pack()
		errcontent.pack(ipadx = 15, ipady = 10)
		
		blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
		blank_frame.pack()
		blank.pack(ipadx = 15, ipady = 10)
		
		button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
		button1 = Button(button1_frame,text="Back to \n Borrow \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
		button1_frame.pack()
		button1.pack(ipadx = 10, ipady = 5)

	

# borrow book button
delete_frame_boarder = Frame(bookborrow, bg = "gold")
delete_frame = Frame(delete_frame_boarder, bg = "turquoise", width = 100)
delete_button = Button(delete_frame, text = "Borrow Book", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = borrow)

delete_frame_boarder.place(x = 350, y = 550)
delete_frame.pack(padx = 5, pady = 5)
delete_button.pack(ipadx = 35, ipady = 23)

bookborrow.mainloop()