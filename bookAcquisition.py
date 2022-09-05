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


book_acq = Tk()
book_acq.title("Book Acquisition")
book_acq.configure(background = "white")
book_acq.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(book_acq, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "turquoise", width = 400)
header = Label(header_frame, text = "For New Book Acquisition, Please Enter Required Information Below:", bg = "turquoise", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 30, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 100, ipady = 20)

# Enter Accession Number
anum_frame = Frame(bg = "DeepSkyBlue3", width = 200, height = 200)
anum = Label(anum_frame, text = "Acession Number:", bg = "DeepSkyBlue3", fg = "white", font = "Arial 18")

anum_frame.place(x = 160, y = 100)
anum.pack(ipadx = 50, ipady = 18)

anum_entry = Entry(book_acq, width = 58, font = "Arial 15", highlightthickness = 4)
anum_entry.insert(0, "Enter Book Accession Number")
anum_entry.place(x = 470, y = 120)

# Enter Title
title_frame = Frame(bg = "DeepSkyBlue2", width = 200, height = 200)
title = Label(title_frame, text = "Title:", bg = "DeepSkyBlue2", fg = "white", font = "Arial 18")

title_frame.place(x = 160, y = 175)
title.pack(ipadx = 122, ipady = 18)

title_entry = Entry(book_acq, width = 58, font = "Arial 15", highlightthickness = 4)
title_entry.insert(0, "Enter Book Title")
title_entry.place(x = 470, y = 195)

# Enter Author
author_frame = Frame(bg = "SteelBlue1", width = 200, height = 200)
author = Label(author_frame, text = "Author:", bg = "SteelBlue1", fg = "white", font = "Arial 18")

author_frame.place(x = 160, y = 250)
author.pack(ipadx = 109, ipady = 18)

author_entry = Entry(book_acq, width = 58, font = "Arial 15", highlightthickness = 4)
author_entry.insert(0, "Author(s) Name")
author_entry.place(x = 470, y = 270)

# Enter ISBN
isbn_frame = Frame(bg = "SkyBlue2", width = 200, height = 200)
isbn = Label(isbn_frame, text = "ISBN:", bg = "SkyBlue2", fg = "white", font = "Arial 18")

isbn_frame.place(x = 160, y = 325)
isbn.pack(ipadx = 117, ipady = 18)

isbn_entry = Entry(book_acq, width = 58, font = "Arial 15", highlightthickness = 4)
isbn_entry.insert(0, "ISBN Number")
isbn_entry.place(x = 470, y = 345)

# Enter Publisher
publisher_frame = Frame(bg = "SkyBlue1", width = 200, height = 200)
publisher = Label(publisher_frame, text = "Publisher:", bg = "SkyBlue1", fg = "white", font = "Arial 18")

publisher_frame.place(x = 160, y = 400)
publisher.pack(ipadx = 93, ipady = 18)

publisher_entry = Entry(book_acq, width = 58, font = "Arial 15", highlightthickness = 4)
publisher_entry.insert(0, "Random House, Penguin, Cengage, Springer, etc.")
publisher_entry.place(x = 470, y = 420)

# Enter Publication
publication_frame = Frame(bg = "SkyBlue1", width = 200, height = 200)
publication = Label(publication_frame, text = "Publication:", bg = "SkyBlue1", fg = "white", font = "Arial 18")

publication_frame.place(x = 160, y = 475)
publication.pack(ipadx = 85, ipady = 18)

publication_entry = Entry(book_acq, width = 58, font = "Arial 15", highlightthickness = 4)
publication_entry.insert(0, "Edition Year")
publication_entry.place(x = 470, y = 495)

# back to main menu button
def backtomain():
	book_acq.destroy()
	os.system('python mainBooks.py')

btmm_frame_boarder = Frame(book_acq, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to Books Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 550)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 10, ipady = 23)

#create Book table 
with engine.connect() as connection:
    r1 = connection.execute(db.text("select * from Book"))
with engine.connect() as connection:
    book_sel = book.select()
    book_sel_result = connection.execute(book_sel)

# check if entries are valid
def anum_uniqueness():
        if len(anum_entry.get()) == 0:
            return False
        for rows in book_sel_result:
            if rows[0] == anum_entry.get():
                return False
            elif len(anum_entry.get())> 5:
                return False
        return True

