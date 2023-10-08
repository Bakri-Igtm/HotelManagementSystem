from tkinter import *
from PIL import Image, ImageTk


ht = Tk()
ht.title("Solarkin Hotel Management Suite")
ht.geometry("1000x1000")
at = Frame(width=1000, height=1000, bg='black')
at.pack()


def checking_in():
    import random
    import sqlite3

    ab = Tk()
    ab.geometry("1000x1000")
    ab.title("Check In Page")
    cl = Frame(ab, width=1000, height=150, bg="#000064")
    cl.place(x=0, y=50)

    def check_in():

        First_Name = FN.get().title()
        Middle_Name = FN2.get()
        Last_Name = FN3.get()
        Phone_Number = FN4.get()
        Email = FN5.get()
        Room_no = b2.get()

        # Emptying guest entries 
        FN.delete(0, 'end')
        FN2.delete(0, 'end')
        FN3.delete(0, 'end')
        FN5.delete(0, 'end')
        FN4.delete(0, 'end')
        b2.delete(0, 'end')


        connection = sqlite3.connect("guest.db")
        cursor = connection.cursor()

        command = "CREATE TABLE IF NOT EXISTS Guest (First_Name TEXT, Middle_Name TEXT, Last_Name TEXT, Phone_Number INTEGER, Email TEXT, Room_Number INTEGER)"
        connection.execute(command)


        comms = "INSERT INTO Guest (First_Name, Middle_Name, Last_Name, Phone_Number, Email, Room_Number) VALUES (?, ?, ?, ?, ?, ?)"
        comms_tuple = (First_Name, Middle_Name, Last_Name, Phone_Number, Email, Room_no)
        cursor = connection.cursor()
        cursor.execute(comms, comms_tuple)
        connection.commit()
        connection.close()


    Flaa = Frame(ab, width=1000, height=100, bg='#000064')
    Flaa.place(x=0, y=0)

    SMS = Label(Flaa, text='SOLARKIN HOTEL MANAGEMENT', bg='#83838B', fg='white', font=('Courier', 40))
    SMS.place(x=0, y=30)

    Floss = Frame(ab, width=600, height=800, bg='black')
    Floss.place(x=0, y=200)

    Floss2 = Frame(ab, width=400, height=1000, bg='#000064')
    Floss2.place(x=600, y=200)

    Pers = Label(Floss, text='Personal Information', font=('Times', 15), fg='white', bg='black')
    Pers.place(x=250, y=20)


    a = Label(Floss, text="First Name:", font=("Courier", 9), bg="black", fg="white")
    a.place(x=20, y=50)
    FN = Entry(Floss, width=25)
    FN.place(x=100, y=50)

    b = Label(Floss, text="Middle Name:", font=("Courier", 9), bg="black", fg="white")
    b.place(x=20, y=100)
    FN2 = Entry(Floss, width=25)
    FN2.place(x=120, y=100)


    c = Label(Floss, text="Last Name:", font=("Courier", 9), bg="black", fg="white")
    c.place(x=20, y=150)
    FN3 = Entry(Floss, width=25)
    FN3.place(x=100, y=150)

    Pers2 = Label(Floss, text='Contact Information', font=('Times', 15), fg='white', bg='black')
    Pers2.place(x=250, y=200)

    d = Label(Floss, text="Phone Number:", font=("Courier", 9), bg="black", fg="white")
    d.place(x=20, y=250)
    FN4 = Entry(Floss, width=25)
    FN4.place(x=120, y=250)

    e = Label(Floss, text="Email:", font=("Courier", 9), bg="black", fg="white")
    e.place(x=20, y=300)
    FN5 = Entry(Floss, width=25)
    FN5.place(x=100, y=300)

    c4 = IntVar(Floss, value=random.randint(0, 400))
    b1 = Label(Floss, text="Available Room to Use", bg='black', fg='white')
    b1.place(x=20, y=350)
    b2 = Entry(Floss, width=10, textvariable=c4)
    b2.place(x=250, y=350)

    d2 = Label(Floss, text="Note: All rooms are deluxe suite", fg='red', bg='black')
    d2.place(x=20, y=375)
    cd = Button(Floss, text='Check In', fg='#000064', command=check_in)
    cd.place(x=250, y=400)

    Bt = Button(Floss2, text='Exit', fg='white', command=ab.destroy, bg="black")
    Bt.place(x=100, y=120, width=100, height=100)
    ab.mainloop() 




