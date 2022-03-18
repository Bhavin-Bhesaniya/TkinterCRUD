from tkinter import messagebox
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="1234@", db="studentmaster")
conCursor = con.cursor()


def CreateTable():
    try:
        conCursor.execute("create table if not exists stud"
                          "(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                          "name varchar(20),"
                          "email varchar(20),"
                          "course varchar(20),"
                          "cno varchar(20),"
                          "city varchar(20),"
                          "hobby varchar(20),"
                          "gender varchar(20))")
        con.commit()
    except Exception as e:
        print(e)


def SaveUser(name, email, course, cno, city, hob3, gen):
    try:
        sql = "insert into stud(name,email,course,cno,city,hobby,gender) values(%s,%s,%s,%s,%s,%s,%s)"
        data = (name, email, course, cno, city, hob3, gen)
        conCursor.execute(sql, data)
        messagebox.showinfo("Information", "Student Added Successfully!!!")
        con.commit()
    except Exception as e:
        messagebox.showinfo("Alert", e)
        con.rollback()
        con.close()


def UpdateUser(name, email, course, cno, city, hob3, gen, id):
    try:
        sql = "update stud set name=%s,email=%s,course=%s,cno=%s,city=%s,hobby=%s,gender=%s where id=%s"
        data = (name, email, course, cno, city, hob3, gen, id)
        conCursor.execute(sql, data)
        messagebox.showinfo("Information", "Student Updated Successfully!!!")
        con.commit()
    except Exception as e:
        messagebox.showinfo("Alert", e)
        con.rollback()
        con.close()


def DeleteUser(id):
    try:
        sql = "delete from stud where id=%s"
        data = (id,)
        conCursor.execute(sql, data)
        messagebox.showinfo("Information", "Student Deleted Successfully!!!")
        con.commit()
    except Exception as e:
        messagebox.showinfo("Alert", e)
        con.rollback()
        con.close()


def GetAllStud():
    conCursor.execute("select * from stud")
    data = conCursor.fetchall()
    return data
