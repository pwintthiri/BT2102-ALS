from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import os

main_reservation = Tk()
main_reservation.title("Reservation Main Page")
main_reservation.configure(background = "white")
main_reservation.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(main_reservation, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "powder blue", width = 400)
header = Label(header_frame, text = "Select one of the Options below:", bg = "powder blue", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Picture
reservation_canvas = Canvas(main_reservation, width = 500, height = 460)
reservation_canvas.place(x = 80, y = 140)
reservation_photo = Image.open('reservation.jpg').resize((500, 460))
reservation_photo = ImageTk.PhotoImage(reservation_photo)
reservation_canvas.create_image(0, 0, anchor = NW, image = reservation_photo)

Label(text = "Reservations", bg = "black", fg = "white", font = "Arial 25").place(x = 250, y = 500)

# Reserve Book Button
def reserve():
	main_reservation.destroy()
	os.system('python bookReservation.py')

reservebook_frame = Frame(bg = "DeepSkyBlue3", width = 300, height = 300)
reservebook_button = Button(reservebook_frame, text = "8. Reserve a Book", bg = "DeepSkyBlue3", fg = "white", font = ("Arial 18 bold"), command = reserve)

reservebook_frame.place(x = 620, y = 200)
reservebook_button.pack(ipadx = 160, ipady = 60)

# Cancel Reservation Button
def cancelreserve():
	main_reservation.destroy()
	os.system('python cancelReservation.py')

cancelbook_frame = Frame(bg = "blue", width = 300, height = 300)
cancelbook_button = Button(cancelbook_frame, text = "9. Cancel Reservation", bg = "blue", fg = "white", font = ("Arial 18 bold"), command = cancelreserve)

cancelbook_frame.place(x = 620, y = 400)
cancelbook_button.pack(ipadx = 140, ipady = 60)

# Return to Main Menu Button
def backtomain():
	main_reservation.destroy()
	os.system('python root.py')

bottom_frame_boarder = Frame(main_reservation, bg = "deep sky blue")
bottom_frame = Frame(bottom_frame_boarder, bg = "powder blue", width = 400)
bottom_button = Button(bottom_frame, text = "Back to Main Menu", bg = "powder blue", fg = "black", font = "Arial 18 bold", command = backtomain)

bottom_frame_boarder.pack(padx = 10, pady = 30, side = BOTTOM)
bottom_frame.pack(padx = 5, pady = 5)
bottom_button.pack(ipadx = 340, ipady = 1)

main_reservation.mainloop()
