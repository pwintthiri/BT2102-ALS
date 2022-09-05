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
#####935am
loanreport = Tk()
loanreport.title("Books on Loan Report")
loanreport.configure(background = "OliveDrab2")
loanreport.geometry('1100x500')

myTitle = Label(loanreport, text = "Books on Loan Report", background = "OliveDrab2", fg = "black", font = "Arial 20 bold")
myTitle.pack(pady = 50, side = TOP)

tableHead_AccessionNumber = Entry(loanreport, width = 9, fg= "black")
tableHead_AccessionNumber.place(x = 0, y = 100)
tableHead_AccessionNumber.insert(0,"AccessionNo")
tableHead_AccessionNumber.config(state="disabled")


tableHead_Title = Entry(loanreport, width = 34, fg= "black")
tableHead_Title.place(x = 93, y = 100)
tableHead_Title.insert(10,"Title")
tableHead_Title.config(state="disabled")

tableHead_Authors = Entry(loanreport, width = 34, fg= "black")
tableHead_Authors.place(x = 390, y = 100)
tableHead_Authors.insert(0,"Authors")
tableHead_Authors.config(state="disabled")

tableHead_ISBN = Entry(loanreport, width = 14, fg= "black")
tableHead_ISBN.place(x = 690, y = 100)
tableHead_ISBN.insert(0,"ISBN")
tableHead_ISBN.config(state="disabled")

tableHead_Publisher = Entry(loanreport, width = 30, fg= "black")
tableHead_Publisher.place(x = 820, y = 100)
tableHead_Publisher.insert(0,"Publisher")
tableHead_Publisher.config(state="disabled")


tableHead_Year = Entry(loanreport, width = 4, fg= "black")
tableHead_Year.place(x = 1050, y = 100)
tableHead_Year.insert(0,"Year")
tableHead_Year.config(state="disabled")

engine = engine = create_engine('mysql+pymysql://root:*2NgHPNg2*@127.0.0.1:3306/Library')
metadata_object = db.MetaData()
connection = engine.connect()
metadata_object.reflect(bind = engine)

loan_report = connection.execute("""SELECT b.accessionNumber, b.title, GROUP_CONCAT(a.authorName SEPARATOR ", "), b.isbn, b.publisher, b.publicationYear 
                        FROM Book b, Authors a
                        WHERE b.membershipID IS NOT NULL AND b.accessionNumber = a.accessionNumber
                        GROUP BY a.accessionNumber;""")
i = 0
for loan in loan_report:
        for j in range(6):
                if j == 0:
                        e = Entry(loanreport, width = 9, fg= "black")
                        e.place(x = 0, y = (i+1.3)*100)
                        e.insert(0,loan[j])
                        e.config(state ="disabled")
                elif j == 1:
                        e = Entry(loanreport, width = 36, fg= "black")
                        e.place(x = 93, y = (i+1.3)*100)
                        e.insert(0,loan[j])
                        
                        e.config(state ="disabled")
                elif j == 2:
                        e = Entry(loanreport, width = 34, fg= "black")
                        e.place(x =400, y = (i+1.3)*100)
                        e.insert(0,loan[j])
                        e.config(state ="disabled")
                elif j == 3:
                        e = Entry(loanreport, width = 14, fg= "black")
                        e.place(x = 700, y = (i+1.3)*100)
                        e.insert(0,loan[j])
                        e.config(state ="disabled")
                elif j == 4:
                        e = Entry(loanreport, width = 28, fg= "black")
                        e.place(x = 830, y = (i+1.3)*100)
                        e.insert(0,loan[j])
                        e.config(state ="disabled")
                elif j == 5:
                        e = Entry(loanreport, width = 4, fg= "black")
                        e.place(x =1050 , y = (i+1.3)*100)
                        e.insert(0,loan[j])
                        e.config(state ="disabled")
        i = i+0.3
        

# back to reports menu button
def backtomain():
	loanreport.destroy()
	os.system('python mainReports.py')

create_frame_boarder = Frame(loanreport, bg = "gold")
create_frame = Frame(create_frame_boarder, bg = "turquoise", width = 100)
create_button = Button(create_frame, text = "Back to Reports Menu", bg = "turquoise", fg = "black", font = "Arial 10 bold", command = backtomain)
create_frame_boarder.pack(pady = 50, side = BOTTOM)
create_frame.pack(padx = 5, pady = 5)
create_button.pack(ipadx = 25, ipady = 2)

loanreport.mainloop()
