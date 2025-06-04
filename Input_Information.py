from tkinter import *
from tkinter import messagebox
import json

mngr = Tk()
mngr.geometry('520x540')
mngr.title("Password Manager")

def saved_entries():

   user_website = website_entry.get()
   user_email = email_entry.get()
   user_password = password_entry.get()

   new_data = {
       user_website: {
           'email': user_email,
           'password': user_password
           }
       }
   if len(user_website) != 0 and len(user_password) != 0:

       try:
           with open('data.json', 'r') as data_file:
               data = json.load(data_file)
               data.update(new_data)
       except FileNotFoundError:
           with open('data.json','w') as data_file:
               json.dump(new_data, data_file, indent=4)
       else:
           is_correct = messagebox.askyesno(
                   title=f"{user_website}",
                   message=f"\n'username': {user_email}\n'password': {user_password}\n\nPlease confirm before saving!")
           if is_correct:
               with open('data.json','w') as data_file:
                   json.dump(data, data_file, indent=4)
                   website_entry.delete(0, END)
                   password_entry.delete(0, END)
   else:
       messagebox.showwarning(
           title='Error',
           message="Please don't leave any fields empty"
           )

def saveinfo():
   save()
   msg()

gui_header = Label(mngr, text="New Account Information",width=25,font=("times",20,"bold"),fg='teal')
gui_header.place(x=60,y=50)
website_label = Label(mngr, text="Website: ",width=20,font=("times",12,"bold"),anchor="w",bg='slategray3')
website_label.place(x=40,y=130)
website_entry = Entry(mngr,width=30,bd=2)
website_entry.place(x=240,y=130)
email_label = Label(mngr, text="Username: ",width=20,font=("times",12,"bold"),anchor="w",bg='lightblue3')
email_label.place(x=40,y=200)
email_entry = Entry(mngr,width=30,bd=2)
email_entry.place(x=240,y=200)
password_label = Label(mngr, text="Password: ",width=20,font=("times",12,"bold"),anchor="w",bg='paleturquoise3')
password_label.place(x=40,y=270)
password_entry = Entry(mngr,width=30,bd=2)
password_entry.place(x=240,y=270)

enter_button = Button(mngr, text='Enter', command=saved_entries, width=15,bg='darkcyan',fg='white',font=("times",12,"bold"))
enter_button.place(x=80,y=370)
cancel_button = Button(mngr, text='Cancel',command=mngr.destroy,width=15,bg='lightseagreen',fg='white',font=("times",12,"bold"))
cancel_button.place(x=280,y=370)

def nextPage():
  mngr.destroy()
  import Random_Password_Generator

def prevPage():
  mngr.destroy()
  import Search_Passwords

Rand_pass_gen = Button(mngr, text="Random Password Generator", command=nextPage, width=22,bg='cadetblue4',fg='white',font=("times",11,"bold"))
Rand_pass_gen.place(x=5,y=505)
Ser_func = Button(mngr, text="Search Passwords", command=prevPage ,width=22,bg='darkslategray4',fg='white',font=("times",11,"bold"))
Ser_func.place(x=305,y=505)

mngr.mainloop()