from tkinter import *
from tkinter import messagebox
import json

mngr = Tk()
mngr.geometry('520x540')
mngr.title("Password Manager")

def search_website():

 user_website = website_entry.get()

 try:
     with open('data.json', 'r') as data_file:
         data = json.load(data_file)
         user_password = data[user_website]['password']
         pass_result.delete(0, END)
         pass_result.insert(0, user_password)
 except KeyError as error_msg:
     messagebox.showinfo(title="Error", message=f"{error_msg} password does not exist")
 except FileNotFoundError as error_msg:
     messagebox.showinfo(message="File does not exist. Try using Add instead")

gui_header = Label(mngr, text="Search Account Passwords", width=25, font=("times", 20, "bold"), fg='darkolivegreen')
gui_header.place(x=60, y=50)

search_label = Label(mngr, text="Enter website ",width=20,font=("times",12,"bold"),anchor="w",bg='darkseagreen4', fg='white')
search_label.place(x=40,y=150)
website_entry = Entry(mngr,width=30,bd=2)
website_entry.place(x=240,y=150)
search_button = Button(mngr, text='Search', command=search_website, width=15,bg='darkseagreen',fg='white',font=("times",12,"bold"))
search_button.place(x=180,y=250)

result_label = Label(mngr, text='Password:')
result_label.place(x=225, y=350)
pass_result = Entry(mngr,width=30,bd=2)
pass_result.place(x=100, y=375, height=50, width=310)

def nextPage():
    mngr.destroy()
    import Input_Information

def prevPage():
    mngr.destroy()
    import Random_Password_Generator

int_inf = Button(mngr, text="Input Information", command=nextPage, width=22,bg='palegreen4',fg='white',font=("times",11,"bold"))
int_inf.place(x=5,y=505)
Rand_pass_gen = Button(mngr, text="Random Password Generator", command=prevPage, width=22,bg='seagreen4',fg='white',font=("times",11,"bold"))
Rand_pass_gen.place(x=305,y=505)

mngr.mainloop()