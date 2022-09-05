from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Column
import pymysql
import pymysql.cursors
import tkinter.font as tkFont
import pandas as pd
import os

booksearch = Tk()
booksearch.title("Book Search")
booksearch.configure(background = "white")
booksearch.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(booksearch, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "turquoise", width = 400)
header = Label(header_frame, text = "Search based on one of the categories below:", bg = "turquoise", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 30, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 100, ipady = 20)

# Enter Title
title_frame = Frame(bg = "DeepSkyBlue3", width = 200, height = 200)
title = Label(title_frame, text = "Title:", bg = "DeepSkyBlue3", fg = "white", font = "Arial 18")

title_frame.place(x = 160, y = 140)
title.pack(ipadx = 122, ipady = 18)

title_entry = Entry(booksearch, width = 58, font = "Arial 15", highlightthickness = 4)
title_entry.insert(0, "")
title_entry.place(x = 470, y = 155)

# Enter Author
author_frame = Frame(bg = "DeepSkyBlue2", width = 200, height = 200)
author = Label(author_frame, text = "Author:", bg = "DeepSkyBlue2", fg = "white", font = "Arial 18")

author_frame.place(x = 160, y = 215)
author.pack(ipadx = 109, ipady = 18)

author_entry = Entry(booksearch, width = 58, font = "Arial 15", highlightthickness = 4)
author_entry.insert(0, "")
author_entry.place(x = 470, y = 230)

# Enter ISBN
isbn_frame = Frame(bg = "SkyBlue2", width = 200, height = 200)
isbn = Label(isbn_frame, text = "ISBN:", bg = "SkyBlue2", fg = "white", font = "Arial 18")

isbn_frame.place(x = 160, y = 290)
isbn.pack(ipadx = 117, ipady = 18)

isbn_entry = Entry(booksearch, width = 58, font = "Arial 15", highlightthickness = 4)
isbn_entry.insert(0, "")
isbn_entry.place(x = 470, y = 305)

# Enter Publisher
publisher_frame = Frame(bg = "SkyBlue1", width = 200, height = 200)
publisher = Label(publisher_frame, text = "Publisher:", bg = "SkyBlue1", fg = "white", font = "Arial 18")

publisher_frame.place(x = 160, y = 365)
publisher.pack(ipadx = 93, ipady = 18)

publisher_entry = Entry(booksearch, width = 58, font = "Arial 15", highlightthickness = 4)
publisher_entry.insert(0, "")
publisher_entry.place(x = 470, y = 380)

# Enter Publication
publication_frame = Frame(bg = "SkyBlue1", width = 200, height = 200)
publication = Label(publication_frame, text = "Publication Year:", bg = "SkyBlue1", fg = "white", font = "Arial 18")

publication_frame.place(x = 160, y = 440)
publication.pack(ipadx = 57, ipady = 18)

publication_entry = Entry(booksearch, width = 58, font = "Arial 15", highlightthickness = 4)
publication_entry.insert(0, "")
publication_entry.place(x = 470, y = 455)

# back to main menu button
def backtomain():
	booksearch.destroy()
	os.system('python mainReports.py')

btmm_frame_boarder = Frame(booksearch, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to Reports Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 550)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 10, ipady = 23)

def check_one_category():
    count = 0
    if title_entry.get() !="":
        count += 1
    if author_entry.get() != "":
        count += 1
    if isbn_entry.get() != "":
        count += 1
    if publisher_entry.get() != "":
        count += 1
    if publication_entry.get() != "":
        count += 1

    return count
def length_checker(x):
    input = x.split()
    if len(input) != 1:
        return False
    else:
        return True
def check_one_word():
    if check_one_category() == 1:
        if title_entry.get() != "":
            return length_checker(title_entry.get())
        elif author_entry.get() != "":
            return length_checker(author_entry.get())
        elif isbn_entry.get() != "":
            return length_checker(isbn_entry.get())
        elif publisher_entry.get() != "":
            return length_checker(publisher_entry.get())
        elif publication_entry.get() != "":
            return length_checker(publication_entry.get())

