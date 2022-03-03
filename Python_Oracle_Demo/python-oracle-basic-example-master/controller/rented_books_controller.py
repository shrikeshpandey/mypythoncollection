import cx_Oracle
from conection.conect import connect

class rented_books_controller:
    
    #------------------------------------------------------------- Method to rent a book
    def rentBook(isbn, usuario,cantidad):
        try:
            conection=connect("invated","invated")
            con=conection.return_conection()
            cursor=con.cursor()
            
            usuario_id=rented_books_controller.searchIdUser(usuario)
            print("---------------------------------------------Usuario ID rented book controller:", type(usuario_id))
            book_to_rent=(isbn, usuario_id, cantidad)
            verify_stock=rented_books_controller.func_verify_stock(isbn, cantidad)
            print(" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++rented book controller verify stock:",verify_stock)
           
            if not(verify_stock ==0):
                update_books_dict={'cantidad':verify_stock,'isbn':isbn}
                
                statement_update="update libros set cantidad=:cantidad where ISBN=:isbn"
                cursor.execute(statement_update, update_books_dict)
                con.commit()
                statement_insert_rent="insert into libros_pedido(id_pedido,ISBN, usuario_id, cantidad) values(seq_id_libros_pedido.nextval,:0,:1,:2)"
                cursor.execute(statement_insert_rent, book_to_rent) 
                con.commit() 
        
        
            return rented_books_controller.return_books(usuario_id)    
        except Exception as ex:
            return None
            print("-------------------------------------Exception rentBook: "+str(ex))

    #---------------------------------------------------------------------------Method for find user id whit the 'user'
    def searchIdUser(usuario):
        conection=connect("invated","invated")
        con=conection.return_conection()
        cursor=con.cursor()
                  
        usuario_dictionary={'usuario':usuario}
        
        statement_user="select * from usuario where usuario=:usuario"   
                
        cursor.execute(statement_user,usuario_dictionary)
        con.commit()
        usuario=cursor.fetchone()
        print("   ---------------------------------------------------------------------rented books controller-User returned",usuario)
        usuario_id=usuario[0]
        return usuario_id

        #-----------------------------------------------------------------------------Execute the oracle function for verify the stock of book
    def func_verify_stock(isbn,quantity):
        try:
            print("-----------------------------------------------------------Entering to func_Verify_Stock")
            conection=connect("invated","invated")
            con=conection.return_conection()
            cursor=con.cursor()
        
            returnFunctionValue=cursor.callfunc("func_verify_stock", cx_Oracle.NUMBER, [str(isbn), int(quantity)])
            con.commit()
            return returnFunctionValue
        except Exception as ex:
            print("-------------------------------------------Exception func_verify_stock: ", str(ex))
            return None
        
                
        #------------------------------------------------------------------------return books of a user
    def return_books(id_user):
        try:
            print("------------------------------------------return_book id_user:",id_user)
            connection=connect("invated","invated")
            con=connection.return_conection()
            cursor=con.cursor()
            user={"id_usuario":id_user}
            stmt_foundBoks="select nombre, libros_pedido.cantidad, usuario from libros, usuario, libros_pedido where libros_pedido.isbn=libros.isbn and libros_pedido.usuario_id=usuario.id_usuario and usuario_id=:id_usuario"
            cursor.execute(stmt_foundBoks,user)
            con.commit()
            books_user=cursor.fetchall()
            return books_user
        except Exception as ex:
            print("------------------------------------------Exception return_books:",str(ex))
            return None
        
        
         


        