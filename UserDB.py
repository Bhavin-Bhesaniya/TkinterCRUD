import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(host='localhost', user='root', password='1234@', db="study")
conCursor = con.cursor()


def CreateTable():
    try:
        conCursor.execute(
            "create table if not exists stu"
            "(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,"
            "name varchar(20) NOT NULL,"
            "email varchar(20) NOT NULL,"
            "phone varchar(20) NOT NULL, "
            "course varchar(20) NOT NULL,"
            "city varchar(20) NOT NULL,"
            "hobby varchar(20) NOT NULL,"
            "gender varchar(20) NOT NULL)")

        con.commit()
    except Exception as e:
        messagebox.showerror("Error", e)
        con.rollback()
        con.close()


def AddStudent(name, email, phone, course, city, hobby, gender):
    try:
        sql = "insert into stu(name,email,phone,course,city,hobby,gender) values(%s,%s,%s,%s,%s,%s,%s)"
        data = (name, email, phone, course, city, hobby, gender)
        conCursor.execute(sql, data)
        messagebox.showinfo("Success", "Record Added Successfully")
        con.commit()

    except Exception as e:
        messagebox.showerror("Error", e)
        con.rollback()
        con.close()


def UpdateStudent(name, email, phone, course, city, hobby, gender, id):
    try:
        sql = "Update stu set name=%s, email=%s, phone=%s, course=%s, city=%s, hobby=%s,gender=%s where id=%s"
        data = (name, email, phone, course, city, hobby, gender, id)
        conCursor.execute(sql, data)
        messagebox.showinfo("Success", "Record Updated Successfully")
        con.commit()

    except Exception as e:
        messagebox.showerror("Error", e)
        con.rollback()
        con.close()


def DeleteStudent(id):
    try:
        sql = "Delete from stu where id=%s"
        data = (id,)
        conCursor.execute(sql, data)
        messagebox.showinfo("Success", "Student Deleted Successfully")
        con.commit()

    except Exception as e:
        messagebox.showerror("Error", e)
        con.rollback()
        con.close()


def ShowAllStudent():
    try:
        conCursor.execute("select * from stu")
        data = conCursor.fetchall()
        return data

    except Exception as e:
        messagebox.showerror("Error", e)
        con.rollback()
        con.close()
