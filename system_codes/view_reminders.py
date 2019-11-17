from tkinter import *
import mysql.connector


def view_reminder():
    global screen_view_reminder
    screen_view_reminder = Toplevel()
    screen_view_reminder.title("view")
    screen_view_reminder.geometry("500x600")
    Label(screen_view_reminder,text="ID ----                    DATE                   TIME                    TILTE                      NOTE").pack()

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="reminder_application_database")
    mycursor = mydb.cursor()
    mycursor.execute("select * from reminders")
    result = mycursor.fetchall()
    for i in result:
        Label(screen_view_reminder,text=str(i[0])+" ----"+str(i[4])+"-"+str(i[5])+"-"+str(i[6])+"-    "
                                        +str(i[7])+":"+str(i[8])+":"+str(i[9])+"        "+" -"+i[1]+"      -"+i[2]).pack()
    Button(screen_view_reminder,text="CLOSE" ,command=ok,width=30,height=2).pack()
    Label(screen_view_reminder,text="")

def ok():
    screen_view_reminder.destroy()
