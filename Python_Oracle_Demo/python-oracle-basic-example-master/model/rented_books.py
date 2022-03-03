class rented_books:
    def __init__(self,ID_PEDIDO,ISBN,USUARIO_ID,CANTIDAD):
        self.id_pedido=ID_PEDIDO
        self.isbn=ISBN
        self.usuario_id=USUARIO_ID
        self.cantidad=CANTIDAD
    
    def getid_pedido(self):
        return self.id_pedido

    def getisbn(self):
        self.isbn
    
    def getusuario_id(self):
        self.usuario_id
    
    def getcantidad(self):
        self.cantidad
