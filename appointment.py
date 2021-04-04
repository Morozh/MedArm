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
    global rootAA,L,e1,e2,e3,e4,e5,e6
    rootAA=tkinter.Tk()
    rootAA.geometry("500x460")
    rootAA.title("Запись на прием")
    H=tkinter.Label(rootAA,text="Запись на прием", bg="#73ACDA", fg='white', font="Times 16 bold", padx=10)
    H.place(x=0,y=0)
    l1=tkinter.Label(rootAA,text="ID пациента")
    l1.place(x=10,y=30)
    e1=tkinter.Entry(rootAA, borderwidth=1, relief="solid")
    e1.place(x=10,y=50)
    l2 = tkinter.Label(rootAA,text="ID доктора")
    l2.place(x=10,y=70)
    e2 = tkinter.Entry(rootAA, borderwidth=1, relief="solid")
    e2.place(x=10, y=90)
    l3 = tkinter.Label(rootAA,text="Номер записи")
    l3.place(x=10,y=115)
    L=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50']
    e3=tkinter.Listbox(rootAA, width=15, height=1, selectmode='SINGLE', exportselection=0)
    for jjj in L:
        e3.insert(tkinter.END, jjj)
    e3.place(x=140,y=115)
    scrollbar = tkinter.Scrollbar(rootAA,orient=tkinter.HORIZONTAL)
    scrollbar.place(x=245, y=115)
    e3.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=e3.yview)
    l4 = tkinter.Label(rootAA,text="Время записи (ЧАС:МИН)")
    l4.place(x=10,y=140)
    e4=tkinter.Entry(rootAA, borderwidth=1, relief="solid")
    e4.place(x=10,y=165)
    l5 = tkinter.Label(rootAA,text="Дата записи (ГГГГ-ММ-ДД)")
    l5.place(x=10,y=195)
    e5=tkinter.Entry(rootAA, borderwidth=1, relief="solid")
    e5.place(x=10,y=220)
    l6=tkinter.Label(rootAA,text="Описание")
    l6.place(x=10,y=240)
    e6=tkinter.Text(rootAA,width=55,height=3, borderwidth=1, relief="solid")
    e6.place(x=10,y=260)
    b1=tkinter.Button(rootAA,text="Записаться", borderwidth=1, relief="solid",command=set)
    b1.place(x=10,y=330)
    b2=tkinter.Button(rootAA,text="Удалить запись", borderwidth=1, relief="solid",command=dela)
    b2.place(x=180,y=330)
    b4=tkinter.Button(rootAA,text="Просмотр записей", borderwidth=1, relief="solid",command=va)
    b4.place(x=320,y=330)
    rootAA.iconbitmap('assets/medical.ico')
    rootAA.mainloop()

def remove():
    global e7,edd
    edd=str(e7.get())
    v=list(conn.execute("select * from appointment where AP_NO=?", (edd,)))
    if (len(v)==0):
        errorD = tkinter.Label(rootAA, text="Запись на прием не найдена",fg="red")
        errorD.place(x=10,y=440)
    else:
        conn.execute('DELETE FROM PATIENT where PATIENT_ID=?',(edd,))
        disd1=tkinter.Label(rootAA,text="Запись на прием удалена",fg='green', padx=5)
        disd1.place(x=10,y=440)
        conn.commit()

def dela():
    global e1,e7
    l3 = tkinter.Label(rootAA, text="Введите номер записи для удаления")
    l3.place(x=10, y=360)
    e7=tkinter.Entry(rootAA, borderwidth=1, relief="solid")
    e7.place(x=10,y=380)
    b3=tkinter.Button(rootAA,text="Удалить", borderwidth=1, relief="solid",command=remove)
    b3.place(x=10,y=410)

rootAP=None

def viewappointment():
    global e8
    global i,dis1,dis2,dis3,dis4,dis5,dis6
    global l1,l2,l3,l4,l5,l6
    ap=str(e8.get())
    vv = list(conn.execute("select * from appointment where PATIENT_ID=?", (ap,)))
    if (len(vv) == 0):
        errorD = tkinter.Label(rootAA, text="Нет записей на сегодня", fg="red")
        errorD.place(x=20, y=420)
    else:
        s=conn.execute("""select EMP_NAME, PATIENT_ID, AP_TIME, AP_DATE, description
                       from appointment
                       NATURAL JOIN employee
                       where appointment.PATIENT_ID=?""", (ap,))
        for i in s:
            l1 = tkinter.Label(rootAP, text="Имя врача", fg='blue', font="Times 12 bold")
            dis1 = tkinter.Label(rootAP, text=i[0])
            l2 = tkinter.Label(rootAP, text="ID пациента", fg='blue', font="Times 12 bold")
            dis2 = tkinter.Label(rootAP, text=i[1])
            l3 = tkinter.Label(rootAP, text="Время записи", fg='blue', font="Times 12 bold")
            dis3 = tkinter.Label(rootAP, text=i[2])
            l4 = tkinter.Label(rootAP, text="Дата записи", fg='blue', font="Times 12 bold")
            dis4 = tkinter.Label(rootAP, text=i[3])
            l5 = tkinter.Label(rootAP, text="Жалоба", fg='blue', font="Times 12 bold")
            dis5 = tkinter.Label(rootAP, text=i[4])
            l1.pack(pady=(100, 0))
            dis1.pack()
            l2.pack()
            dis2.pack()
            l3.pack()
            dis3.pack()
            l4.pack()
            dis4.pack()
            l5.pack()
            dis5.pack()
            conn.commit()

def va():
    global rootAP,e8
    rootAP=tkinter.Tk()
    rootAP.geometry("440x340")
    rootAP.title("Записи на сегодня")
    h1=tkinter.Label(rootAP,text="Введите ID пациента для просмотра записи", bg="#73ACDA", fg='white', font="Times 16 bold", padx=10)
    h1.place(x=0,y=0)
    e8=tkinter.Entry(rootAP, borderwidth=1, relief="solid")
    e8.place(x=10,y=35)
    b5=tkinter.Button(rootAP,text="Поиск", borderwidth=1, relief="solid",command=viewappointment)
    b5.place(x=10,y=65)
    rootAP.iconbitmap('assets/medical.ico')
    rootAP.mainloop()