__author__ = 'user'
import cx_Oracle
con = cx_Oracle.connect(user="pyora",password="pyora",dsn="localhost/ORCL19C")

cur = con.cursor()