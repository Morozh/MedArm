import tkinter
import sqlite3
conn=sqlite3.connect("database/medDB.db")
rootAA=None

def set():
    global e3,e1,e2,e4,e5,e6,conn
    p1=e1.get()
    p2=e2.get()
    p3=e3.get(tkinter.ACTIVE)
    p4=e4.get()
    p5=e5.get()
    p6=e6.get(1.0,tkinter.END)
    conn = sqlite3.connect("database/medDB.db")
    conn.execute("Insert into appointment values(?,?,?,?,?,?)",(p1,p2,p3,p4,p5,p6,))
    conn.commit()
    tkinter.messagebox.showinfo("medARM ЛИС система", "Запись на прием прошла успешно")

def appo():
    global rootAP,e8
    rootAP=tkinter.Tk()
    rootAP.geometry("440x340")
    rootAP.title("Лаборатория")
    h1=tkinter.Label(rootAP,text="Введите ID пациента для поиска в лаборатории", bg="#73ACDA", fg='white', font="Times 14 bold", padx=10)
    h1.place(x=0,y=0)
    e8=tkinter.Entry(rootAP, borderwidth=1, relief="solid")
    e8.place(x=10,y=35)
    b5=tkinter.Button(rootAP,text="Поиск", borderwidth=1, relief="solid",command=viewappointment)
    b5.place(x=10,y=65)
    rootAP.iconbitmap('assets/medical.ico')
    rootAP.mainloop()

rootAP=None

def viewappointment():
    global e8
    global i,dis1,dis2,dis3,dis4,dis5,dis6
    global l1,l2,l3,l4,l5,l6
    ap=str(e8.get())
    vv = list(conn.execute("select * from ROOM where PATIENT_ID=?", (ap,)))
    if (len(vv) == 0):
        errorD = tkinter.Label(rootAP, text="Нет данных об анализах", fg="red")
        errorD.place(x=10, y=100)
    else:
        s=conn.execute("""select PATIENT_ID, ROOM_TYPE, RATE, AN_STATUS
                       from ROOM
                       NATURAL JOIN ANALYZES
                       where PATIENT_ID=?""", (ap,))
        for i in s:
            l1 = tkinter.Label(rootAP, text="Имя пациента", fg='blue', font="Times 12 bold")
            dis1 = tkinter.Label(rootAP, text=i[0])
            l2 = tkinter.Label(rootAP, text="Назначенный анализ", fg='blue', font="Times 12 bold")
            dis2 = tkinter.Label(rootAP, text=i[1])
            l3 = tkinter.Label(rootAP, text="Болезнь (при наличии)", fg='blue', font="Times 12 bold")
            dis3 = tkinter.Label(rootAP, text=i[2])
            l4 = tkinter.Label(rootAP, text="Статус анализа", fg='blue', font="Times 12 bold")
            dis4 = tkinter.Label(rootAP, text=i[3])
            l1.pack(pady=(100, 0))
            dis1.pack()
            l2.pack()
            dis2.pack()
            l3.pack()
            dis3.pack()
            l4.pack()
            dis4.pack()
            conn.commit()