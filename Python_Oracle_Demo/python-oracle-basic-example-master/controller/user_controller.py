import cx_Oracle
from conection.conect import connect
from model.user import user

class user_controller:

    #-------------------------------------------------find the user in the database
    def start_session(usuario, clave):
        try:
            connection=connect("invated", "invated")
            con = connection.return_conection()          
            cur=con.cursor()
            user={'usuario':usuario,
                  'clave':clave
                  }
            statement="select * from usuario where usuario=:usuario and clave=:clave"
            cur.execute(statement,user)
            con.commit()
            users=[]
            for result in cur:
                print("--------------------------------------------- Result: ", result)
                myUser={'id_usuario':result[0],
                        'usuario':result[1],
                        'clave':result[2],
                        'fecha':result[3]
                        }
                print('-------------------Usuario.fecha:',type(result[3]))
                users.append(myUser)
            
            print('---------------------------------------------- Users: ',users)
            if len(users)==1:
                print('-----------------------Users[Usuario][fecha]',users[0]['fecha'])
                if users[0]['usuario']==usuario and users[0]['clave']==clave:
                    
                    return users[0]
                else:
                    return None
            else:
                return None

                

        except Exception as ex:
            print('Exception Start Session:',ex)

    #-------------------------------------------------------Register(Sign up)
    def create_user(usuario,clave):
        try:
            connection=connect("invated", "invated")
            con = connection.return_conection()          
            cur=con.cursor()
            cur=con.cursor()
            user={
            'usuario':usuario,
            'clave':clave
            }

            statement="INSERT INTO usuario(id_usuario,usuario, clave) values(sec_usuario_id.nextval,:usuario,:clave)"
            cur.execute(statement,user)
            con.commit()
            return "User "+usuario+" Created Succesfully"
        except Exception as ex:
            print("create user Exception:" + str(ex))
            return "Error:"+str(ex)

        




