import tkinter
from mainmenu import menu

#root=login page
#root1=menu
#rootp=patient form

#variables
root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None
#command for login button
def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='Admin' and S2=='1234'):
        menu()
    elif(S1=='' and S2==''):
        menu()
    else:
        error=tkinter.Label(bottomframe,text="Неправильный ID или пароль \n Попробуйте снова",fg="red",font="bold")
        error.pack()


#АВТОРИЗАЦИЯ
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("430x320")
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe=tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="Лабораторная информационная система \n medARM.", fg="#FFF",font='Times 16 bold', bg="#73ACDA", padx=20, pady=10)
    username = tkinter.Label(topframe,text="Логин", fg='#73ACDA', font="arial 14 normal", padx=20, pady=10)
    userbox = tkinter.Entry(topframe, show="*", borderwidth=1, relief="solid")
    password = tkinter.Label(bottomframe, text="Пароль", fg='#73ACDA', font="arial 14 normal", padx=20, pady=10)
    passbox = tkinter.Entry(bottomframe, show="*", borderwidth=1, relief="solid")
    login = tkinter.Button(bottomframe, text="Авторизироваться", command=GET, font="arial 14 normal", fg='#73ACDA', borderwidth=1, relief="solid")
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack(pady=20)
    root.title("Авторизация в системе")
    root.mainloop()

Entry()

