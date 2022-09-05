from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import os

main_membership = Tk()
main_membership.title("Membership Main Page")
main_membership.configure(background = "white")
main_membership.geometry('1280x720')

# Top Heading
header_frame_boarder = Frame(main_membership, bg = "deep sky blue")
header_frame = Frame(header_frame_boarder, bg = "powder blue", width = 400)
header = Label(header_frame, text = "Select one of the Options below:", bg = "powder blue", fg = "black", font = "Arial 18 bold")

header_frame_boarder.pack(padx = 10, pady = 10)
header_frame.pack(padx = 5, pady = 5)
header.pack(ipadx = 270, ipady = 20)

# Picture
membership_canvas = Canvas(main_membership, width = 500, height = 460)
membership_canvas.place(x = 80, y = 140)
membership_photo = Image.open('membership.jpg').resize((500, 460))
membership_photo = ImageTk.PhotoImage(membership_photo)
membership_canvas.create_image(0, 0, anchor = NW, image = membership_photo)

Label(text = "Membership", bg = "black", fg = "white", font = "Arial 25").place(x = 250, y = 500)

# Create Member Button
def createmembership():
	main_membership.destroy()
	os.system('python createMember.py')

creation_frame = Frame(bg = "DeepSkyBlue3", width = 300, height = 300)
creation_button = Button(creation_frame, text = "1. Creation", bg = "DeepSkyBlue3", fg = "white", font = ("Arial 18 bold"), command = createmembership)

creation_frame.place(x = 620, y = 150)
creation_button.pack(ipadx = 200, ipady = 40)

# Deletion Button
def deletemembership():
	main_membership.destroy()
	os.system('python deleteMember.py')

deletion_frame = Frame(bg = "blue", width = 300, height = 300)
deletion_button = Button(deletion_frame, text = "2. Deletion", bg = "blue", fg = "white", font = ("Arial 18 bold"), command = deletemembership)

deletion_frame.place(x = 620, y = 300)
deletion_button.pack(ipadx = 202, ipady = 40)

# Update Button
def updatemembership():
	main_membership.destroy()
	import updateMember

update_frame = Frame(bg = "SlateBlue3", width = 300, height = 300)
update_button = Button(update_frame, text = "3. Update", bg = "SlateBlue3", fg = "white", font = ("Arial 18 bold"), command = updatemembership)

update_frame.place(x = 620, y = 450)
update_button.pack(ipadx = 210, ipady = 40)

# Return to Main Menu Button
def backtomain():
	main_membership.destroy()
	os.system('python root.py')

bottom_frame_boarder = Frame(main_membership, bg = "deep sky blue")
bottom_frame = Frame(bottom_frame_boarder, bg = "powder blue", width = 400)
bottom_button = Button(bottom_frame, text = "Back to Main Menu", bg = "powder blue", fg = "black", font = "Arial 18 bold", command = backtomain)

bottom_frame_boarder.pack(padx = 10, pady = 30, side = BOTTOM)
bottom_frame.pack(padx = 5, pady = 5)
bottom_button.pack(ipadx = 340, ipady = 1)

main_membership.mainloop()
