from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import os

main_reports = Tk()
main_reports.title("Membership Main Page")
main_reports.configure(background = "white")
main_reports.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(main_reports, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "powder blue", width = 400)
header = Label(header_frame, text = "Select one of the Options below:", bg = "powder blue", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Picture
reports_canvas = Canvas(main_reports, width = 500, height = 460)
reports_canvas.place(x = 80, y = 140)
reports_photo = Image.open('reports.jpg').resize((500, 460))
reports_photo = ImageTk.PhotoImage(reports_photo)
reports_canvas.create_image(0, 0, anchor = NW, image = reports_photo)

Label(text = "Reports", bg = "black", fg = "white", font = "Arial 25").place(x = 250, y = 500)

# Book Search Button
def searchbook():
        main_reports.destroy()
        os.system('python bookSearch.py')

booksearch_frame = Frame(bg = "DeepSkyBlue3", width = 300, height = 300)
booksearch_button = Button(booksearch_frame, text = "11. Book Search", bg = "DeepSkyBlue3", fg = "white", font = ("Arial 18 bold"), command = searchbook)

booksearch_frame.place(x = 620, y = 110)
booksearch_button.pack(ipadx = 185, ipady = 20)

# Books On Loan
def loanreport():
	main_reports.destroy()
	os.system('python loanReport.py')

booksloan_frame = Frame(bg = "blue", width = 300, height = 300)
booksloan_button = Button(booksloan_frame, text = "12. Books on Loan", bg = "blue", fg = "white", font = ("Arial 18 bold"), command = loanreport)

booksloan_frame.place(x = 620, y = 210)
booksloan_button.pack(ipadx = 171, ipady = 20)

# Books On Res Button
def resreport():
	main_reports.destroy()
	os.system('python reservationReport.py')

booksonres_frame = Frame(bg = "SlateBlue3", width = 300, height = 300)
booksonres_button = Button(booksonres_frame, text = "13. Books on Reservation", bg = "SlateBlue3", fg = "white", font = ("Arial 18 bold"), command = resreport)

booksonres_frame.place(x = 620, y = 310)
booksonres_button.pack(ipadx = 132, ipady = 20)

# Outstanding Fines
def membersfines():
	main_reports.destroy()
	os.system('python membersFines.py')

outsfines_frame = Frame(bg = "purple1", width = 300, height = 300)
outsfines_button = Button(outsfines_frame, text = "14. Outstanding Fines", bg = "purple1", fg = "white", font = ("Arial 18 bold"), command = membersfines)

outsfines_frame.place(x = 620, y = 410)
outsfines_button.pack(ipadx = 152, ipady = 20)

# Books on Loan to Member
def bookonloan():
	main_reports.destroy()
	os.system('python onloantoMember.py')

loantomemb_frame = Frame(bg = "magenta2", width = 300, height = 300)
loantomemb_button = Button(loantomemb_frame, text = "15. Books on Loan \n to Member", bg = "magenta2", fg = "white", font = ("Arial 18 bold"), command = bookonloan)

loantomemb_frame.place(x = 620, y = 510)
loantomemb_button.pack(ipadx = 167, ipady = 8)

# Return to Main Menu Button
def backtomain():
	main_reports.destroy()
	os.system('python root.py')

bottom_frame_boarder = Frame(main_reports, bg = "deep sky blue")
bottom_frame = Frame(bottom_frame_boarder, bg = "powder blue", width = 400)
bottom_button = Button(bottom_frame, text = "Back to Main Menu", bg = "powder blue", fg = "black", font = "Arial 18 bold", command = backtomain)

bottom_frame_boarder.pack(padx = 10, pady = 30, side = BOTTOM)
bottom_frame.pack(padx = 5, pady = 5)
bottom_button.pack(ipadx = 340, ipady = 1)

main_reports.mainloop()
