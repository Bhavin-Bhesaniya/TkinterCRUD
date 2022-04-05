import sqlite3

con = sqlite3.connect("bhavin.db")


def CreateTable():
    try:
        con.execute("create table if not exists stud(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "name varchar(20),"
                    "email varchar(20),"
                    "cno varchar(20),"
                    "pass varchar(20),"
                    "gender varchar(20),"
                    "course varchar(20),"
                    "hobby varchar(20))")
        con.commit()
    except Exception as e:
        print(e)


def AddStud(name, email, cno, password, gender, course, hobby):
    try:
        data = (name, email, cno, password, gender, course, hobby)
        con.execute("insert into stud(name,email,cno,pass,gender,course,hobby) values(?,?,?,?,?,?,?)", data)
        con.commit()
        print("Inserted")
    except Exception as e:
        print(e)


def UpdateStud(name, email, cno, password, gender, course, hobby, idu):
    try:
        data = (name, email, cno, password, gender, course, hobby, idu)
        con.execute("update stud set name=?,email=?,cno=?,pass=?,gender=?,course=?,hobby=? where id = ?", data)
        con.commit()
        print("Updated")
    except Exception as e:
        print(e)


def DeleteStud(id):
    try:
        data = (id)
        con.execute("delete from stud where id =?", data)
        con.commit()
        print("Deleted")
    except Exception as e:
        print(e)

def ShowAll():
    cur = con.execute("select * from stud")
    data = cur.fetchall()
    return data
