import sqlite3
my_conn = sqlite3.connect('guest.db')
from tkinter import *

a = Tk()
a.title('Guest Info')
a.geometry('800x300')

def guest_details(Room_Entry):
    try:
        val = int(Room_Entry)
        try:
            my_data = (val, )
            q="SELECT * FROM guest WHERE Room_Number = ?"
            my_cursor = my_conn.execute(q, my_data)
            data_row = my_cursor.fetchone()
            my_str.set(data_row)

        except sqlite3.Error as my_error:
            print("error: ", my_error)
        
    except:
        my_str.set("No record found")



guest_info_frame = Frame(a, width=800, height=300, bg='black')
guest_info_frame.place(x=0, y=0)

Room_number = Label(guest_info_frame, text="Enter the rooom  number of the guest", font=('Courier', 20), fg='white', bg='black')
Room_number.place(x=0, y=0)
Room_Entry = Entry(guest_info_frame, width=50)
Room_Entry.place(x=50, y=100, height=50)

Check = Button(guest_info_frame, text="Check Details", command=lambda:  guest_details(Room_Entry.get()))
Check.place(x=50, y=200, width=200, height=20)

my_str = StringVar()
l2 = Label(a, textvariable=my_str, font=15, fg='red')
l2.place(x=50, y=150)

de = Button(a, text='Back', command=a.destroy, fg="black")
de.place(x=300, y=200)
a.mainloop()