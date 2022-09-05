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
mfreport = Tk()
mfreport.title("Members with Fine Report")
mfreport.configure(background = "OliveDrab2")
mfreport.geometry('900x500')

myTitle = Label(mfreport, text = "Members With Outstanding Fines", background = "OliveDrab2", fg = "black", font = "Arial 20 bold")
myTitle.pack(pady = 50, side = TOP)

tableHead_MembershipID = Entry(mfreport, width = 10, fg= "black")
tableHead_MembershipID.place(x = 50, y = 100)
tableHead_MembershipID.insert(0,"Membership ID")
tableHead_MembershipID.config(state="disabled")


tableHead_Name = Entry(mfreport, width = 25, fg= "black")
tableHead_Name.place(x = 150, y = 100)
tableHead_Name.insert(10,"Name")
tableHead_Name.config(state="disabled")

tableHead_Faculty = Entry(mfreport, width = 15, fg= "black")
tableHead_Faculty.place(x = 370, y = 100)
tableHead_Faculty.insert(0,"Faculty")
tableHead_Faculty.config(state="disabled")

tableHead_Phone = Entry(mfreport, width = 12, fg= "black")
tableHead_Phone.place(x = 500, y = 100)
tableHead_Phone.insert(0,"Phone Number")
tableHead_Phone.config(state="disabled")

tableHead_Email = Entry(mfreport, width = 20, fg= "black")
tableHead_Email.place(x = 620, y = 100)
tableHead_Email.insert(0,"Email Address")
tableHead_Email.config(state="disabled")



engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
metadata_object = db.MetaData()
connection = engine.connect()
metadata_object.reflect(bind = engine)



fine_report = connection.execute("""SELECT f.membershipID, m.memberName, m.faculty, m.phoneNumber,m.emailAddress 
                FROM Fine f, Members m
                WHERE f.PaymentAmount > 0 AND m.membershipID = f.membershipID;""")
i = 0
for fine in fine_report:
        for j in range(5):
                if j == 0:
                        e = Entry(mfreport, width = 10, fg= "black")
                        e.place(x = 50, y = (i+1.3)*100)
                        e.insert(0,fine[j])
                        e.config(state ="disabled")
                elif j == 1:
                        e = Entry(mfreport, width = 25, fg= "black")
                        e.place(x =150, y = (i+1.3)*100)
                        e.insert(0,fine[j])
                        
                        e.config(state ="disabled")
                elif j == 2:
                        e = Entry(mfreport, width = 15, fg= "black")
                        e.place(x =370, y = (i+1.3)*100)
                        e.insert(0,fine[j])
                        e.config(state ="disabled")
                elif j == 3:
                        e = Entry(mfreport, width = 12, fg= "black")
                        e.place(x = 500, y = (i+1.3)*100)
                        e.insert(0,fine[j])
                        e.config(state ="disabled")
                elif j == 4:
                        e = Entry(mfreport, width = 20, fg= "black")
                        e.place(x = 620, y = (i+1.3)*100)
                        e.insert(0,fine[j])
                        e.config(state ="disabled")

        i = i+0.3
        



# back to reports menu button
def backtomain():
	mfreport.destroy()
	os.system('python mainReports.py')

create_frame_boarder = Frame(mfreport, bg = "gold")
create_frame = Frame(create_frame_boarder, bg = "turquoise", width = 100)
create_button = Button(create_frame, text = "Back to Reports Menu", bg = "turquoise", fg = "black", font = "Arial 10 bold", command = backtomain)
create_frame_boarder.pack(pady = 50, side = BOTTOM)
create_frame.pack(padx = 5, pady = 5)
create_button.pack(ipadx = 25, ipady = 2)

mfreport.mainloop()
