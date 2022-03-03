class book:
    def __init__(self, ISBN, NOMBRE, CANTIDAD):
        self.isbn=ISBN
        self.nombre=NOMBRE
        self.cantidad=CANTIDAD
    
    def getisbn(self):
        return self.isbn

    def getnombre(self):
        return self.nombre

    def getcantidad(self):
        return self.cantidad

