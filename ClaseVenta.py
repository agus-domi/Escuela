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

class Carrito:
    def __init__(self):
        self.productos = []
        self.total = 0.0

    def agregarProducto(self, producto, cantidad):
        if not producto.reducirStock(cantidad):
            return producto.stock  # Retorna el stock disponible si no se puede agregar
        for fila in self.productos:
            if fila[0] is producto:
                fila[1] += cantidad
                self.total += producto.precio * cantidad
                return True
        self.productos.append([producto, cantidad])
        self.total += producto.precio * cantidad
        return True

    def eliminarProducto(self, producto):
        for fila in self.productos:
            if fila[0] is producto:
                producto.aumentarStock(fila[1])
                self.total -= producto.precio * fila[1]
                self.productos.remove(fila)
                return True
        return False

    def calcularTotal(self):
        return self.total

    def mostrarCarrito(self):
        resumen = {}
        for producto, cantidad in self.productos:
            resumen[producto.nombre] = {'precio': producto.precio, 'cantidad': cantidad}
        return resumen

# Ejemplo de uso
if __name__ == "__main__":
    p1 = Producto("Laptop", 1000, 5)
    p2 = Producto("Mouse", 50, 10)

    carrito = Carrito()
    carrito.agregarProducto(p1, 2)
    carrito.agregarProducto(p2, 3)

    print("Carrito:", carrito.mostrarCarrito())
    print("Total a pagar:", carrito.calcularTotal())

    carrito.eliminarProducto(p2)
    print("Carrito después de eliminar un Mouse:", carrito.mostrarCarrito())
    print("Total a pagar después de eliminar un Mouse:", carrito.calcularTotal())