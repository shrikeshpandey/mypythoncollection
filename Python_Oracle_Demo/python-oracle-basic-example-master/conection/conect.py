#os.chdir("C:\\Users\\RJ\\Downloads\\instantclient-basic-windows.x64-19.3.0.0.0dbru\\instantclient_19_3")
import cx_Oracle
class connect:
    #---------------------------------------------------Create Connection

    def __init__(self, USER, PASS):
        self.user=USER
        self.password=PASS
        try:
            dsn_tns=cx_Oracle.makedsn('localhost','1521', service_name='orcl19c')
            self.connection=cx_Oracle.connect(self.user, self.password, dsn_tns)
           
        except Exception as ex:
            print("construct error conect.py: " + str(ex))
    
    #-------------------------------------------------Return Connection
    def return_conection(self):
        try:
            return self.connection
        except Exception as ex:
            print("return conection error: " + str(ex))
            return None

if __name__ == "__main__":
    import sys