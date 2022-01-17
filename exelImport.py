from os import popen

from pyodbc import Error
from excelRead import ExcelBook
from db import SQLserver


df = ExcelBook.book
cnxn = SQLserver.cnxn
cursor = SQLserver.cnxn.cursor()


try:
        cursor.execute(""" CREATE TABLE ##NombreCompleto (nombre VARCHAR(25), apellido VARCHAR(25), apellido2 VARCHAR(25))""")
        print("*" * 15)
        print("table created")
        data = [[]]
        
        for index, row in df.iterrows():
                        data.append([row.nombre,row.apellido, row.apellido2])
        Nrow = len(data)
        print("*" * 15)
        print("row saved:")
        print(Nrow -1)
        print("*" * 15)
        for i in range(Nrow -1):
                i =  i + 1
                #print(data[i][1])
                tablespopulated = cursor.execute("""
                Insert into ##NombreCompleto (nombre, apellido, apellido2) values(?,?,?)""",(data[i][0],data[i][1],data[i][2]))
                                        

        cursor.commit()
        cnxn.close()
        print("Table populated" )
        print("*" * 15)
        print("Enter any key to finish")
        input()
except(RuntimeError, TypeError, NameError):
        print("query fail", RuntimeError, TypeError, NameError)