from tkinter import *
import mysql.connector
from tkinter import messagebox
from system_codes import view_reminders as vr

def delete_reminder():
    global screen_delete_reminder
    screen_delete_reminder = Toplevel()
    screen_delete_reminder.title("Delete")
    screen_delete_reminder.geometry("500x600")
    Label(screen_delete_reminder,text="ID ----                    DATE                   TIME                    TILTE                      NOTE").pack()

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="reminder_application_database")
    mycursor = mydb.cursor()
    mycursor.execute("select * from reminders")
    result = mycursor.fetchall()
    for i in result:
        Label(screen_delete_reminder,text=str(i[0])+" ----"+str(i[4])+"-"+str(i[5])+"-"+str(i[6])+"-    "
                                        +str(i[7])+":"+str(i[8])+":"+str(i[9])+"        "+" -"+i[1]+"      -"+i[2]).pack()

    Label(screen_delete_reminder,text="\n").pack()
    Label(screen_delete_reminder,text="Enter Reminder ID to Delete",font=("Arial",15,"bold")).pack()
    global id
    id=StringVar()
    Entry(screen_delete_reminder,textvariable=id).pack()
    Button(screen_delete_reminder, text="DELETE", command=ok, width=20, height=2,bg="grey").pack()

def ok():
    print(id.get())
    id_no=id.get()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="reminder_application_database")
    mycursor = mydb.cursor()
    mycursor.execute("delete from reminders where id='"+str(id_no)+"'")
    messagebox.showinfo("info","ID:"+str(id_no)+"\n reminder deleted")

    mydb.commit()
    vr.view_reminder()
    screen_delete_reminder.destroy()