def actual_search():
    
    
    engine = engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
    metadata_object = db.MetaData()
    connection = engine.connect()
    metadata_object.reflect(bind = engine)
    if check_one_word() == True and check_one_category() == 1:
        toplevel = Toplevel(booksearch, bg="lawn green")
        toplevel.geometry('1100x600')
        l1_frame = Frame(toplevel, bg = "lawn green", width = 400, height=50)
        l1=Label(l1_frame,text="Book Search Result", font = "Arial 20 bold", fg="black", bg="lawn green")
        l1_frame.pack()
        l1.pack(ipadx = 20, ipady = 20)
        if title_entry.get() !="":
            output = connection.execute("""
            SELECT b.accessionNumber, b.title, GROUP_CONCAT(a.authorName SEPARATOR ", "), b.isbn, b.publisher, b.publicationYear
            FROM Book b, Authors a
            WHERE b.title LIKE %s AND a.accessionNumber = b.accessionNumber
            GROUP BY b.accessionNumber;
            """, ('%' + title_entry.get() + '%'))
            
        if author_entry.get() !="":
            output = connection.execute("""
            SELECT b.accessionNumber, b.title, GROUP_CONCAT(a.authorName SEPARATOR ", "), b.isbn, b.publisher, b.publicationYear
            FROM Book b, Authors a
            WHERE a.authorName LIKE %s AND a.accessionNumber = b.accessionNumber
            GROUP BY b.accessionNumber;
            """, ('%' + author_entry.get() + '%'))

        if isbn_entry.get() !="":
            output = connection.execute("""
            SELECT b.accessionNumber, b.title, GROUP_CONCAT(a.authorName SEPARATOR ", "), b.isbn, b.publisher, b.publicationYear
            FROM Book b, Authors a
            WHERE b.isbn LIKE %s AND a.accessionNumber = b.accessionNumber
            GROUP BY b.accessionNumber;
            """, ('%' + isbn_entry.get() + '%'))

        if publisher_entry.get() !="":
            output = connection.execute("""
            SELECT b.accessionNumber, b.title, GROUP_CONCAT(a.authorName SEPARATOR ", "), b.isbn, b.publisher, b.publicationYear
            FROM Book b, Authors a
            WHERE b.publisher LIKE %s AND a.accessionNumber = b.accessionNumber
            GROUP BY b.accessionNumber;
            """, ('%' + publisher_entry.get() + '%'))

        if publication_entry.get() !="":
            output = connection.execute("""
            SELECT b.accessionNumber, b.title, GROUP_CONCAT(a.authorName SEPARATOR ", "), b.isbn, b.publisher, b.publicationYear
            FROM Book b, Authors a
            WHERE b.publicationYear LIKE %s AND a.accessionNumber = b.accessionNumber
            GROUP BY b.accessionNumber;
            """, ('%' + publication_entry.get() + '%'))
            
        tableHead_AccessionNumber = Entry(toplevel, width = 9, fg= "black")
        tableHead_AccessionNumber.place(x = 0, y = 100)
        tableHead_AccessionNumber.insert(0,"AccessionNo")
        tableHead_AccessionNumber.config(state="disabled")


        tableHead_Title = Entry(toplevel, width = 36, fg= "black")
        tableHead_Title.place(x = 93, y = 100)
        tableHead_Title.insert(10,"Title")
        tableHead_Title.config(state="disabled")

        tableHead_Authors = Entry(toplevel, width = 34, fg= "black")
        tableHead_Authors.place(x = 400, y = 100)
        tableHead_Authors.insert(0,"Authors")
        tableHead_Authors.config(state="disabled")

        tableHead_ISBN = Entry(toplevel, width = 14, fg= "black")
        tableHead_ISBN.place(x = 700, y = 100)
        tableHead_ISBN.insert(0,"ISBN")
        tableHead_ISBN.config(state="disabled")

        tableHead_Publisher = Entry(toplevel, width = 28, fg= "black")
        tableHead_Publisher.place(x = 830, y = 100)
        tableHead_Publisher.insert(0,"Publisher")
        tableHead_Publisher.config(state="disabled")

        tableHead_Year = Entry(toplevel, width = 4, fg= "black")
        tableHead_Year.place(x = 1050, y = 100)
        tableHead_Year.insert(0,"Year")
        tableHead_Year.config(state="disabled")

        leftbutton_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        leftbutton = Button(leftbutton_frame,text="Back To\nSearch Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", width=15, command = toplevel.destroy)
        leftbutton_frame.place(x = 450, y = 450)
        leftbutton.pack(ipadx = 10, ipady = 5)

        i = 0
        for row in output:
            print(row)
            for j in range(6):
                if j == 0:
                        e = Entry(toplevel, width = 9, fg= "black")
                        e.place(x = 0, y = (i+1.3)*100)
                        e.insert(0,row[j])
                        e.config(state ="disabled")
                elif j == 1:
                        e = Entry(toplevel, width = 36, fg= "black")
                        e.place(x = 93, y = (i+1.3)*100)
                        e.insert(0,row[j])
                        
                        e.config(state ="disabled")
                elif j == 2:
                        e = Entry(toplevel, width = 34, fg= "black")
                        e.place(x =400, y = (i+1.3)*100)
                        e.insert(0,row[j])
                        e.config(state ="disabled")
                elif j == 3:
                        e = Entry(toplevel, width = 14, fg= "black")
                        e.place(x = 700, y = (i+1.3)*100)
                        e.insert(0,row[j])
                        e.config(state ="disabled")
                elif j == 4:
                        e = Entry(toplevel, width = 28, fg= "black")
                        e.place(x = 830, y = (i+1.3)*100)
                        e.insert(0,row[j])
                        e.config(state ="disabled")
                elif j == 5:
                        e = Entry(toplevel, width = 4, fg= "black")
                        e.place(x =1050, y = (i+1.3)*100)
                        e.insert(0,row[j])
                        e.config(state ="disabled")
            i = i+0.3
    else:
        toplevel = Toplevel(booksearch, bg="red")
        toplevel.geometry('300x300')
        l1_frame = Frame(toplevel, bg = "red", width = 300, height=50)
        l1=Label(l1_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
        l1_frame.pack()
        l1.pack(ipadx = 20, ipady = 20)
        l2_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        l2=Label(l2_frame,text="Only ONE word in \nONE category allowed! ", font = "Arial 10", fg="yellow", bg="red")
        l2_frame.pack()
        l2.pack(ipadx = 15, ipady = 10)
        l3_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        l3=Label(l3_frame,text="                         ", font = "Arial 10", fg="yellow", bg="red")
        l3_frame.pack()
        l3.pack(ipadx = 15, ipady = 10)
        b1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
        b1=Button(b1_frame,text="Back to \n Search Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
        b1_frame.pack()
        b1.pack(ipadx = 10, ipady = 5)



# search book 
create_frame_boarder = Frame(booksearch, bg = "gold")
create_frame = Frame(create_frame_boarder, bg = "turquoise", width = 100)
create_button = Button(create_frame, text = "Search Book", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = actual_search)
create_frame_boarder.place(x = 350, y = 550)
create_frame.pack(padx = 5, pady = 5)
create_button.pack(ipadx = 55, ipady = 23)

booksearch.mainloop()
