from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
from datetime import date
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Column
import pymysql
import pymysql.cursors
import tkinter.font as tkFont
import pandas as pd
import os 
######954am
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
temporary = db.Table('Temporary',metadata_object, autoload=True, autoload_with=engine)


onloan = Tk()
onloan.title("Books on Loan to Member Report")
onloan.configure(background = "white")
onloan.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(onloan, bg = "deep sky blue")
header_frame = Frame(onloan, bg = "turquoise", width = 400)
header = Label(header_frame, text = "Books on Loan to Member", bg = "turquoise", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Enter Memb ID
membid_frame = Frame(bg = "magenta3", width = 200, height = 200)
membid = Label(membid_frame, text = "Membership ID:", bg = "magenta3", fg = "white", font = "Arial 18")

membid_frame.place(x = 160, y = 235)
membid.pack(ipadx = 50, ipady = 18)

membid_entry = Entry(onloan, width = 58, font = "Arial 15", highlightthickness = 4)
membid_entry.insert(0, "Enter Membership ID")
membid_entry.place(x = 470, y = 250)



# back to main menu button
def backtomain():
	onloan.destroy()
	os.system('python mainReports.py')

btmm_frame_boarder = Frame(onloan, bg = "gold")
btmm_frame = Frame(btmm_frame_boarder, bg = "turquoise", width = 100)
btmm_button = Button(btmm_frame, text = "Back to\nReports Menu", bg = "turquoise", fg = "black", font = "Arial 15 bold", command = backtomain)

btmm_frame_boarder.place(x = 700, y = 550)
btmm_frame.pack(padx = 5, pady = 5)
btmm_button.pack(ipadx = 25, ipady = 10)

def is_a_member():
    with engine.connect() as connection:
        member_table = connection.execute(db.text("select * from Members"))
    with engine.connect() as connection:
        member_sel = members.select()
        member_sel_result = connection.execute(member_sel)
    for row in member_sel_result:
        if row[0] == membid_entry.get():
                return True
    return False



def booksonloan1():
        if is_a_member() == False:
                toplevel = Toplevel(onloan, bg="red")
                toplevel.geometry('300x300')
                l1_frame = Frame(toplevel, bg = "red", width = 300, height=50)
                l1=Label(l1_frame,text="Error!", font = "Arial 40", fg="yellow", bg="red")
                l1_frame.pack()
                l1.pack(ipadx = 20, ipady = 20)
                l2_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                l2=Label(l2_frame,text="Member does not exist.", font = "Arial 10", fg="yellow", bg="red")
                l2_frame.pack()
                l2.pack(ipadx = 15, ipady = 10)
                l3_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                l3=Label(l3_frame,text="                         ", font = "Arial 10", fg="yellow", bg="red")
                l3_frame.pack()
                l3.pack(ipadx = 15, ipady = 10)
                b1_frame = Frame(toplevel, bg = "red", width = 300, height=20)
                b1=Button(b1_frame,text="Back to \n Book on Loan to Member Search Function", bg = "powder blue", fg = "black", font = "Arial 10 bold", command=toplevel.destroy, width=15)
                b1_frame.pack()
                b1.pack(ipadx = 10, ipady = 5)

        else:   
                engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
                metadata_object = db.MetaData()
                connection = engine.connect()
                metadata_object.reflect(bind = engine)
                connection.execute("INSERT INTO Temporary VALUES (%s)", (membid_entry.get()))
                onloan.destroy()
                os.system('python onloanpopup.py')


# search member button
search_frame_boarder = Frame(onloan, bg = "gold")
search_frame = Frame(search_frame_boarder, bg = "turquoise", width = 100)
search_button = Button(search_frame, text = "Search Member", bg = "turquoise", fg = "black", font = "Arial 15 bold",command = booksonloan1)

search_frame_boarder.place(x = 350, y = 550)
search_frame.pack(padx = 5, pady = 5)
search_button.pack(ipadx = 25, ipady = 23)

onloan.mainloop()
