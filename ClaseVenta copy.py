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
            if fila[0].nombre == producto.nombre:
                fila[1] += cantidad
                self.total += producto.precio * cantidad
                return True

        # Si no existe, agregar nueva fila [producto, cantidad]
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

        print(f"El producto '{producto.nombre}' no está en el carrito")
        return False

    def mostrarProducto(self, posicion):
        if posicion < 0 or posicion >= len(self.productos):
            return "Producto no existente"
        producto, cantidad = self.productos[posicion]
        return [producto.nombre, producto.precio, cantidad, producto.precio * cantidad]

    def vaciarCarrito(self):
        for fila in self.productos:
            producto, cantidad = fila
            producto.aumentarStock(cantidad)
        self.productos.clear()
        self.total = 0.0
        return True

# Ejemplo de uso
if __name__ == "__main__":
    p1 = Producto("Laptop", 1000, 5)
    p2 = Producto("Mouse", 50, 10)

    carrito = Carrito()
    carrito.agregarProducto(p1, 2)
    carrito.agregarProducto(p2, 3)
    print(carrito.mostrarProducto(0))  # Muestra detalles del primer producto en el carrito
    print(carrito.mostrarProducto(1))  # Muestra detalles del segundo producto
    carrito.eliminarProducto(p1)
    print(carrito.mostrarProducto(0))  # Muestra detalles del primer producto
    carrito.vaciarCarrito()
    print(carrito.mostrarProducto(0))  # Intenta mostrar un producto en un carrito vacío