import pyodbc

class SQLserver:
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(LocalDb)\localdbDemo;DATABASE=onlytest;Trusted_Connection=yes;')        
        print("connection success!!")
    except:
        print("fail to connect")