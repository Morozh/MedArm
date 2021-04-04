import sqlite3
import tkinter
import tkinter.messagebox
conn=sqlite3.connect("database/medDB.db")

#variables
rootB=None

def date_up():
    global b1,b2
    b1 = P_id.get()
    b2 = dd.get()
    conn.execute("UPDATE ROOM SET DATE_DISCHARGED=? where PATIENT_ID=?", (b2, b1,))
    conn.commit()
    tkinter.messagebox.showinfo("medARM ЛИС система", "Дата выписки обновлена")

def up():
    global c1, b1, P_id, b3, b4, b5, b6, dd, treat_1, treat_2, cost_t, b7, b8, med, med_q, price, u
    conn = sqlite3.connect("database/medDB.db")
    c1 = conn.cursor()
    b1 = P_id.get()
    b3 = treat_1.get(tkinter.ACTIVE)
    b4 = treat_2.get(tkinter.ACTIVE)
    b5 = cost_t.get()
    b6 = med.get(tkinter.ACTIVE)
    b7 = med_q.get(tkinter.ACTIVE)
    b8 = price.get()
    conn.execute("INSERT INTO TREATMENT VALUES(?,?,?,?)", (b1, b3, b4, b5,))
    conn.execute("INSERT INTO MEDICINE VALUES(?,?,?,?)", (b1, b6, b7, b8,))
    conn.commit()
    tkinter.messagebox.showinfo("medARM ЛИС система", "Платежные данные сохранены")

def calci():
    global b1
    conn = sqlite3.connect("database/medDB.db")
    u=conn.execute("Select sum(T_COST+ (M_COST*M_QTY) +(DATE_DISCHARGED-DATE_ADMITTED)*RATE) FROM ROOM NATURAL JOIN TREATMENT natural JOIN MEDICINE where PATIENT_ID=?",(b1,) )
    conn.commit()
    for ii in u:
        pp=tkinter.Label(rootB,text="Общая сумма к уплате", fg='red', font="Times 12 bold")
        pp.place(x=200, y=260)
        uu=tkinter.Label(rootB,text=ii[0])
        uu.place(x=230, y=290)

L1=None
L2=None
L3=None
L4=None

def exitt():
    rootB.destroy()

def BILLING():
    global rootB,L1,treat1,P_id,dd,cost,med,med_q,price,treat_1,treat_2,cost_t,j,jj,jjj,jjjj,L2,L3,L4
    rootB=tkinter.Tk()
    rootB.geometry("600x400")
    rootB.title("Платежная система")
    head=tkinter.Label(rootB,text="Карта пациента", bg="#73ACDA", fg='white', font="Times 16 bold", padx=30)
    head.place(x=0,y=0)
    id = tkinter.Label(rootB, text="ID пациента")
    id.place(x=10, y=40)
    P_id = tkinter.Entry(rootB, borderwidth=1, relief="solid")
    P_id.place(x=10, y=60)
    dd_l = tkinter.Label(rootB, text="Дата выписки")
    dd_l.place(x=10, y=80)
    dd = tkinter.Entry(rootB, borderwidth=1, relief="solid")
    dd.place(x=10, y=100)
    ddp=tkinter.Button(rootB,text="Обновить дату выписки", borderwidth=1, relief="solid",command=date_up)
    ddp.place(x=150,y=97)
    treat = tkinter.Label(rootB, text="Тип услуги")
    treat.place(x=10, y=140)
    L1 = ["Консультация","Операция","Анализы"]
    treat_1= tkinter.Listbox(rootB, width=16, height=1, selectmode='SINGLE', exportselection=0, borderwidth=1, relief="solid")
    for j in L1:
        treat_1.insert(tkinter.END, j)
    treat_1.place(x=90,y=140)
    treat_c = tkinter.Label(rootB, text="Код")
    treat_c.place(x=200, y=140)
    L2 = ["C_1", "S_1", "L_1"]
    treat_2 = tkinter.Listbox(rootB, width=6, height=1, selectmode='SINGLE', exportselection=0, borderwidth=1, relief="solid")
    for jj in L2:
        treat_2.insert(tkinter.END, jj)
    treat_2.place(x=240, y=140)
    costl= tkinter.Label(rootB, text="Цена ₽")
    costl.place(x=305, y=140)
    cost_t = tkinter.Entry(rootB,width=8, borderwidth=1, relief="solid")
    cost_t.place(x=350, y=140)
    med1 = tkinter.Label(rootB, text="Препараты")
    med1.place(x=10, y=180)
    L3 = ["Успокоительное", "Ношпа", "Дисприн", "Доло+", "Перевязывание", "Парацетамол"]
    med = tkinter.Listbox(rootB, width=16, height=1, selectmode='SINGLE', exportselection=0, borderwidth=1, relief="solid")
    for jjj in L3:
        med.insert(tkinter.END, jjj)
    med.place(x=90, y=180)
    med_ql = tkinter.Label(rootB, text="Количество")
    med_ql.place(x=200, y=180)
    L4 = [1,2,3,4,5,6,7,8,9,10]
    med_q = tkinter.Listbox(rootB, width=4, height=1, selectmode='SINGLE', exportselection=0, borderwidth=1, relief="solid")
    for jjjj in L4:
        med_q.insert(tkinter.END, jjjj)
    med_q.place(x=280, y=180)
    pricel = tkinter.Label(rootB, text="Цена ₽")
    pricel.place(x=325, y=180)
    price = tkinter.Entry(rootB, width=8, borderwidth=1, relief="solid")
    price.place(x=380, y=180)
    b1=tkinter.Button(rootB,text="Создать", borderwidth=1, relief="solid",command=calci)
    b1.place(x=10,y=210)
    b2 = tkinter.Button(rootB, text="Обновить", borderwidth=1, relief="solid", command=up)
    b2.place(x=70, y=210)
    ee=tkinter.Button(rootB,text="Выйти", borderwidth=1, relief="solid",command=exitt)
    ee.place(x=140,y=210)
    rootB.iconbitmap('assets/medical.ico')
    rootB.mainloop()
