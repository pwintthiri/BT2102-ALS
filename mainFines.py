from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import os

main_fines = Tk()
main_fines.title("Books Main Page")
main_fines.configure(background = "white")
main_fines.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(main_fines, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "powder blue", width = 400)
header = Label(header_frame, text = "Select one of the Options below:", bg = "powder blue", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Picture
fines_canvas = Canvas(main_fines, width = 500, height = 460)
fines_canvas.place(x = 80, y = 140)
fines_photo = Image.open('fines.jpg').resize((500, 460))
fines_photo = ImageTk.PhotoImage(fines_photo)
fines_canvas.create_image(0, 0, anchor = NW, image = fines_photo)

Label(text = "Fines", bg = "black", fg = "white", font = "Arial 25").place(x = 280, y = 500)

# Payment Button
def pay():
	main_fines.destroy()
	os.system('python paymentFine.py')

payment_frame = Frame(bg = "DeepSkyBlue3", width = 300, height = 300)
payment_button = Button(payment_frame, text = "10. Payment", bg = "DeepSkyBlue3", fg = "white", font = ("Arial 18 bold"), command = pay)

payment_frame.place(x = 620, y = 270)
payment_button.pack(ipadx = 200, ipady = 60)

# Return to Main Menu Button
def backtomain():
	main_fines.destroy()
	os.system('python root.py')

bottom_frame_boarder = Frame(main_fines, bg = "deep sky blue")
bottom_frame = Frame(bottom_frame_boarder, bg = "powder blue", width = 400)
bottom_button = Button(bottom_frame, text = "Back to Main Menu", bg = "powder blue", fg = "black", font = "Arial 18 bold", command = backtomain)

bottom_frame_boarder.pack(padx = 10, pady = 30, side = BOTTOM)
bottom_frame.pack(padx = 5, pady = 5)
bottom_button.pack(ipadx = 340, ipady = 1)

main_fines.mainloop()
