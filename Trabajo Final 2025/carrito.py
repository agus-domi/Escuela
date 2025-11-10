# Clase Carrito
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