import re
from tkinter import *
from tkinter import ttk, messagebox
import UserDB as user

user.CreateTable()


def ClearAllField():
    uid.set("")
    uname.set("")
    uemail.set("")
    ucourse.set("")
    uphone.set("")
    sel_course.current(0)
    ucity.set("Select Your City")
    chk1.deselect()
    chk2.deselect()
    rd2.deselect()


def ShowAllStud():
    record = user.ShowAllStudent()
    for i, (Id, Name, Email, PhoneNo, Course, City, Hobby, Gender) in enumerate(record, start=1):
        DispList.insert("", "end", values=(Id, Name, Email, PhoneNo, Course, City, Hobby, Gender))


def AddStud():
    name = uname.get()
    email = uemail.get()
    phone = uphone.get()
    course = ucourse.get()
    city = ucity.get()
    hobby1 = uhobby1.get()
    hobby2 = uhobby2.get()
    gender = ugender.get()

    if hobby1 == "Cricket" and hobby2 == "Football":
        hobby3 = hobby1 + "|" + hobby2
    elif hobby1 == "Cricket" and hobby2 == "":
        hobby3 = hobby1
    elif hobby1 == "" and hobby2 == "Football":
        hobby3 = hobby2
    elif hobby1 == "" and hobby2 == "":
        hobby3 = ""

    name_pat = re.compile(r'^[A-Za-z]+$')
    if re.fullmatch(name_pat, name):
        v_name = name
    else:
        messagebox.showerror("Error", "Invalid Name")

    email_pat = re.compile(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
    if re.fullmatch(email_pat, email):
        v_email = email
    else:
        messagebox.showerror("Error", "Invalid email")

    phone_pat = re.compile(r'^[0-9]{10}$')
    if re.fullmatch(phone_pat, phone):
        v_phone = phone
    else:
        messagebox.showerror("Error", "Invalid phone no")

    if name == "" or email == "" or phone == "" or course == "Select Course" or city == "Select Your City" or hobby3 == "" or gender == "":
        messagebox.showerror("Error", "All Field Required")
    else:
        user.AddStudent(v_name, v_email, v_phone, course, city, hobby3, gender)
        ClearAllField()

    DispList.destroy()
    DispRecordView()
    ShowAllStud()


def UpdateStud():
    id = uid.get()
    name = uname.get()
    email = uemail.get()
    phone = uphone.get()
    course = ucourse.get()
    city = ucity.get()
    hobby1 = uhobby1.get()
    hobby2 = uhobby2.get()
    gender = ugender.get()
    hobby3 = ""

    if hobby1 == "Cricket" and hobby2 == "Football":
        hobby3 = hobby1 + "|" + hobby2
    elif hobby1 == "Cricket" and hobby2 == "":
        hobby3 = hobby1
    elif hobby2 == "Football" and hobby1 == "":
        hobby3 = hobby2
    elif hobby1 == "" and hobby2 == "":
        hobby3 = ""

    name_pat = re.compile(r'^[A-Za-z]+$')
    if re.fullmatch(name_pat, name):
        v_name = name
    else:
        messagebox.showerror("Error", "Invalid Name")

    email_pat = re.compile(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
    if re.fullmatch(email_pat, email):
        v_email = email
    else:
        messagebox.showerror("Error", "Invalid email")

    phone_pat = re.compile(r'^[0-9]{10}$')
    if re.fullmatch(phone_pat, phone):
        v_phone = phone
    else:
        messagebox.showerror("Error", "Invalid phone no")

    if id == "" or name == "" or email == "" or phone == "" or course == "Select Course" or city == "Select Your City" or hobby3 == "" or gender == "":
        messagebox.showerror("Error", "All Field Required")
    else:
        user.UpdateStudent(v_name, v_email, v_phone, course, city, hobby3, gender, id)
        ClearAllField()
    DispList.destroy()
    DispRecordView()
    ShowAllStud()


def DeleteStudent():
    id = uid.get()
    if id == "":
        messagebox.showerror("Required", "Id must Required ")
    else:
        user.DeleteStudent(id)
    ClearAllField()
    DispList.destroy()
    DispRecordView()
    ShowAllStud()


def SetValueFromList(event):
    # ('Id', 'Name', 'Email', 'PhoneNo', 'Course', 'City', 'Hobby', 'Gender')
    ClearAllField()
    row_id = DispList.selection()[0]
    select = DispList.set(row_id)
    uid.set(str(select['Id']))
    uname.set(str(select['Name']))
    uemail.set(str(select['Email']))
    uphone.set(str(select['PhoneNo']))
    sel_course.set(str(select['Course']))
    ucity.set(str(select['City']))
    uhobby1.set(str(select['Hobby']))
    ugender.set(str(select['Gender']))


# Code Start From Here
root = Tk()
root.geometry("1000x700+200+50")

global uid, uname, uemail, uphone, ucourse, ucity, uhobby1, uhobby2, ugender, DispList

uid = StringVar()
uname = StringVar()
uemail = StringVar()
uphone = StringVar()
ucourse = StringVar()
ucity = StringVar()
uhobby1 = StringVar()
uhobby2 = StringVar()
ugender = StringVar()

# All Label
Label(root, text="Student Id").grid(row=1, column=1, padx=10, pady=10)
Label(root, text="Student Name").grid(row=2, column=1, padx=10, pady=10)
Label(root, text="Student Email").grid(row=3, column=1, padx=10, pady=10)
Label(root, text="Student phone").grid(row=4, column=1, padx=10, pady=10)
Label(root, text="Student Course").grid(row=5, column=1, padx=10, pady=10)
Label(root, text="Student City").grid(row=6, column=1, padx=10, pady=10)
Label(root, text="Student Hobby").grid(row=7, column=1, padx=10, pady=10)
Label(root, text="Student Gender").grid(row=8, column=1, padx=10, pady=10)

# All Widget
Entry(root, textvariable=uid).grid(row=1, column=2, padx=10, pady=10)
Entry(root, textvariable=uname).grid(row=2, column=2, padx=10, pady=10)
Entry(root, textvariable=uemail).grid(row=3, column=2, padx=10, pady=10)
Entry(root, textvariable=uphone).grid(row=4, column=2, padx=10, pady=10)

# ComboBox
sel_course = ttk.Combobox(root, textvariable=ucourse, state='readonly')
sel_course['values'] = ('Select Course', 'BCA', 'BscIT', 'BTech')
sel_course.grid(row=5, column=2, padx=10, pady=10)
sel_course.current(0)

# OptionBox
city = ["Junagadh", "Rajkot", "Ahmedabad"]
ucity.set("Select Your City")
OptionMenu(root, ucity, *city).grid(row=6, column=2, padx=10, pady=10)

# CheckBox Button
chk1 = Checkbutton(root, text='Cricket', variable=uhobby1, onvalue="Cricket", offvalue="")
chk1.grid(row=7, column=2, padx=10, pady=10)

chk2 = Checkbutton(root, text='Football', variable=uhobby2, onvalue="Football", offvalue="")
chk2.grid(row=7, column=3, padx=10, pady=10)

# Radio Button
rd1 = Radiobutton(root, variable=ugender, text="Male", value="Male")
rd1.grid(row=8, column=2, padx=10, pady=10)
rd1.select()

rd2 = Radiobutton(root, variable=ugender, text="Female", value="Female")
rd2.grid(row=8, column=3, padx=10, pady=10)

# All Button
Button(root, text="Add", command=AddStud, width=10).grid(row=10, column=1, padx=10, pady=10)
Button(root, text="Update", command=UpdateStud, width=10).grid(row=10, column=2, padx=10, pady=10)
Button(root, text="Delete", command=DeleteStudent, width=10).grid(row=11, column=1, padx=10, pady=10)
Button(root, text="Clear", command=ClearAllField, width=10).grid(row=11, column=2, padx=10, pady=10)


# Display Record Here
def DispRecordView():
    global DispList
    cols = ('Id', 'Name', 'Email', 'PhoneNo', 'Course', 'City', 'Hobby', 'Gender')
    DispList = ttk.Treeview(root, columns=cols, show='headings', padding=5)
    DispList.column(0, width=2)
    DispList.column(1, width=120)
    DispList.column(2, width=120)
    DispList.column(3, width=80)
    DispList.column(4, width=80)
    DispList.column(5, width=80)
    DispList.column(6, width=120)
    DispList.column(7, width=80)

    for col in cols:
        DispList.heading(col, text=col)
        DispList.place(x=0, y=450)
    DispList.bind('<ButtonRelease-1>', SetValueFromList)


ClearAllField()
DispRecordView()
ShowAllStud()
root.mainloop()
