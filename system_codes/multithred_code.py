from tkinter import *
import mysql.connector
from tkinter import messagebox
from win10toast import ToastNotifier
import _datetime as dt
import time
from system_codes import set_reminder_file as sr


def run(id,td):
    timedelta=td
    print(timedelta)
    idn=int(id[0])
    count = timedelta
    while count > 0:
        time.sleep(1)
        count -= 1

    #messagebox.showinfo("msg", "reminder")
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="reminder_application_database")
    mycursor = mydb.cursor()
    mycursor.execute("Select topic,note from reminders where id='" + str(idn) + "';")
    result = mycursor.fetchall()
    for i in result:
        toaster = ToastNotifier()
        toaster.show_toast("Reminder!!!!\n "+str(i[0])+" :"+str(i[1])+".")





