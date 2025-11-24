class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def reducirStock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False
    
    def aumentarStock(self, cantidad):
        self.stock += cantidad
        return True


class Carrito:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto, cantidad):
        if not producto.reducirStock(cantidad):
            return False
        
        for fila in self.productos:
            if fila[0] is producto:
                fila[1] += cantidad
                return True
        
        self.productos.append([producto, cantidad])
        return True

    def eliminarProducto(self, nombreProducto):
        for fila in self.productos:
            producto, cantidad = fila
            if producto.nombre == nombreProducto:
                producto.aumentarStock(1)
                
                fila[1] -= 1
                if fila[1] == 0:
                    self.productos.remove(fila)

                return True
        return False

    def calcularTotal(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.productos)

    def mostrarCarrito(self):
        resumen = {}
        for producto, cantidad in self.productos:
            resumen[producto.nombre] = {
                'precio': producto.precio,
                'cantidad': cantidad,
                'subtotal': producto.precio * cantidad
            }
        return resumen

# Ejemplo de uso
p1 = Producto("Laptop", 1000, 5)
p2 = Producto("Mouse", 50, 10)

carrito = Carrito()
carrito.agregarProducto(p1, 2)
carrito.agregarProducto(p2, 3)

print("Carrito:", carrito.mostrarCarrito())
print("Total:", carrito.calcularTotal())

carrito.eliminarProducto("Mouse")
print("Carrito:", carrito.mostrarCarrito())
print("Total:", carrito.calcularTotal())