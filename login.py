import tkinter
from window2 import menu

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
    elif(S1=='1' and S2=='1'):
        menu()
    else:
        error=tkinter.Label(bottomframe,text="Неправильный ID или пароль \n Попробуйте снова",fg="red",font="bold")
        error.pack()


#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("1366x768")
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe=tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="Добро пожаловать",bg='white',fg='orange',font='Times 16 bold italic')
    username=tkinter.Label(topframe,text="Логин")
    userbox = tkinter.Entry(topframe)
    password=tkinter.Label(bottomframe,text="Пароль")
    passbox = tkinter.Entry(bottomframe,show="*")
    login = tkinter.Button(bottomframe, text="Авторизироваться", command=GET,font="arial 8 bold")
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("Авторизация в системе")
    root.mainloop()

Entry()

