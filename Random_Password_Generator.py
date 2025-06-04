from tkinter import *
import string
import random

mngr = Tk()
mngr.geometry('520x540')
mngr.title("Password Manager")

letters = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():

  letter_count = int(letter_entry.get())
  number_count = int(number_entry.get())
  special_character_count = int(character_entry.get())

  password = []

  for i in range(letter_count):
      password.append(random.choice(letters))

  for i in range(number_count):
      password.append(random.choice(numbers))

  for i in range(special_character_count):
      password.append(random.choice(special_characters))

  random.shuffle(password)

  print("".join(password))

  result = password
  rand_pass_entry.delete(0, 'end')
  rand_pass_entry.insert(END, str(result))

gui_header = Label(mngr, text="Random Password Generator",width=25,font=("times",20,"bold"),fg='palevioletred4')
gui_header.place(x=60,y=50)

letter_label = Label(mngr, text="# of letters ",width=20,font=("times",12,"bold"),anchor="w",bg='palevioletred3')
letter_label.place(x=40,y=130)
letter_entry = Entry(mngr,width=30,bd=2)
letter_entry.place(x=240,y=130)
number_label = Label(mngr, text="# of numbers ",width=20,font=("times",12,"bold"),anchor="w",bg='lightpink3')
number_label.place(x=40,y=205)
number_entry = Entry(mngr,width=30,bd=2)
number_entry.place(x=240,y=205)
character_label = Label(mngr, text="# of special characters ",width=20,font=("times",12,"bold"),anchor="w",bg='rosybrown2')
character_label.place(x=40,y=280)
character_entry = Entry(mngr,width=30,bd=2)
character_entry.place(x=240,y=280)
password_button = Button(mngr, text='Generate Password', command=generate_random_password, bg= 'mistyrose2', font=("times",11, "bold"))
password_button.grid(row=3,column=2,sticky="EW")
password_button.place(x=185,y=350)
rand_pass = Label(mngr, text='Randomly Generated Password:')
rand_pass.place(x=170, y=400)
rand_pass_entry = Entry(mngr,width=30,bd=2)
rand_pass_entry.place(x=100, y=420, height=50, width=310)

def nextPage():
  mngr.destroy()
  import Input_Information

def prevPage():
  mngr.destroy()
  import Search_Passwords

int_inf = Button(mngr, text="Input Information", command=nextPage, width=22,bg='deeppink4',fg='white',font=("times",11,"bold"))
int_inf.place(x=5,y=505)
Ser_func = Button(mngr, text="Search Passwords", command=prevPage ,width=22,bg='maroon4',fg='white',font=("times",11,"bold"))
Ser_func.place(x=305,y=505)

mngr.mainloop()