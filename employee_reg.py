import tkinter
import sqlite3
rootE=None
var=None

def inp():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,var
    e1=t1.get()
    e2=t2.get()
    e3=str(var.get())
    e4=t3.get()
    e5=lb.get(tkinter.ACTIVE)
    e6=t4.get()
    e7=t5.get()
    e8=t6.get()
    e9=t7.get()
    conn = sqlite3.connect("database/medDB.db")
    conn.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,))
    conn.commit()
    tkinter.messagebox.showinfo("medARM ЛИС система", "Данные о работнике занесены")

def ex():
    rootE.destroy()

def emp_screen():
    global rootE,t1,t2,r1,r2,t3,lb,t4,t5,t6,t7,var
    rootE=tkinter.Tk()
    rootE.title("Регистрация сотрудника")
    rootE.geometry('260x550')
    var = tkinter.StringVar(master=rootE)
    H=tkinter.Label(rootE,text="Регистрация сотрудника", bg="#73ACDA", fg='white', font="Times 16 bold", padx=10)
    H.place(x=0,y=0)
    l1=tkinter.Label(rootE,text="ID сотрудника")
    l1.place(x=10,y=50)
    t1=tkinter.Entry(rootE, borderwidth=1, relief="solid")
    t1.place(x=10,y=70)
    l2 = tkinter.Label(rootE, text="Имя сотрудника")
    l2.place(x=10,y=90)
    t2 = tkinter.Entry(rootE, borderwidth=1, relief="solid")
    t2.place(x=10, y=110)
    l3 = tkinter.Label(rootE, text="Пол")
    l3.place(x=10,y=130)
    r1 = tkinter.Radiobutton(rootE, text="Мужской", variable=var, value="Male")
    r1.place(x=10, y=150)
    r2 = tkinter.Radiobutton(rootE, text="Женский", variable=var, value="Female")
    r2.place(x=90, y=150)
    l4 = tkinter.Label(rootE, text="Возраст")
    l4.place(x=10,y=170)
    t3=tkinter.Entry(rootE, borderwidth=1, relief="solid")
    t3.place(x=10,y=190)
    l5 = tkinter.Label(rootE, text="Должность сотрудника")
    l5.place(x=10,y=210)
    scrollbar = tkinter.Scrollbar(rootE, width=3)
    scrollbar.place(x=150, y=225)
    lb = tkinter.Listbox(rootE, selectmode='SINGLE', exportselection=0, height=1, width=20, borderwidth=1, relief="solid", yscrollcommand = scrollbar.set)
    lb.insert(tkinter.END, "Доктор")
    lb.insert(tkinter.END, "Мед работник")
    lb.insert(tkinter.END, "Помощник врача")
    lb.place(x=10, y=240)
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lb.yview)
    l6=tkinter.Label(rootE,text="Зарплата")
    l6.place(x=10,y=260)
    t4=tkinter.Entry(rootE, borderwidth=1, relief="solid")
    t4.place(x=10,y=280)
    l7 = tkinter.Label(rootE, text="Опыт работы")
    l7.place(x=10,y=300)
    t5 = tkinter.Entry(rootE, borderwidth=1, relief="solid")
    t5.place(x=10,y=320)
    l8 = tkinter.Label(rootE, text="Мобильный номер")
    l8.place(x=10,y=340)
    t6 = tkinter.Entry(rootE, borderwidth=1, relief="solid")
    t6.place(x=10,y=360)
    l9 = tkinter.Label(rootE, text="Email")
    l9.place(x=10,y=380)
    t7=tkinter.Entry(rootE, borderwidth=1, relief="solid")
    t7.place(x=10,y=400)
    b1=tkinter.Button(rootE,text="Сохранить", borderwidth=1, relief="solid",command=inp)
    b1.place(x=10,y=430)
    b2=tkinter.Button(rootE,text="Удалить", borderwidth=1, relief="solid",command=delo)
    b2.place(x=80,y=430)
    b3=tkinter.Button(rootE,text="Выйти", borderwidth=1, relief="solid",command=ex)
    b3.place(x=135,y=430)
    rootE.iconbitmap('assets/medical.ico')
    rootE.mainloop()

def delling():
    global d1,de
    de=str(d1.get())
    conn = sqlite3.connect("database/medDB.db")
    p = list(conn.execute("select * from employee where EMP_ID=?", (de,)))
    if (len(p) != 0):
        conn.execute("DELETE from employee where EMP_ID=?", (de,))
        dme = tkinter.Label(rootDE, text="Сотрудник успешно удален из базы", fg="green")
        dme.place(x=10, y=100)
        conn.commit()
    else:
        error = tkinter.Label(rootDE, text="Сотрудник не найден", fg="Red")
        error.place(x=10, y=100)

rootDE=None
def delo():
    global rootDE,d1
    rootDE=tkinter.Tk()
    rootDE.geometry("360x400")
    rootDE.title("Удаление сотрудника")
    h1=tkinter.Label(rootDE,text="Введите ID работника для удаления из базы", bg="#73ACDA", fg='white', font="Times 16 bold", padx=10)
    h1.place(x=-0,y=0)
    d1=tkinter.Entry(rootDE, borderwidth=1, relief="solid")
    d1.place(x=10,y=40)
    B1=tkinter.Button(rootDE,text="Удалить", borderwidth=1, relief="solid", command=delling)
    B1.place(x=10,y=70)
    rootDE.iconbitmap('assets/medical.ico')
    rootDE.mainloop()
