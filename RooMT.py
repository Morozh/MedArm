import sqlite3
import tkinter
import tkinter.messagebox
conn=sqlite3.connect("database/medDB.db")

P_id=None
rootR=None

##ROOM BUTTON
def room_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
    conn = sqlite3.connect("database/medDB.db")
    r1=P_id.get()
    r2=room_t.get(tkinter.ACTIVE)
    r3=room_no.get(tkinter.ACTIVE)
    r4=rate.get()
    r5=da.get()
    r6=dd.get()
    conn.execute('INSERT INTO ROOM VALUES(?,?,?,?,?,?)',(r1,r3, r2, r4, r5, r6,))
    tkinter.messagebox.showinfo("medARM ЛИС система", "Анализ назначен")
    conn.commit()
    conn.close()

def update_button():
    global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
    r1=P_id.get()
    r2=room_t.get(tkinter.ACTIVE)
    r3=room_no.get(tkinter.ACTIVE)
    r4=rate.get()
    r5=da.get()
    r6=dd.get()
    p = list(conn.execute("Select * from ROOM where PATIENT_ID=?", (r1,)))
    if len(p) != 0:
        conn.execute('UPDATE ROOM SET ROOM_NO=?,ROOM_TYPE=?,RATE=?,DATE_ADMITTED=?,DATE_DISCHARGED=? where PATIENT_ID=?',(r3, r2, r4, r5, r6,r1,))
        tkinter.messagebox.showinfo("medARM ЛИС система", "Данные об анализе обновлены")
        conn.commit()
    else:
        tkinter.messagebox.showinfo("medARM ЛИС система", "Пациент не сдавал анализы")
##ROOT FOR DISPLAY ROOM INFO
rootRD=None

##EXIT FOR ROOM_PAGE
def EXITT():
    global rootR
    rootR.destroy()

##FUNCTION FOR ROOM DISPLAY BUTTON
def ROOMD_button():
    global r1,lr1,dis1,lr2,dis2,c1,ii,conn,c1,P_iid
    conn = sqlite3.connect("database/medDB.db")
    c1=conn.cursor()
    r1=P_iid.get()
    p=list(c1.execute('select * from  ROOM  where PATIENT_ID=?',(r1,)))
    if (len(p)==0):
        tkinter.messagebox.showinfo("medARM ЛИС система", "Пациент не сдавал анализы")
    else:
        t=c1.execute('SELECT NAME,ROOM_NO,ROOM_TYPE FROM ROOM NATURAL JOIN PATIENT where PATIENT_ID=?',(r1,));
        for ii in t:
            lr0=tkinter.Label(rootRD,text="Имя пациента",fg='blue', font="Times 12 bold")
            dis0=tkinter.Label(rootRD,text=ii[0])
            lr0.place(x=50,y=120)
            dis0.place(x=50,y=140)
            lr1=tkinter.Label(rootRD,text="Экстренный случай",fg='blue', font="Times 12 bold")
            dis1=tkinter.Label(rootRD,text=ii[1])
            lr1.place(x=50,y=170)
            dis1.place(x=50,y=190)
            lr2=tkinter.Label(rootRD,text="Назначенный анализ",fg='blue', font="Times 12 bold")
            dis2=tkinter.Label(rootRD,text=ii[2])
            lr2.place(x=50,y=220)
            dis2.place(x=50,y=240)

def exittt():
    rootRD.destroy()

def roomDD():
    global rootRD,ra1,ss,P_iid
    rootRD=tkinter.Tk()
    rootRD.geometry("280x280")
    rootRD.title("Данные о пациенте")
    ra1=tkinter.Label(rootRD,text="Введите ID пациента", bg="#73ACDA", fg='white', font="Times 16 bold", padx=10)
    ra1.place(x=0,y=0)
    P_iid=tkinter.Entry(rootRD, borderwidth=1, relief="solid")
    ss=tkinter.Button(rootRD,text="Поиск", borderwidth=1, relief="solid",command=ROOMD_button)
    ra1.place(x=0, y=0)
    P_iid.place(x=10, y=50)
    ss.place(x=10,y=90)
    e=tkinter.Button(rootRD,text="Выход", borderwidth=1, relief="solid",command=exittt)
    e.place(x=60,y=90)
    rootRD.iconbitmap('assets/medical.ico')
    rootRD.mainloop()

def exitt():
    rootR.destroy()

L=None
L1=None
def Room_all():
    global rootR,r_head,P_id,id,room_tl,L,i,room_t,room_nol,room_no,L1,j,ratel,rate,da_l,da ,dd_l,dd,Submit,Update,cr
    rootR = tkinter.Tk()
    rootR.title("Назначение анализов")
    rootR.geometry("400x400")
    r_head = tkinter.Label(rootR,text="Назначение анализов", bg="#73ACDA", fg='white', font="Times 16 bold", padx=10)
    r_head.place(x=0,y=0)
    id = tkinter.Label(rootR,text="ID пациента")
    id.place(x=10,y=30)
    P_id = tkinter.Entry(rootR, borderwidth=1, relief="solid")
    P_id.place(x=10,y=50)
    room_tl = tkinter.Label(rootR,text="Назначить анализ")
    room_tl.place(x=10, y=75)
    L = ["Анализ крови", "Анализ мочи", "COVID тест", "Биохимия", "Гормоны", "Бактериология", "Аллергология"]
    room_t= tkinter.Listbox(rootR, width=28, height=3, selectmode='SINGLE', exportselection=0)
    for i in L:
        room_t.insert(tkinter.END,i)
    room_t.place(x=10,y=100)
    room_nol=tkinter.Label(rootR,text="Экстренный случай")
    room_nol.place(x=10,y=160)
    L1=['Да', 'Нет']
    room_no = tkinter.Listbox(rootR, width=8, height=1, selectmode='SINGLE', exportselection=0)
    for j in L1:
        room_no.insert(tkinter.END,j)
    room_no.place(x=10,y=180)
    ratel=tkinter.Label(rootR, text="Название болезни (при наличии)")
    ratel.place(x=10, y=200)
    rate=tkinter.Entry(rootR, borderwidth=1, relief="solid")
    rate.place(x=10, y=220)
    da_l = tkinter.Label(rootR, text="Дата проведения анализа")
    da_l.place(x=10,y=240)
    da=tkinter.Entry(rootR, borderwidth=1, relief="solid")
    da.place(x=10,y=260)
    dd_l = tkinter.Label(rootR, text="Дата результатов анализа")
    dd_l.place(x=10, y=280)
    dd =tkinter.Entry(rootR, borderwidth=1, relief="solid")
    dd.place(x=10, y=300)
    Submit=tkinter.Button(rootR,text="Подтвердить", borderwidth=1, relief="solid",command=room_button)
    Submit.place(x=10,y=340)
    Update=tkinter.Button(rootR,text="Обновить", borderwidth=1, relief="solid",command=update_button)
    Update.place(x=100,y=340)
    cr=tkinter.Button(rootR,text='Подробнее о пациенте', borderwidth=1, relief="solid",command=roomDD)
    cr.place(x=170,y=340)
    ee=tkinter.Button(rootR,text="Выход", borderwidth=1, relief="solid",command=exitt)
    ee.place(x=330,y=340)
    rootR.iconbitmap('assets/medical.ico')
    rootR.mainloop()
