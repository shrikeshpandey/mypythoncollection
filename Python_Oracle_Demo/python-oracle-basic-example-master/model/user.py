class user:

    def __init__(self, ID_USUARIO, USUARIO, CLAVE, FECHA_CREACION):
        self.id_usuario=ID_USUARIO
        self.usuario=USUARIO
        self.clave=CLAVE
        self.fecha_creacion=FECHA_CREACION

    def getUsuario(self):
        return self.usuario
    
    def getClave(self):
        return self.clave
    

