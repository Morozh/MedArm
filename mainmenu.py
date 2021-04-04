import tkinter
import sqlite3
import tkinter.messagebox
from PATDELSU import P_display
from PATDELSU import D_display
from PATDELSU import P_UPDATE
from RooMT import Room_all
from BILLING import BILLING
from employee_reg import emp_screen
from appointment import appo

conn=sqlite3.connect("database/medDB.db")
print("Связь с БД установлена")

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None

#ВЫЙТИ ИЗ МЕНЮ
def ex():
    global root1
    root1.destroy()

#ОПЦИИ МЕНЮ
def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1 = tkinter.Tk()
    root1.geometry("1366x768")
    root1.title("Главное меню")
    m = tkinter.Label(root1,text="Главное меню",font='Times 24 bold',fg='#000')
    button1 = tkinter.Button(root1,text="1. Регистрация пациента",font='Times 18 bold',bg='#FFF',fg='#73ACDA', borderwidth=1, relief="solid",command=PAT)
    button2 = tkinter.Button(root1, text="2. Распределение комнат",font='Times 18 bold',bg='#FFF',fg='#73ACDA', borderwidth=1, relief="solid",command=Room_all)
    button3 = tkinter.Button(root1, text="3. Регистрация сотрудника",font='Times 18 bold',bg='#FFF',fg='#73ACDA', borderwidth=1, relief="solid",command=emp_screen)
    button4 = tkinter.Button(root1, text="4. Записаться на прием",font='Times 18 bold',bg='#FFF',fg='#73ACDA', borderwidth=1, relief="solid",command=appo)
    button5 = tkinter.Button(root1, text="5. Бухгалтерия",font='Times 18 bold',bg='#FFF',fg='#73ACDA', borderwidth=1, relief="solid",command=BILLING)
    button6 = tkinter.Button(root1, text="Выйти",font='Times 18 bold',bg='#FFF',fg='#73ACDA', borderwidth=1, relief="solid",command=ex)
    m.place(x=15,y=20)
    button1.pack(side=tkinter.TOP)
    button1.place(x=20,y=70)
    button2.pack(side=tkinter.TOP)
    button2.place(x=20,y=120)
    button3.pack(side=tkinter.TOP)
    button3.place(x=20,y=170)
    button4.pack(side=tkinter.TOP)
    button4.place(x=20, y=220)
    button5.pack(side=tkinter.TOP)
    button5.place(x=20,y=270)
    button6.pack(side=tkinter.TOP)
    button6.place(x=20,y=320)

    root1.iconbitmap('assets/medical.ico')
    root1.mainloop()

p=None
#ФОРМА РЕГИСТРАЦИИ ПАЦИЕНТА
def IN_PAT():
    global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1,conn
    conn=sqlite3.connect("database/medDB.db")
    conn.cursor()
    pp1=pat_ID.get()
    pp2=pat_name.get()
    pp3=pat_sex.get()
    pp4=pat_BG.get()
    pp5=pat_dob.get()
    pp6=pat_contact.get()
    pp7=pat_contactalt.get()
    pp8=pat_address.get()
    pp9=pat_CT.get()
    pp10=pat_email.get()
    conn.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)',(pp1,pp2,pp3,pp4,pp5,pp8,pp9,pp10,))
    conn.execute('INSERT INTO CONTACT_NO VALUES (?,?,?)',(pp1,pp6,pp7,))
    tkinter.messagebox.showinfo("medARM ЛИС система","Данные добавлены в систему")
    conn.commit()


#ВЫЙТИ ИЗ ФОРМЫ ПАЦИЕНТА
def EXO():
    rootp.destroy()

def nothing():
    print("Связь с базой данных установлена ")

def nothing1():
    print("medARM. Сделано в ПКС 17/18")

#ФОРМА ПАЦИЕНТА
back=None
SEARCH=None
DELETE=None
UPDATE=None

