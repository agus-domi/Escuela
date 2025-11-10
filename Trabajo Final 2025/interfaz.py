import tkinter as tk
from tkinter import messagebox
from carrito import Carrito
from producto import Producto

# ------------------- FUNCIONES AUXILIARES -----------------------

def buscar(nombre):
    """Busca un producto por nombre en el depósito."""
    for p in deposito:
        if p.nombre.lower() == nombre.lower():
            return p
    return False

def actualizar_lista_productos():
    """Muestra los productos disponibles en la tienda."""
    lista_productos.delete(0, tk.END)
    for p in deposito:
        lista_productos.insert(
            tk.END, f"{p.nombre} - ${p.precio:.2f} | Stock: {p.stock}"
        )

def actualizar_lista_carrito():
    """Muestra los productos en el carrito."""
    lista_carrito.delete(0, tk.END)
    for i in range(len(carrito.productos)):
        nombre, precio, cantidad, subtotal = carrito.mostrarProducto(i)
        lista_carrito.insert(tk.END, f"{nombre} x{cantidad} - ${subtotal:.2f}")
    lbl_total.config(text=f"Total: ${carrito.total:.2f}")

def agregar_al_carrito():
    """Agrega el producto seleccionado al carrito."""
    seleccion = lista_productos.curselection()
    if not seleccion:
        messagebox.showwarning("Atención", "Seleccione un producto de la lista.")
        return

    indice = seleccion[0]
    producto = deposito[indice]

    try:
        cantidad = int(spin_cantidad.get())
    except ValueError:
        cantidad = 1

    resultado = carrito.agregarProducto(producto, cantidad)
    if resultado is True:
        messagebox.showinfo("Agregado", f"Se agregó {cantidad} {producto.nombre} al carrito.")
    else:
        messagebox.showwarning("Stock insuficiente", f"Solo hay {resultado} en stock.")

    actualizar_lista_productos()
    actualizar_lista_carrito()

def eliminar_item():
    """Elimina el producto seleccionado del carrito."""
    seleccion = lista_carrito.curselection()
    if not seleccion:
        messagebox.showwarning("Atención", "Seleccione un producto del carrito.")
        return

    indice = seleccion[0]
    producto, _ = carrito.productos[indice]
    carrito.eliminarProducto(producto)
    actualizar_lista_carrito()
    actualizar_lista_productos()

def vaciar_carrito():
    """Vacía completamente el carrito."""
    carrito.vaciarCarrito()
    actualizar_lista_carrito()
    actualizar_lista_productos()

def mostrar_carrito():
    """Cambia a la vista del carrito."""
    frame_tienda.pack_forget()
    frame_carrito.pack(fill="both", expand=True)
    actualizar_lista_carrito()

def mostrar_tienda():
    """Vuelve a la vista de la tienda."""
    frame_carrito.pack_forget()
    frame_tienda.pack(fill="both", expand=True)
    actualizar_lista_productos()

def agregar_producto():
    """Abre una ventana para agregar un nuevo producto al depósito."""
    def guardar_producto():
        nombre = entry_nombre.get()
        try:
            precio = float(entry_precio.get())
            cantidad = int(entry_cantidad.get())
            if nombre and precio >= 0 and cantidad >= 0:
                nuevo_producto = Producto(nombre, precio, cantidad)
                deposito.append(nuevo_producto)
                # Guardar en el archivo
                with open("productos.txt", "a", encoding="utf-8") as archivo:
                    archivo.write(f"\n{nombre};{precio};{cantidad}")
                messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado al depósito.")
                ventana_agregar.destroy()
                actualizar_lista_productos()
            else:
                messagebox.showwarning("Error", "Por favor complete todos los campos correctamente")
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser números válidos")

    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Producto")
    ventana_agregar.geometry("300x200")

    tk.Label(ventana_agregar, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(ventana_agregar)
    entry_nombre.pack(pady=5)

    tk.Label(ventana_agregar, text="Precio:").pack(pady=5)
    entry_precio = tk.Entry(ventana_agregar)
    entry_precio.pack(pady=5)

    tk.Label(ventana_agregar, text="Cantidad:").pack(pady=5)
    entry_cantidad = tk.Entry(ventana_agregar)
    entry_cantidad.pack(pady=5)

    tk.Button(ventana_agregar, text="Guardar", command=guardar_producto).pack(pady=10)

# -------------------------------------------------------------------------------------------------------
# Inicialización de Variables
carrito = Carrito()
deposito = []
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            partes = linea.split(";")
            nombre = partes[0]
            precio = float(partes[1])
            cantidad = int(partes[2])
            deposito.append(Producto(nombre, precio, cantidad))

# -------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title("Tienda y Carrito")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# -------------------- FRAME TIENDA ------------------------------------
frame_tienda = tk.Frame(root, bg="#ffffff")
frame_tienda.pack(fill="both", expand=True)

tk.Label(frame_tienda, text="🛍️ Tienda", font=("Arial", 24), bg="#ffffff").pack(pady=10)
lista_productos = tk.Listbox(frame_tienda, width=60, height=10, bg="#eaeaea", font=("Arial", 12))
lista_productos.pack(pady=10)

# Selector de cantidad
tk.Label(frame_tienda, text="Cantidad:", bg="#ffffff").pack()
spin_cantidad = tk.Spinbox(frame_tienda, from_=1, to=100, width=5, font=("Arial", 12))
spin_cantidad.pack(pady=5)

# Botones
tk.Button(frame_tienda, text="Agregar al carrito", command=agregar_al_carrito, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(frame_tienda, text="Ver carrito", command=mostrar_carrito, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(frame_tienda, text="Añadir Producto", command=agregar_producto, bg="#FFC107", fg="black", font=("Arial", 12)).pack(pady=5)

# -------------------- FRAME CARRITO ------------------------------------
frame_carrito = tk.Frame(root, bg="#ffffff")

tk.Label(frame_carrito, text="🛒 Carrito", font=("Arial", 24), bg="#ffffff").pack(pady=10)
lista_carrito = tk.Listbox(frame_carrito, width=60, height=10, bg="#eaeaea", font=("Arial", 12))
lista_carrito.pack(pady=10)

lbl_total = tk.Label(frame_carrito, text="Total: $0.00", font=("Arial", 16), bg="#ffffff")
lbl_total.pack(pady=10)

tk.Button(frame_carrito, text="Eliminar producto", command=eliminar_item, bg="#f44336", fg="white", font=("Arial", 12)).pack(pady=3)
tk.Button(frame_carrito, text="Vaciar carrito", command=vaciar_carrito, bg="#f44336", fg="white", font=("Arial", 12)).pack(pady=3)
tk.Button(frame_carrito, text="Volver a la tienda", command=mostrar_tienda, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=3)

# Inicializa la vista de la tienda
actualizar_lista_productos()

root.mainloop()