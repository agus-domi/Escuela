class Producto:
    def __init__ (self,nombre,precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def reducirStock(self,cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False
    
    def aumentarStock(self,cantidad):
        self.stock += cantidad
        return True