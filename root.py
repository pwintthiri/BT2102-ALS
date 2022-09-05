from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("A Library System")
root.configure(background = "white")
root.geometry('1280x720')

# Main Page
myTitle = Label(root, text = "(ALS)", background = "white", fg = "black", font = "Arial 40 bold")
myTitle.place(x = 580, y = 50)

# photos
membership_photo = Image.open('membership.jpg').resize((300, 200))
membership_photo = ImageTk.PhotoImage(membership_photo)

books_photo = Image.open('books.jpg').resize((300, 200))
books_photo = ImageTk.PhotoImage(books_photo)

loans_photo = Image.open('loans.jpg').resize((300, 200))
loans_photo = ImageTk.PhotoImage(loans_photo)

reservation_photo = Image.open('reservation.jpg').resize((300, 200))
reservation_photo = ImageTk.PhotoImage(reservation_photo)

fines_photo = Image.open('fines.jpg').resize((300, 200))
fines_photo = ImageTk.PhotoImage(fines_photo)

reports_photo = Image.open('reports.jpg').resize((300, 200))
reports_photo = ImageTk.PhotoImage(reports_photo)

def openNewWindow():
	newWindow = Toplevel(root)
	newWindow.title("New Window")
	newWindow.geometry("1280x720")

def openMainMembership():
	root.destroy()
	import mainMembership

def openMainBooks():
	root.destroy()
	import mainBooks

def openMainLoans():
	root.destroy()
	import mainLoans

def openMainReservation():
	root.destroy()
	import mainReservation

def openMainFines():
	root.destroy()
	import mainFines

def openMainReports():
	root.destroy()
	import mainReports

# buttons
membership_button = Button(root, image = membership_photo, command = openMainMembership)
membership_button["border"] = "0"
membership_button.place(x = 135, y = 150)

books_button = Button(root, image = books_photo, command = openMainBooks)
books_button["border"] = "0"
books_button.place(x = 490, y = 150)

loans_button = Button(root, image = loans_photo, command = openMainLoans)
loans_button["border"] = "0"
loans_button.place(x = 845, y = 150)

reservation_button = Button(root, image = reservation_photo, command = openMainReservation)
reservation_button["border"] = "0"
reservation_button.place(x = 135, y = 450)

fines_button = Button(root, image = fines_photo, command = openMainFines)
fines_button["border"] = "0"
fines_button.place(x = 490, y = 450)

reports_button = Button(root, image = reports_photo, command = openMainReports)
reports_button["border"] = "0"
reports_button.place(x = 845, y = 450)

# button labels
Label(text = "Membership", bg = "white", fg = "black", font = "Arial 25").place(x = 200, y = 360)
Label(text = "Books", bg = "white", fg = "black", font = "Arial 25").place(x = 600, y = 360)
Label(text = "Loans", bg = "white", fg = "black", font = "Arial 25").place(x = 950, y = 360)
Label(text = "Reservations", bg = "white", fg = "black", font = "Arial 25").place(x = 200, y = 660)
Label(text = "Fines", bg = "white", fg = "black", font = "Arial 25").place(x = 600, y = 660)
Label(text = "Reports", bg = "white", fg = "black", font = "Arial 25").place(x = 940, y = 660)

root.mainloop()

