import re
from tkinter import *
from tkinter import messagebox, ttk
import UserDao as user


def ClearField():
    u_id.set("")
    u_nm.set("")
    u_em.set("")
    u_cno.set("")
    u_city.set("Select Your City")
    sel_Course.current(0)
    chk1.deselect()
    chk2.deselect()
    rd1.select()
    rd2.deselect()


def ShowStudent():
    record = user.GetAllStud()
    for i, (Id, Name, Email, Contact_No, Course, City, Hobby, Gender) in enumerate(record, start=1):
        DispList.insert("", "end", values=(Id, Name, Email, Contact_No, Course, City, Hobby, Gender))


def AddStudent():
    name = u_nm.get()
    email = u_em.get()
    cno = u_cno.get()
    course = u_course.get()
    city = u_city.get()
    gen = u_gender.get()
    hob1 = u_hobby1.get()
    hob2 = u_hobby2.get()

    # Validation Check
    name_pat = re.compile(r"[A-Za-z]+")
    if re.fullmatch(name_pat, name):
        v_name = name
    else:
        messagebox.showerror("Validation", "InValid Name")

    email_pat = re.compile(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
    if re.fullmatch(email_pat, email):
        v_email = email
    else:
        messagebox.showerror("Validation", "InValid Email")

    contact_pat = re.compile(r"[0-9]{10}")
    if re.fullmatch(contact_pat, cno):
        v_cno = cno
    else:
        messagebox.showerror("Validation", "InValid Contact No")

    if hob1 == "Cricket" and hob2 == "Football":
        hob3 = hob1 + " | " + hob2
    elif hob1 == "Cricket" and hob2 == "":
        hob3 = hob1
    elif hob1 == "" and hob2 == "Football":
        hob3 = hob2
    elif hob1 == "" and hob2 == "":
        hob3 = ""

    if name == "" or email == "" or cno == "" or course == "Select Course" or city == "Select Your City" or gen == "" or hob3 == "":
        messagebox.showinfo("Required", "All Field Required ")
    else:
        user.SaveUser(v_name, v_email, v_cno, course, city, hob3, gen)
        ClearField()

    DispList.destroy()
    createTreeView()
    ShowStudent()


def UpdateStudent():
    id = u_id.get()
    name = u_nm.get()
    email = u_em.get()
    cno = u_cno.get()
    course = u_course.get()
    city = u_city.get()
    gen = u_gender.get()
    hob1 = u_hobby1.get()
    hob2 = u_hobby2.get()
    hob3 = ""

    # Validation Check
    name_pat = re.compile(r"[A-Za-z]+")
    if re.fullmatch(name_pat, name):
        v_name = name
    else:
        messagebox.showerror("Validation", "InValid Name")

    email_pat = re.compile(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
    if re.fullmatch(email_pat, email):
        v_email = email
    else:
        messagebox.showerror("Validation", "InValid Email")

    contact_pat = re.compile(r"[0-9]{10}")
    if re.fullmatch(contact_pat, cno):
        v_cno = cno
    else:
        messagebox.showerror("Validation", "InValid Contact No")

    if hob1 == "Cricket" and hob2 == "Football":
        hob3 = hob1 + " | " + hob2
    elif hob1 == "Cricket" and hob2 == "":
        hob3 = hob1
    elif hob1 == "" and hob2 == "Football":
        hob3 = hob2
    elif hob1 == "" and hob2 == "":
        hob3 = ""

    if name == "" or email == "" or cno == "" or course == "Select Course" or city == "Select Your City" or gen == "" or hob3 == "":
        messagebox.showinfo("Required", "All Field Required ")
    else:
        user.UpdateUser(v_name, v_email, v_cno, course, city, hob3, gen, id)
        ClearField()

    DispList.destroy()
    createTreeView()
    ShowStudent()


def DeleteStudent():
    id = u_id.get()
    if id == "":
        messagebox.showerror("Required", "Id must Required ")
    else:
        user.DeleteUser(id)
    ClearField()
    DispList.destroy()
    createTreeView()
    ShowStudent()


def SetValueFromList(event):
    ClearField()
    row_id = DispList.selection()[0]
    select = DispList.set(row_id)
    u_id.set(str(select['Id']))
    u_nm.set(str(select['Name']))
    u_em.set(str(select['Email']))
    u_cno.set(str(select['Contact_No']))
    sel_Course.set(str(select['Course']))
    u_city.set(select['City'])
    u_hobby1.set(str(select['Hobby']))
    # u_hobby2.set(str(select['Hobby']))
    u_gender.set(str(select['Gender']))


root = Tk()
root.geometry('800x700+300+50')

global u_id, u_nm, u_em, u_cno, u_course, u_city, u_hobby1, u_hobby2, u_gender

u_id = StringVar()
u_nm = StringVar()
u_em = StringVar()
u_cno = StringVar()
u_course = StringVar()
u_city = StringVar()
u_hobby1 = StringVar()
u_hobby2 = StringVar()
u_gender = StringVar()

Label(root, text="Student ID").grid(row=4, column=3, padx=10, pady=10)
Label(root, text="Student Name").grid(row=5, column=3, padx=10, pady=10)
Label(root, text="Email").grid(row=6, column=3, padx=10, pady=10)
Label(root, text="Contact No").grid(row=7, column=3, padx=10, pady=10)
Label(root, text="Course").grid(row=8, column=3, padx=10, pady=10)
Label(root, text="City").grid(row=9, column=3, padx=10, pady=10)
Label(root, text="Hobby").grid(row=10, column=3, padx=10, pady=10)
Label(root, text="Gender").grid(row=11, column=3, padx=10, pady=10)

Entry(root, textvariable=u_id).grid(row=4, column=5, padx=10, pady=10)
Entry(root, textvariable=u_nm).grid(row=5, column=5, padx=10, pady=10)
Entry(root, textvariable=u_em).grid(row=6, column=5, padx=10, pady=10)
Entry(root, textvariable=u_cno).grid(row=7, column=5, padx=10, pady=10)

# Select Course Combobox
sel_Course = ttk.Combobox(root, state='readonly', textvariable=u_course)
sel_Course["values"] = ("Select Course", "BCA", "BscIT", "BTech")
sel_Course.grid(row=8, column=5, padx=10, pady=10)
sel_Course.current(0)

# Select City Value Here
city = ["Junagadh", "Rajkot", "Bhavnagar"]
u_city.set("Select Your City")
OptionMenu(root, u_city, *city).grid(row=9, column=5, padx=10, pady=10)

# CheckButton
chk1 = Checkbutton(root, text='Cricket', variable=u_hobby1, onvalue='Cricket', offvalue="")
chk1.grid(row=10, column=5, pady=10)
chk1.deselect()

chk2 = Checkbutton(root, text='Football', variable=u_hobby2, onvalue='Football', offvalue="")
chk2.grid(row=10, column=6, pady=10)
chk2.deselect()

# RadioButton
rd1 = Radiobutton(root, value='Male', text='Male', variable=u_gender)
rd1.grid(row=11, column=5, padx=10, pady=10)
rd1.select()

rd2 = Radiobutton(root, value='FeMale', text='FeMale', variable=u_gender)
rd2.grid(row=11, column=6, padx=10, pady=10)

# Function Button
Button(root, text="Add", command=AddStudent, height=2, width=13).grid(row=14, column=3, padx=20, pady=10)
Button(root, text="Update", command=UpdateStudent, height=2, width=13).grid(row=14, column=5, padx=10, pady=10)
Button(root, text="Delete", command=DeleteStudent, height=2, width=13).grid(row=14, column=6, padx=10, pady=10)
Button(root, text="Clear", command=ClearField, height=2, width=13).grid(row=14, column=7, padx=20, pady=10)


def createTreeView():
    global DispList
    cols = ('Id', 'Name', 'Email', 'Contact_No', 'Course', 'City', 'Hobby', 'Gender')
    DispList = ttk.Treeview(root, columns=cols, show='headings', padding=5)
    DispList.column(0, width=2)
    DispList.column(1, width=75)
    DispList.column(2, width=120)
    DispList.column(3, width=75)
    DispList.column(4, width=75)
    DispList.column(5, width=80)
    DispList.column(6, width=100)
    DispList.column(7, width=80)

    for col in cols:
        DispList.heading(col, text=col)
        DispList.grid(row=1, column=1)
        # DispList.grid(row=16, column=7)
        DispList.place(x=30, y=450)
    DispList.bind('<ButtonRelease-1>', SetValueFromList)


createTreeView()
ShowStudent()
ClearField()
root.mainloop()
