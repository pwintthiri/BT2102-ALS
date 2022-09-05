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

#####939am
rreport = Tk()
rreport.title("Books on Loan Report")
rreport.configure(background = "OliveDrab2")
rreport.geometry('900x500')

myTitle = Label(rreport, text = "Books on Reservation Report", background = "OliveDrab2", fg = "black", font = "Arial 20 bold")
myTitle.pack(pady = 50, side = TOP)

tableHead_AccessionNumber = Entry(rreport, width = 10, fg= "black")
tableHead_AccessionNumber.place(x = 40, y = 100)
tableHead_AccessionNumber.insert(0,"AccessionNo.")
tableHead_AccessionNumber.config(state="disabled")


tableHead_Title = Entry(rreport, width = 32, fg= "black")
tableHead_Title.place(x = 143, y = 100)
tableHead_Title.insert(10,"Title")
tableHead_Title.config(state="disabled")

tableHead_MembershipID = Entry(rreport, width = 14, fg= "black")
tableHead_MembershipID.place(x = 444, y = 100)
tableHead_MembershipID.insert(0,"MembershipID")
tableHead_MembershipID.config(state="disabled")

tableHead_Name = Entry(rreport, width = 20, fg= "black")
tableHead_Name.place(x =583, y = 100)
tableHead_Name.insert(0,"Name")
tableHead_Name.config(state="disabled")

engine = engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
metadata_object = db.MetaData()
connection = engine.connect()
metadata_object.reflect(bind = engine)


reservation_report = connection.execute("""SELECT  r.accessionNumber, b.title, r.membershipID, m.memberName
FROM Members m, Book b, Reservation r
WHERE r.membershipID = m.membershipID AND b.accessionNumber = r.accessionNumber;""")

i = 0
for reservation in reservation_report:
        for j in range(4):
                if j == 0:
                        e = Entry(rreport, width = 10, fg= "black")
                        e.place(x = 40, y = (i+1.3)*100)
                        e.insert(0,reservation[j])
                        e.config(state ="disabled")
                elif j == 1:
                        e = Entry(rreport, width = 32, fg= "black")
                        e.place(x = 143, y = (i+1.3)*100)
                        e.insert(0,reservation[j])
                        
                        e.config(state ="disabled")
                elif j == 2:
                        e = Entry(rreport, width = 14, fg= "black")
                        e.place(x = 444, y = (i+1.3)*100)
                        e.insert(0,reservation[j])
                        e.config(state ="disabled")
                elif j == 3:
                        e = Entry(rreport, width = 20, fg= "black")
                        e.place(x = 583, y = (i+1.3)*100)
                        e.insert(0,reservation[j])
                        e.config(state ="disabled")

        i = i+0.3
        


# back to reports menu button
def backtomain():
	rreport.destroy()
	os.system('python mainReports.py')

create_frame_boarder = Frame(rreport, bg = "gold")
create_frame = Frame(create_frame_boarder, bg = "turquoise", width = 100)
create_button = Button(create_frame, text = "Back to Reports Menu", bg = "turquoise", fg = "black", font = "Arial 10 bold", command = backtomain)
create_frame_boarder.pack(pady = 50, side = BOTTOM)
create_frame.pack(padx = 5, pady = 5)
create_button.pack(ipadx = 25, ipady = 2)

rreport.mainloop()
