import cx_Oracle
from conection.conect import connect
from model.book import book

class book_controller:

    #------------------------------------------------------------Return all books
    def return_books():
        try:
            connection=connect("invated","invated")
            con=connection.return_conection()
            cur=con.cursor()
            statement_books="select * from libros"
            cur.execute(statement_books)
            con.commit()
            all_books=[]
            for row_book in cur:
                aux_book=book(row_book[0],row_book[1],row_book[2])
                all_books.append(aux_book)
            
            return all_books


        except Exception as ex:
            print("----------------------Exception Return Books: "+str(ex))
    
    #------------------------------------------------------find a book whit ISBN
    def return_a_book(isbn):
        try:
            connection=connect("invated","invated")
            con=connection.return_conection()
            cur=con.cursor()
            isbn_dic={"isbn":isbn}
            statement_search_book="select * from libros where ISBN=:isbn"
            cur.execute(statement_search_book,isbn_dic)

            book_found=cur.fetchone()
            
            print("-------------------------------BOOK found: ", book_found)
            return book_found



        except Exception as ex:
            print("---------------------------RETURN ONE BOOK:"+str(ex))