def title_length():
    if len(title_entry.get()) ==0 or len(title_entry.get())> 65:
        return False
    else:
        return True

def isbn_length():
    if len(isbn_entry.get()) == 0 or len(isbn_entry.get()) > 15:
        return False
    else:
        return True
        
def publisher_length():
    if len(publisher_entry.get()) ==0 or len(publisher_entry.get()) > 40:
        return False
    else:
        return True

def pubyear_length():
    if len(publication_entry.get()) == 0 or len(publication_entry.get()) >5 or publication_entry.get().isnumeric() == False:
        return False
    else:
        return True

def author_names():
        count = 0
        for i in author_entry.get():
                if i ==",":
                        count = count +1
        return count

def actual_author():
        if author_names() == 0:
                return [author_entry.get()]
        else:
                author_list = []
                count = 0
                for i in range(len(author_entry.get())):
                        if author_entry.get()[i] == ',':
                                author_list.append(author_entry.get()[count:i])
                                count = i+1
                        elif i==len(author_entry.get()) - 1:
                            author_list.append(author_entry.get()[count:])
                print(author_list)
                return author_list

def actual_book_insertion():
    if anum_uniqueness() and title_length() and isbn_length() and publisher_length() and pubyear_length():
        engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
        metadata_object = db.MetaData()
        connection = engine.connect()
        metadata_object.reflect(bind = engine)

        connection.execute( """
		INSERT INTO Book VALUES (%s,%s,%s,%s,%s, NULL, NULL, NULL, NULL)
        """, (anum_entry.get(), title_entry.get(), isbn_entry.get(), publisher_entry.get(), publication_entry.get()))
      

        # Green window
        toplevel = Toplevel(book_acq, bg="lawn green")
        toplevel.geometry('300x300')
        
        successtxt_frame = Frame(toplevel, bg = "lawn green", width = 300, height=50)
        successtxt = Label(successtxt_frame,text="Success!", font = "Arial 40", fg="black", bg="lawn green")
        successtxt_frame.pack()
        successtxt.pack(ipadx = 20, ipady = 20)
        
        successmes_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
        successmes = Label(successmes_frame,text="New Book added in Library.", font = "Arial 10", fg="black", bg="lawn green")
        successmes_frame.pack()
        successmes.pack(ipadx = 15, ipady = 10)
        
        blank_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="lawn green", bg="lawn green")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)
        
        button2_frame = Frame(toplevel, bg = "lawn green", width = 300, height=20)
        button2 = Button(button2_frame,text="Back to \n Acquisition \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        button2_frame.pack()
        button2.pack(ipadx = 10, ipady = 5)

        author_list = actual_author()
        for i in range(len(author_list)):
            connection.execute( """
		INSERT INTO Authors VALUES (%s,%s)
                """, (author_list[i],anum_entry.get()))


        
    else:
        toplevel = Toplevel(book_acq, bg="red")
        toplevel.geometry('300x300')
        
        errortxt_frame = Frame(toplevel, bg = "red", width = 300, height=50)
        errortxt = Label(errortxt_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
        errortxt_frame.pack()
        errortxt.pack(ipadx = 20, ipady = 20)
        
        errcontent_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        errcontent = Label(errcontent_frame,text="Book already added; \n Duplicate, Missing or \n  Incomplete fields.", font = "Arial 10", fg="yellow", bg="red")
        errcontent_frame.pack()
        errcontent.pack(ipadx = 15, ipady = 10)
        
        blank_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        blank = Label(blank_frame,text="                         ", font = "Arial 10", fg="red", bg="red")
        blank_frame.pack()
        blank.pack(ipadx = 15, ipady = 10)
        
        button1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        button1 = Button(button1_frame,text="Back to \n Acquisition \n Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        button1_frame.pack()
        button1.pack(ipadx = 10, ipady = 5)


# acquire book button
create_frame_boarder = Frame(book_acq, bg = "gold")
create_frame = Frame(create_frame_boarder, bg = "turquoise", width = 100)
create_button = Button(create_frame, text = "Add New Book", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = actual_book_insertion)
create_frame_boarder.place(x = 350, y = 550)
create_frame.pack(padx = 5, pady = 5)
create_button.pack(ipadx = 35, ipady = 23)

book_acq.mainloop()
