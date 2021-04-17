import sqlite3
import tkinter
import tkinter.messagebox
conn=sqlite3.connect("database/medDB.db")

#variables
rootB=None

def create():
    global c1, b1, b2, b3, b4, P_id, dd, treat_1, price, med
    conn = sqlite3.connect("database/medDB.db")
    c1 = conn.cursor()
    b1 = P_id.get()
    b2 = dd.get()
    b3 = treat_1.get(tkinter.ACTIVE)
    b4 = price.get()
    b5 = med.get(tkinter.ACTIVE)

    conn.execute("INSERT INTO ANALYZES VALUES(?,?,?,?,?)", (b1, b2, b3, b4, b5))
    conn.commit()
    tkinter.messagebox.showinfo("medARM ЛИС система", "Запись об анализе успешно добавлена")

def exit():
    rootB.destroy()

def BILLING():
    global rootB,L1,L3,treat1,P_id,dd,cost,med,med_q,price,treat_1,j,jjj
    rootB = tkinter.Tk()
    rootB.geometry("300x350")
    rootB.title("Процедурный кабинет")
    head = tkinter.Label(rootB,text="Процедурный кабинет", bg="#73ACDA", fg='white', font="Times 16 bold", padx=30)
    head.place(x=0,y=0)
    id = tkinter.Label(rootB, text="ID пациента")
    id.place(x=10, y=40)
    P_id = tkinter.Entry(rootB, borderwidth=1, relief="solid")
    P_id.place(x=10, y=60)
    dd_l = tkinter.Label(rootB, text="Дата сдачи анализа")
    dd_l.place(x=10, y=80)
    dd = tkinter.Entry(rootB, borderwidth=1, relief="solid")
    dd.place(x=10, y=100)
    treat = tkinter.Label(rootB, text="Наименование анализа")
    treat.place(x=10, y=120)
    L1 = ["Анализ крови", "Анализ мочи", "COVID тест", "Биохимия", "Гормоны", "Бактериология", "Аллергология"]
    treat_1= tkinter.Listbox(rootB, width=20, height=1, selectmode='SINGLE', exportselection=0, borderwidth=1, relief="solid")
    for j in L1:
        treat_1.insert(tkinter.END, j)
    treat_1.place(x=10,y=140)
    costl = tkinter.Label(rootB, text="Цена ₽")
    costl.place(x=10, y=160)
    price = tkinter.Entry(rootB,width=8, borderwidth=1, relief="solid")
    price.place(x=10, y=180)
    med1 = tkinter.Label(rootB, text="Статус анализа")
    med1.place(x=10, y=200)
    L3 = ["Анализ в процессе", "Анализ не выполнен", "Анализ готов"]
    med = tkinter.Listbox(rootB, width=20, height=1, selectmode='SINGLE', exportselection=0, borderwidth=1, relief="solid")
    for jjj in L3:
        med.insert(tkinter.END, jjj)
    med.place(x=10, y=220)
    b1 = tkinter.Button(rootB,text="Создать", borderwidth=1, relief="solid",command=create)
    b1.place(x=10, y=250)
    ee = tkinter.Button(rootB,text="Выйти", borderwidth=1, relief="solid",command=exit)
    ee.place(x=70, y=250)
    rootB.iconbitmap('assets/medical.ico')
    rootB.mainloop()
