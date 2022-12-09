import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()
    
    def __init__(self, studentNumber, name, surname, birthdate, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        
    def saveStudent(self):
        sql = "INSERT INTO Student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES(%s, %s, %s, %s, %s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
        except mysql.connector.Error as err:
            print(err)
        finally:
            Student.connection.close()
            
    @staticmethod()
    def saveStudents(studentsList):
        sql = "INSERT INTO Student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES(%s, %s, %s, %s, %s)"
        values = studentsList
        Student.mycursor.execute(sql,values)
        try:
            Student.connection.commit()
        except mysql.connector.Error as err:
            print(err)
        finally:
            Student.connection.close()
        
        
studentsList = [
        ("201", "Ali", "Candan", datetime(2001, 5, 11), "E"),
        ("202", "Kenan", "Işık", datetime(2001, 1, 3), "E"),
        ("203", "Ceren", "Uslu", datetime(2000, 4, 8), "K"),
        ("204", "Ebru", "Başar", datetime(2001, 2, 6), "K"),
        ("205", "Zeynep", "Büyük", datetime(2001, 7, 12), "K"),
    ]

Student.saveStudents(studentsList)
