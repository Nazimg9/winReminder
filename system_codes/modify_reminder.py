
from tkinter import *
import mysql.connector
from tkinter import messagebox
import _datetime as dt
from system_codes import set_reminder_file as sr
import threading
from system_codes import multithred_code as mc



def modify_deatils_screen():
    global screen_modify_reminder
    screen_modify_reminder = Toplevel()
    screen_modify_reminder.title("MOdify")
    screen_modify_reminder.geometry("500x600")
    Label(screen_modify_reminder,
          text="ID ----                    DATE                   TIME                    TILTE                      NOTE").pack()

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="reminder_application_database")
    mycursor = mydb.cursor()
    mycursor.execute("select * from reminders")
    result = mycursor.fetchall()
    for i in result:
        Label(screen_modify_reminder, text=str(i[0]) + " ----" + str(i[4]) + "-" + str(i[5]) + "-" + str(i[6]) + "-    "
                                           + str(i[7]) + ":" + str(i[8]) + ":" + str(i[9]) + "        " + " -" + i[
                                               1] + "      -" + i[2]).pack()

    Label(screen_modify_reminder, text="\n").pack()
    Label(screen_modify_reminder, text="Enter Reminder ID to make changes", font=("Arial", 15, "bold")).pack()
    global id
    id = StringVar()
    Entry(screen_modify_reminder, textvariable=id).pack()
    Button(screen_modify_reminder, text="MODIFY", command=modify_data_input, width=20, height=2, bg="grey").pack()

#to insert new input screen will be opened
def modify_data_input():
    screen_modify_reminder.destroy()
    global screen_modify_input
    screen_modify_input = Toplevel()
    screen_modify_input.title("Modify")
    screen_modify_input.geometry("500x600")
#options list for drop down menu ..........................
    years=sr.create_liste(2019,2025)
    months=sr.create_liste(1,12)
    days=sr.create_liste(1,31)
    hours=sr.create_liste(1,24)
    mins=sr.create_liste(1,60)
    seconds=sr.create_liste(1,60)
    states=['0','1']
#............................................
    current_datetime = dt.datetime.today()
    global year,month,day,hour,minute,second,state

    year = StringVar(screen_modify_input)
    month = StringVar(screen_modify_input)
    day = StringVar(screen_modify_input)
    hour = StringVar(screen_modify_input)
    minute = StringVar(screen_modify_input)
    second = StringVar(screen_modify_input)
    state=StringVar(screen_modify_input)
    mydb =mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="reminder_application_database")
    mycursor = mydb.cursor()
    idno=id.get()
    mycursor.execute("select * from reminders where id='"+str(idno)+"';")
    result=mycursor.fetchall()
    for u in result:
        print(u)
    for i in result:
        state.set(i[3])
        year.set(i[4])

        month.set(i[5])
        day.set(i[6])
        hour.set(i[7])
        minute.set(i[8])
        second.set(i[9])


#header details......................
    Label(screen_modify_input, text="MODIFY REQUIRED DETAILS",font=("Arial",20,"bold italic")).pack()
    Label(screen_modify_input, text="").pack()
    Label(screen_modify_input,font=("Arial",10,"bold italic"), text="Today's Date :" + str(current_datetime.date())).pack()
    Label(screen_modify_input, text="").pack()
    Label(screen_modify_input,font=("Arial",10,"bold italic"), text="TIME :" + str(current_datetime.time())).pack()
    Label(screen_modify_input, text="").pack()
#getting new title and note ..............................
    global topic,note
    topic = StringVar()
    note= StringVar()
    Label(screen_modify_input,font=("Arial",8,"bold"), text="Name of the reminder").pack()
    Entry(screen_modify_input,textvariable=topic).pack()
    Label(screen_modify_input,font=("Arial",8,"bold"), text="Note for the reminder").pack()
    Entry(screen_modify_input, textvariable=note).pack()

#date and time drop down menues..................
    Label(screen_modify_input, text="Year :").pack()
    OptionMenu(screen_modify_input, year, *years).pack()
    Label(screen_modify_input, text="month :").pack()
    OptionMenu(screen_modify_input, month, *months).pack()
    Label(screen_modify_input, text="day :").pack()
    OptionMenu(screen_modify_input, day, *days).pack()

    Label(screen_modify_input, text="hour :").pack()
    OptionMenu(screen_modify_input, hour, *hours).pack()
    Label(screen_modify_input, text="mins :").pack()
    OptionMenu(screen_modify_input, minute, *mins).pack()
    Label(screen_modify_input, text="secs :").pack()
    OptionMenu(screen_modify_input, second, *seconds).pack()
    Label(screen_modify_input, text="State :").pack()
    OptionMenu(screen_modify_input, state, *states).pack()
    Button(screen_modify_input, text="SAVE", width=30, height=2, bg="grey", command=save_reminder).pack()



def save_reminder():
    screen_modify_input.destroy()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="reminder_application_database")
    mycursor = mydb.cursor()
    idn=id.get()
    yr = year.get()
    mo = month.get()
    dy = day.get()
    hr = hour.get()
    mi = minute.get()  # column name is min
    sec = second.get()
    tp = topic.get()
    nt = note.get()
    st =state.get()
    print(yr, mo, dy, hr, mi, sec)
    # mycursor.execute("create table reminders(id int(20) NOT NULL auto_increment,topic varchar(50),note varchar(150),state varchar(10),primary key (id))")
    mycursor.execute("update reminders set topic='" + str(tp) + "'" + "," + "note='" + str(nt) + "'" + ","+"state='"+str(st)+"'" +","+ "hr='" + str(hr) + "'" + ","
                     + "mo='" + str(mo) + "'" + "," + "dy='" + str(dy) + "'" + "," + "hr='" + str(hr) +
                     "'" + "," + "min='" + str(mi) + "'" + "," + "sec='" + str(sec) + "' where id='"+str(idn)+"'" )

    mydb.commit()
    sr.start_reminder(yr, mo, dy, hr, mi, sec)


def start_reminder(year,month,day,hour,minute,seconds):
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    minute = int(minute)
    seconds = int(seconds)
    current_datetime = dt.datetime.today()
    reminder_datetime = dt.datetime(year, month, day, hour, minute, seconds, 0)
    timedelta = (reminder_datetime - current_datetime)
    messagebox.showinfo("done", "time remaining to reminder\n" + str(timedelta))
    # print(current_datetime,reminder_datetime)
    # print(timedelta.total_seconds())
    tp = topic.get()
    print(tp)
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="reminder_application_database")
    mycursor = mydb.cursor()
    mycursor.execute("select id from reminders where topic='" + str(tp) + "'")
    threade_index = mycursor.fetchone()

    t = threading.Thread(target=mc.run(timedelta.total_seconds()), args=(threade_index,))




