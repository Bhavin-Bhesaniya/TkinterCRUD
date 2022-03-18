from tkinter import *
from tkinter import ttk, messagebox
import UserDao as user

user.CreateTable()


def ShowStudent():
    record = user.GetAllStud()
    for i, (Id, Name, Email, Contact_No, Course, City, Hobby, Gender) in enumerate(record, start=1):
        DispList.insert("", "end", values=(Id, Name, Email, Contact_No, Course, City, Hobby, Gender))


def AddStudent():
    name = u_name.get()
    email = u_email.get()
    course = sel_Course.get()
    cno = u_phone.get()
    City = selectCity.get()
    gen = u_gender.get()
    hob1 = sel_chk1.get()
    hob2 = sel_chk2.get()

    if hob1 == 1 or hob2 == 1:
        hob3 = str(hob1) + str(hob2)
    elif hob1 == 1 or hob2 == 0:
        hob3 = str(hob1)
    elif hob1 == 0 or hob2 == 1:
        hob3 = str(hob2)
    else:
        hob3 = str(hob2)
    messagebox.showinfo("Display", hob3)

    if len(name) == 0 or len(email) == 0 or len(course) == 0 or len(cno) == 0:
        messagebox.showinfo("Required", "All Field Required ")
    else:
        user.SaveUser(name, email, cno, course, City, hob3, gen)
    clearEntry()
    DispList.destroy()
    createTreeView()
    ShowStudent()


def UpdateStudent():
    id = u_id.get()
    name = u_name.get()
    email = u_email.get()
    cno = u_phone.get()
    course = sel_Course.get()
    City = selectCity.get()
    gen = u_gender.get()
    # hob1 = sel_chk1.get()
    # hob2 = sel_chk2.get()

    # if hob1 == 1 or hob2 == 1:
    #     hob3 = str(hob1) + str(hob2)
    # elif hob1 == 1 or hob2 == 0:
    #     hob3 = str(hob1)
    # elif hob1 == 0 or hob2 == 1:
    #     hob3 = str(hob2)
    # else:
    #     hob3 = str(hob2)
    hob3 = 786
    messagebox.showinfo("Display", hob3)

    if len(name) == 0 or len(email) == 0 or len(course) == 0 or len(cno) == 0 or len(City) == 0:
        messagebox.showinfo("Required", "All Field Required ")
    else:
        user.UpdateUser(name, email, cno, course, City, hob3, gen, id)
    clearEntry()
    DispList.destroy()
    createTreeView()
    ShowStudent()


def DeleteStudent():
    id = u_id.get()
    if len(id) == 0:
        messagebox.showerror("Required", "Id must Required ")
    else:
        user.DeleteUser(id)
    clearEntry()
    DispList.destroy()
    createTreeView()
    ShowStudent()


def clearEntry():
    u_id.delete(0, END)
    u_name.delete(0, END)
    u_email.delete(0, END)
    u_phone.delete(0, END)
    selectCity.set("Select Your City")
    chk1.deselect()
    chk2.deselect()
    rd1.select()
    rd2.deselect()
    sel_Course.current(0)


def SetValueFromList(event):
    clearEntry()
    row_id = DispList.selection()[0]
    select = DispList.set(row_id)
    u_id.insert(0, select['Id'])
    u_name.insert(0, select['Name'])
    u_email.insert(0, select['Email'])
    u_phone.insert(0, select['Contact_No'])
    sel_Course.set(str(select['Course']))
    selectCity.set(select['City'])
    sel_chk1.set(str(select['Hobby']))
    u_gender.set(str(select['Gender']))


def checkname(self, u_name):
    if u_name.isalumn():
        return True
    if u_name == '':
        return True
    else:
        messagebox.showerror('Invalid', 'Username is invalid' + u_name[-1])
        return False


root = Tk()
root.geometry("1200x1000")
root.title("Student Form")
global u_id, u_name, u_email, u_phone, \
    chk1, chk2, sel_chk1, sel_chk2, sel_Course, \
    rd1, rd2, u_gender, selectCity, data_id, lb1
u_id = IntVar()
u_name = StringVar()
u_email = StringVar()
u_phone = StringVar()
u_gender = StringVar()
sel_Course = StringVar()
selectCity = StringVar()
sel_chk1 = IntVar()
sel_chk2 = IntVar()

Label(root, text="Student ID").place(x=10, y=10)
Label(root, text="Student Name").place(x=10, y=40)
Label(root, text="Email").place(x=10, y=70)
Label(root, text="Contact No").place(x=10, y=100)
Label(root, text="Course").place(x=10, y=130)
Label(root, text="City").place(x=10, y=160)
Label(root, text="Hobby").place(x=10, y=190)
Label(root, text="Gender").place(x=10, y=220)

u_id = Entry(root)
u_id.place(x=140, y=10)

u_name = Entry(root)
u_name.place(x=140, y=40)

# valid_name = root.register(checkname(u_name))
# u_name.config(validate='key', validatecommand=(valid_name, '%P'))

u_email = Entry(root)
u_email.place(x=140, y=70)

u_phone = Entry(root)
u_phone.place(x=140, y=100)

sel_Course = ttk.Combobox(root, state='readonly', textvariable=sel_Course)
sel_Course["values"] = ("Select Course", "BCA", "BscIT", "BTech")
sel_Course.place(x=140, y=130)
sel_Course.current(0)

# Select City Value Here
city = ["Junagadh", "rajkot", "bhavanagar"]
selectCity.set("Select Your City")
OptionMenu(root, selectCity, *city).place(x=140, y=160)

chk1 = Checkbutton(root, variable=sel_chk1, text='Cricket', onvalue=1, offvalue=0)
chk1.place(x=140, y=190)

chk2 = Checkbutton(root, text='Football', variable=sel_chk2, onvalue=1, offvalue=0)
chk2.place(x=200, y=190)

rd1 = Radiobutton(root, value='Male', text='Male', variable=u_gender)
rd1.place(x=140, y=220)
rd1.select()

rd2 = Radiobutton(root, value='FeMale', text='FeMale', variable=u_gender)
rd2.place(x=190, y=220)

Button(root, text="Add", command=AddStudent, height=2, width=13).place(x=330, y=380)
Button(root, text="Update", command=UpdateStudent, height=2, width=13).place(x=440, y=380)
Button(root, text="Delete", command=DeleteStudent, height=2, width=13).place(x=550, y=380)
Button(root, text="Clear", command=clearEntry, height=2, width=13).place(x=660, y=380)


def createTreeView():
    global DispList
    cols = ('Id', 'Name', 'Email', 'Contact_No', 'Course', 'City', 'Hobby', 'Gender')
    DispList = ttk.Treeview(root, columns=cols, show='headings', padding=5)
    DispList.column(0, width=2)
    DispList.column(1, width=75)
    DispList.column(2, width=120)
    DispList.column(3, width=75)
    DispList.column(4, width=75)

    for col in cols:
        DispList.heading(col, text=col)
        DispList.grid(row=1, column=1)
        DispList.place(x=10, y=500)

    DispList.bind('<ButtonRelease-1>', SetValueFromList)


createTreeView()
ShowStudent()
root.mainloop()
