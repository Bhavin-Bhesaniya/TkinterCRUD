from tkinter import *
from tkinter import ttk

import UserDaoMain as u


def ShowStudent():
    record = u.ShowAll()
    for i, (Id, Name, Email, Cno, Pass, Gender, Course, Hobby) in enumerate(record, start=1):
        DispList.insert("", "end", values=(Id, Name, Email, Cno, Pass, Gender, Course, Hobby))


def AddStudent():
    nm = name.get()
    em = email.get()
    cn = cno.get()
    pw = pwd.get()
    gn = gender.get()
    cs = course.get()
    hb = hobby.get()
    u.AddStud(nm, em, cn, pw, gn, cs, hb)
    DispList.destroy()
    CreateTreeView()
    ShowStudent()
    ClearValue()


def UpdateStudent():
    i = id.get()
    nm = name.get()
    em = email.get()
    cn = cno.get()
    pw = pwd.get()
    gn = gender.get()
    cs = course.get()
    hb = hobby.get()
    u.UpdateStud(nm, em, cn, pw, gn, cs, hb, i)
    DispList.destroy()
    CreateTreeView()
    ShowStudent()
    ClearValue()


def DeleteStudent():
    i = id.get()
    u.DeleteStud(i)
    DispList.destroy()
    CreateTreeView()
    ShowStudent()
    ClearValue()


def ClearValue():
    id.set("")
    name.set("")
    email.set("")
    cno.set("")
    pwd.set("")
    cwd.set("")
    gender.set("")
    course.set("")
    hobby.set("")


def SetValue(event):
    row_id = DispList.selection()[0]
    select = DispList.set(row_id)
    id.set(str(select['Id']))
    name.set(str(select['Name']))
    email.set(str(select['Email']))
    cno.set(str(select['Cno']))
    pwd.set(str(select['Pass']))
    gender.set(str(select['Gender']))
    course.set(str(select['Course']))
    hobby.set(str(select['Hobby']))


root = Tk()
root.geometry('1200x700+150+50')

global id, name, email, cno, pwd, cwd, gender, course, hobby, DispList

id = StringVar()
name = StringVar()
email = StringVar()
cno = StringVar()
pwd = StringVar()
cwd = StringVar()
gender = StringVar()
course = StringVar()
hobby = StringVar()

Label(root, text="Student id").grid(row=1, column=1, padx=10, pady=10)
Label(root, text="Student name").grid(row=2, column=1, padx=10, pady=10)
Label(root, text="Student email").grid(row=3, column=1, padx=10, pady=10)
Label(root, text="Student cno").grid(row=4, column=1, padx=10, pady=10)
Label(root, text="Student password").grid(row=5, column=1, padx=10, pady=10)
Label(root, text="Student cpassword").grid(row=6, column=1, padx=10, pady=10)
Label(root, text="Student gender").grid(row=7, column=1, padx=10, pady=10)
Label(root, text="Student course").grid(row=8, column=1, padx=10, pady=10)
Label(root, text="Student hobby").grid(row=9, column=1, padx=10, pady=10)

Entry(root, textvariable=id).grid(row=1, column=2, padx=10, pady=10)
Entry(root, textvariable=name).grid(row=2, column=2, padx=10, pady=10)
Entry(root, textvariable=email).grid(row=3, column=2, padx=10, pady=10)
Entry(root, textvariable=cno).grid(row=4, column=2, padx=10, pady=10)
Entry(root, textvariable=pwd).grid(row=5, column=2, padx=10, pady=10)
Entry(root, textvariable=cwd).grid(row=6, column=2, padx=10, pady=10)
Entry(root, textvariable=gender).grid(row=7, column=2, padx=10, pady=10)
Entry(root, textvariable=course).grid(row=8, column=2, padx=10, pady=10)
Entry(root, textvariable=hobby).grid(row=9, column=2, padx=10, pady=10)

Button(root, text="Add", command=AddStudent).grid(row=12, column=1, padx=10, pady=10)
Button(root, text="Update", command=UpdateStudent).grid(row=12, column=2, padx=10, pady=10)
Button(root, text="Delete", command=DeleteStudent).grid(row=13, column=1, padx=10, pady=10)
Button(root, text="Clear", command=ClearValue).grid(row=13, column=2, padx=10, pady=10)


def CreateTreeView():
    global DispList
    cols = ['Id', 'Name', 'Email', 'Cno', 'Pass', 'Gender', 'Course', 'Hobby']
    DispList = ttk.Treeview(root, column=cols, show='headings', padding=5)
    DispList.column(0, width=20)
    DispList.column(1, width=50)
    DispList.column(2, width=50)
    DispList.column(3, width=50)

    for col in cols:
        DispList.heading(col, text=col)
        DispList.place(x=0, y=500)
    DispList.bind('<ButtonRelease-1>', SetValue)


u.CreateTable()
CreateTreeView()
ShowStudent()
root.mainloop()
