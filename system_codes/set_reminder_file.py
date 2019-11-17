from tkinter import *
import mysql.connector
from tkinter import messagebox
import _datetime as dt
import time
from system_codes import multithred_code as mc

import threading


'''def set_reminder():
    global screen_set_reminder
    screen_set_reminder = Toplevel()
    screen_set_reminder.title("SET A REMINDER")
    screen_set_reminder.geometry("1000x600")
    input_code(screen_set_reminder)
    Button(screen_set_reminder, text="SET REMINDER", width=30, height=2, bg="grey", command=save_reminder).pack()
'''

def set_reminder():


    global screen_set_reminder
    screen_set_reminder = Toplevel()
    screen_set_reminder.title("SET A REMINDER")
    screen_set_reminder.geometry("1000x600")

#options list for drop down menu ..........................
    years=create_liste(2019,2025)
    months=create_liste(1,12)
    days=create_liste(1,31)
    hours=create_liste(1,24)
    mins=create_liste(1,60)
    seconds=create_liste(1,60)
#............................................
    current_datetime = dt.datetime.today()
    global year,month,day,hour,minute,second

    year = StringVar(screen_set_reminder)
    month = StringVar(screen_set_reminder)
    day = StringVar(screen_set_reminder)
    hour = StringVar(screen_set_reminder)
    minute = StringVar(screen_set_reminder)
    second = StringVar(screen_set_reminder)

    year.set(current_datetime.year)
    month.set(current_datetime.month)
    day.set(current_datetime.day)
    hour.set(current_datetime.hour)
    minute.set(current_datetime.minute)
    second.set(current_datetime.second)


##header details..................................................................
    Label(screen_set_reminder, text="Set Reminder",font=("Arial",20,"bold italic")).pack()
    Label(screen_set_reminder, text="").pack()
    Label(screen_set_reminder,font=("Arial",10,"bold italic"), text="Today's Date :" + str(current_datetime.date())).pack()
    Label(screen_set_reminder, text="").pack()
    Label(screen_set_reminder,font=("Arial",10,"bold italic"), text="TIME :" + str(current_datetime.time())).pack()
    Label(screen_set_reminder, text="").pack()
#.................................................................................
    global topic,note
    topic = StringVar()
    note= StringVar()
    Label(screen_set_reminder,font=("Arial",8,"bold"), text="Name of the reminder").pack()
    Entry(screen_set_reminder,textvariable=topic).pack()
    Label(screen_set_reminder,font=("Arial",8,"bold"), text="Note for the reminder").pack()
    Entry(screen_set_reminder, textvariable=note).pack()

#date and time drop down menues..................
    Label(screen_set_reminder, text="Year :").pack()
    OptionMenu(screen_set_reminder, year, *years).pack()
    Label(screen_set_reminder, text="month :").pack()
    OptionMenu(screen_set_reminder, month, *months).pack()
    Label(screen_set_reminder, text="day :").pack()
    OptionMenu(screen_set_reminder, day, *days).pack()

    Label(screen_set_reminder, text="hour :").pack()
    OptionMenu(screen_set_reminder, hour, *hours).pack()
    Label(screen_set_reminder, text="mins :").pack()
    OptionMenu(screen_set_reminder, minute, *mins).pack()
    Label(screen_set_reminder, text="secs :").pack()
    OptionMenu(screen_set_reminder, second, *seconds).pack()



    Button(screen_set_reminder,text="SAVE REMINDER",width=30,height=2,bg="grey",command=save_reminder).pack()






def save_reminder():
        screen_set_reminder.destroy()
        #print(year.get(),month.get(),day.get(),hour.get(),minute.get(),second.get(),topic.get(),note.get())
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234",database="reminder_application_database")
        mycursor = mydb.cursor()
        state=1
        yr=year.get()
        mo=month.get()
        dy=day.get()
        hr=hour.get()
        mi=minute.get() #column name is min
        sec=second.get()
        tp=topic.get()
        print(tp)
        nt=note.get()
        print(yr, mo, dy, hr, mi, sec)
        #mycursor.execute("create table reminders(id int(20) NOT NULL auto_increment,topic varchar(50),note varchar(150),state varchar(10),primary key (id))")
        mycursor.execute("insert into reminders values('0','"+str(tp)+ "'" + "," + "'" +str(nt)+ "'" + "," + "'"+str(state)+"'"+","+ "'" + str(hr) + "'"+","
                         + "'" + str(mo) + "'" + ","+ "'" + str(dy) + "'"+","+ "'" + str(hr) + "'"+","+ "'" + str(mi) + "'"+","+ "'" + str(sec) + "'"+")")

        mydb.commit()

        start_reminder(yr, mo, dy, hr, mi, sec)

#Fuction to count seconds btw current and reminder time.................and starting thread named as id.

def start_reminder(year,month,day,hour,minute,seconds):
    #print(year,month,day,hour,minute,seconds)
    year=int(year)
    month=int(month)
    day=int(day)
    hour=int(hour)
    minute=int(minute)
    seconds=int(seconds)
    current_datetime=dt.datetime.today()
    reminder_datetime=dt.datetime(year,month,day,hour,minute,seconds,0)
    timedelta=(reminder_datetime-current_datetime)
    messagebox.showinfo("done","time remaining to reminder\n"+str(timedelta))
    #print(current_datetime,reminder_datetime)
    #print(timedelta.total_seconds())
    tp= topic.get()
    print(tp)
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="reminder_application_database")
    mycursor = mydb.cursor()
    mycursor.execute("select id from reminders where topic='"+str(tp)+"'")
    threade_index=mycursor.fetchone()


    t=threading.Thread(target=mc.run(threade_index,abs(timedelta.total_seconds())),args=(threade_index,))

def create_liste(start,end):
    if start==end:
        return start
    else:
        res=[]
        while(start<end+1):
            res.append(start)
            start+=1
        return res