def PAT():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootp,regform,id,name,dob,sex,email,ct,addr,c1,c2,bg,SUBMIT,menubar,filemenu,back,SEARCH,DELETE,UPDATE
    rootp=tkinter.Tk()
    rootp.title("Новый пациент")
    menubar=tkinter.Menu(rootp)
    filemenu=tkinter.Menu(menubar,tearoff=0)
    filemenu.add_command(label="Добавить",command=PAT)
    filemenu.add_separator()
    filemenu.add_command(label="Выйти", command=EXO)
    helpmenu=tkinter.Menu(menubar,tearoff=0)
    helpmenu.add_command(label="Помощь",command=nothing)
    helpmenu.add_command(label="Подробнее",command=nothing1)
    menubar.add_cascade(label="Файл", menu=filemenu)
    menubar.add_cascade(label="Помощь", menu=helpmenu)
    rootp.config(menu=menubar)
    regform=tkinter.Label(rootp,text="Новый пациент",bg="#73ACDA", fg='white', font="Times 16 bold")
    id=tkinter.Label(rootp,text="ID пациента")
    pat_ID=tkinter.Entry(rootp, borderwidth=1, relief="solid")
    name=tkinter.Label(rootp,text="Имя пациента")
    pat_name = tkinter.Entry(rootp, borderwidth=1, relief="solid")
    sex=tkinter.Label(rootp,text="Пол")
    pat_sex=tkinter.Entry(rootp, borderwidth=1, relief="solid")
    dob=tkinter.Label(rootp, text="Дата рождения (ГГГГ-ММ-ДД)")
    pat_dob=tkinter.Entry(rootp, borderwidth=1, relief="solid")
    bg=tkinter.Label(rootp, text="Группа крови",)
    pat_BG=tkinter.Entry(rootp, borderwidth=1, relief="solid")
    c1=tkinter.Label(rootp, text="Контактный номер")
    pat_contact=tkinter.Entry(rootp, borderwidth=1, relief="solid")
    c2=tkinter.Label(rootp, text="Дополнительный номер")
    pat_contactalt=tkinter.Entry(rootp, borderwidth=1, relief="solid")
    email=tkinter.Label(rootp, text="Email")
    pat_email = tkinter.Entry(rootp, borderwidth=1, relief="solid")
    ct=tkinter.Label(rootp,text="Ведущий врач")
    pat_CT=tkinter.Entry(rootp, borderwidth=1, relief="solid")
    addr=tkinter.Label(rootp, text="Адресс")
    pat_address=tkinter.Entry(rootp, borderwidth=1, relief="solid")
    back=tkinter.Button(rootp,text="Назад", borderwidth=1, relief="solid",command=menu)
    SEARCH=tkinter.Button(rootp,text="Поиск", borderwidth=1, relief="solid",command=P_display)
    DELETE=tkinter.Button(rootp,text="Удалить", borderwidth=1, relief="solid",command=D_display)
    UPDATE=tkinter.Button(rootp,text="Обновить", borderwidth=1, relief="solid",command=P_UPDATE)
    SUBMIT=tkinter.Button(rootp,text="Подтвердить", borderwidth=1, relief="solid",command=IN_PAT,)
    regform.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_name.pack()
    sex.pack()
    pat_sex.pack()
    dob.pack()
    pat_dob.pack()
    bg.pack()
    pat_BG.pack()
    c1.pack()
    pat_contact.pack()
    c2.pack()
    pat_contactalt.pack()
    email.pack()
    pat_email.pack()
    ct.pack()
    pat_CT.pack()
    addr.pack()
    pat_address.pack()
    SUBMIT.pack(pady=10)
    back.pack(side=tkinter.LEFT, padx=(0, 10))
    UPDATE.pack(side=tkinter.LEFT, padx=(0, 10))
    DELETE.pack(side=tkinter.LEFT, padx=(0, 10))
    SEARCH.pack(side=tkinter.LEFT, pady=10)
    rootp.iconbitmap('assets/medical.ico')
    rootp.mainloop()
