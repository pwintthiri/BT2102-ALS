from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import os

main_loans = Tk()
main_loans.title("Books Main Page")
main_loans.configure(background = "white")
main_loans.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(main_loans, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "powder blue", width = 400)
header = Label(header_frame, text = "Select one of the Options below:", bg = "powder blue", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Picture
loans_canvas = Canvas(main_loans, width = 500, height = 440)
loans_canvas.place(x = 80, y = 140)
loans_photo = Image.open('loans.jpg').resize((500, 440))
loans_photo = ImageTk.PhotoImage(loans_photo)
loans_canvas.create_image(0, 0, anchor = NW, image = loans_photo)

Label(text = "Loans", bg = "black", fg = "white", font = "Arial 25").place(x = 280, y = 500)

# Borrow Button
def borrow():
	main_loans.destroy()
	os.system('python bookBorrow.py')

borrow_frame = Frame(bg = "DeepSkyBlue3", width = 300, height = 300)
borrow_button = Button(borrow_frame, text = "6. Borrow", bg = "DeepSkyBlue3", fg = "white", font = ("Arial 18 bold"), command = borrow)

borrow_frame.place(x = 620, y = 200)
borrow_button.pack(ipadx = 210, ipady = 60)

# Return Button
def returnbook():
	main_loans.destroy()
	os.system('python returnLoan.py')

return_frame = Frame(bg = "blue", width = 300, height = 300)
return_button = Button(return_frame, text = "7. Return", bg = "blue", fg = "white", font = ("Arial 18 bold"), command = returnbook)

return_frame.place(x = 620, y = 400)
return_button.pack(ipadx = 213, ipady = 60)

# Return to Main Menu Button
def backtomain():
	main_loans.destroy()
	os.system('python root.py')

bottom_frame_boarder = Frame(main_loans, bg = "deep sky blue")
bottom_frame = Frame(bottom_frame_boarder, bg = "powder blue", width = 400)
bottom_button = Button(bottom_frame, text = "Back to Main Menu", bg = "powder blue", fg = "black", font = "Arial 18 bold", command = backtomain)

bottom_frame_boarder.pack(padx = 10, pady = 30, side = BOTTOM)
bottom_frame.pack(padx = 5, pady = 5)
bottom_button.pack(ipadx = 340, ipady = 1)

main_loans.mainloop()
