from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import os

main_books = Tk()
main_books.title("Books Main Page")
main_books.configure(background = "white")
main_books.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(main_books, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "powder blue", width = 400)
header = Label(header_frame, text = "Select one of the Options below:", bg = "powder blue", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Picture
books_canvas = Canvas(main_books, width = 500, height = 460)
books_canvas.place(x = 80, y = 140)
books_photo = Image.open('books.jpg').resize((500, 460))
books_photo = ImageTk.PhotoImage(books_photo)
books_canvas.create_image(0, 0, anchor = NW, image = books_photo)

Label(text = "Books", bg = "black", fg = "white", font = "Arial 25").place(x = 290, y = 500)

# Acquisition Button
def acquisition():
	main_books.destroy()
	os.system('python bookAcquisition.py')

acquisition_frame = Frame(bg = "DeepSkyBlue3", width = 300, height = 300)
acquisition_button = Button(acquisition_frame, text = "4. Acquisition", bg = "DeepSkyBlue3", fg = "white", font = ("Arial 18 bold"), command = acquisition)

acquisition_frame.place(x = 620, y = 200)
acquisition_button.pack(ipadx = 180, ipady = 60)

# Withdrawal Button
def withdraw():
	main_books.destroy()
	os.system('python bookWithdraw.py')

withdrawal_frame = Frame(bg = "blue", width = 300, height = 300)
withdrawal_button = Button(withdrawal_frame, text = "5. Withdrawal", bg = "blue", fg = "white", font = ("Arial 18 bold"), command = withdraw)

withdrawal_frame.place(x = 620, y = 400)
withdrawal_button.pack(ipadx = 183, ipady = 60)

# Return to Main Menu Button
def backtomain():
	main_books.destroy()
	os.system('python root.py')

bottom_frame_boarder = Frame(main_books, bg = "deep sky blue")
bottom_frame = Frame(bottom_frame_boarder, bg = "powder blue", width = 400)
bottom_button = Button(bottom_frame, text = "Back to Main Menu", bg = "powder blue", fg = "black", font = "Arial 18 bold", command = backtomain)

bottom_frame_boarder.pack(padx = 10, pady = 30, side = BOTTOM)
bottom_frame.pack(padx = 5, pady = 5)
bottom_button.pack(ipadx = 340, ipady = 1)

main_books.mainloop()