def show_all_guests_info():
    import sqlite3
    my_conn = sqlite3.connect('guest.db')
    my_w = Tk()
    my_w.geometry("1300x1300")
    my_w.title("All Guest Information")
    my_w.config(bg="cyan")
    r_set = my_conn.execute("SELECT * FROM guest LIMIT 0,400");
    i = 0
    for guest in r_set:
        for j in range(len(guest)):
            e = Entry(my_w, width=25, fg="blue")
            e.grid(row=i, column=j)
            e.insert(END, guest[j])
        i=i+1

    ac = Button(my_w, text="Exit", command=my_w.destroy, fg='black', bg="cyan")
    ac.place(x=1000, y=450, width=200)

    my_w.mainloop()






def check_out():
    import sqlite3
    
    def delete_record():
        try:
            connection = sqlite3.connect("guest.db")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Guest WHERE Room_Number = ?", (af.get(),))
            connection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Error: ", error)
        af.delete(0, 'end')
    root = Tk()
    root.geometry("200x500")
    root.title("Guest Check-out Forum")
    root.config(bg='teal')

    bc = Label(root, text="Check Outs", font=30, bg='teal')
    bc.place(x=50, y=50)

    ad = Label(root, text="Enter the Guest's room number: ", bg='teal')
    ad.place(x=10, y=200)

    af = Entry(root, width=10)
    af.place(x=50, y=250)

    ag = Button(root, text="Check Out", command=delete_record)
    ag.place(x=50, y=300)

    ad = Button(root, text='Back', command=root.destroy)
    ad.place(x=50, y=350)
    root.mainloop()



Labs = Label(at, text="WELCOME ", font=('Times', 40), fg="teal", bg='black')
Labs.place(x=500, y=40)
Labs1 = Label(at, text="TO", font=('Times', 30), fg="teal", bg='black')
Labs1.place(x=600, y=100)
Labs2 = Label(at, text="SOLARKIN HOTEL", font=('Times', 30), fg="teal", bg='black')
Labs2.place(x=500, y=150)

Fram = Frame(at, width=900, height=900)
Fram.place(x=500, y=200)
img = ImageTk.PhotoImage(Image.open('Solark.jpg'))
img_label = Label(Fram, image = img, bg='black')
img_label.pack()

Btn = Button(at, text="CHECK IN", bg="teal", command=checking_in)
Btn.place(x=100, y=200, width=350, height=70)

Btn2 = Button(at, text="SHOW GUEST LIST", bg="teal", command=show_all_guests_info)
Btn2.place(x=100, y=300, width=350, height=70)

Btn3 = Button(at, text="CHECK OUT", bg="teal", command=check_out)
Btn3.place(x=100, y=400, width=350, height=70)

Btn5 = Button(at, text="EXIT", bg="teal", command=ht.destroy)
Btn5.place(x=100, y=550, width=350, height=100)

Lab = Label(at, text='"... your comfort is', font=('Italics', 30) ,fg="teal", bg="black")
Lab.place(x=520, y=520)

Lab2 = Label(at, text='our happiness ..."', font=('Italics', 30) ,fg="teal", bg="black")
Lab2.place(x=570, y=570)



Frams = Frame(at, width=200, height=150, bg="black")
Frams.pack()
Frams.place(x=100, y=20)
imgs = ImageTk.PhotoImage(Image.open('Solark Logo.jpg'))
imgs_labels = Label(Frams, image = imgs, bg="black")
imgs_labels.place(x=100, y=20)


ht.mainloop()