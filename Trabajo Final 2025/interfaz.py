import tkinter as tk
from tkinter import messagebox
from carrito import Carrito
from producto import Producto

# ------------------- FUNCIONES AUXILIARES -----------------------

def buscar(nombre):
    for p in deposito:
        if p.nombre.lower() == nombre.lower():
            return p
    return False

def actualizar_lista_productos():
    lista_productos.delete(0, tk.END)
    for p in deposito:
        lista_productos.insert(
            tk.END, f"{p.nombre} - ${p.precio:.2f} | Stock: {p.stock}"
        )

def actualizar_lista_carrito():
    for widget in carrito_items_frame.winfo_children():
        widget.destroy()

    if not carrito.productos:
        tk.Label(
            carrito_items_frame,
            text="El carrito está vacío 🛒",
            font=("Segoe UI", 12, "italic"),
            fg="#999"
        ).pack(pady=30)
        lbl_total.config(text="Total: $0.00")
        return

    for i in range(len(carrito.productos)):
        nombre, precio, cantidad, subtotal = carrito.mostrarProducto(i)

        fila = tk.Frame(
            carrito_items_frame,
            bg="white",
            relief="groove",
            bd=1
        )
        fila.pack(pady=6, ipadx=10, ipady=6, anchor="center")

        tk.Label(
            fila,
            text=f"{nombre} ×{cantidad}  -  ${subtotal:.2f}",
            bg="white",
            font=("Segoe UI", 11)
        ).pack(side="left", padx=10)

        tk.Button(
            fila,
            text="✖",
            command=lambda idx=i: eliminar_item_index(idx),
            bg="#ff6b6b",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            activebackground="#ff8787",
            cursor="hand2",
            width=3,
            relief="flat"
        ).pack(side="right", padx=5)

    lbl_total.config(text=f"Total: ${carrito.total:.2f}")

def agregar_al_carrito():
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
        if resultado <= 0:
            messagebox.showwarning("Stock insuficiente", f"No hay stock de este producto.")
        else:
            messagebox.showwarning("Stock insuficiente", f"Solo hay {resultado} en stock.")

    actualizar_lista_productos()
    actualizar_lista_carrito()

def eliminar_item_index(indice):
    if indice < 0 or indice >= len(carrito.productos):
        messagebox.showwarning("Atención", "Producto no válido.")
        return
    producto, _ = carrito.productos[indice]
    carrito.eliminarProducto(producto)
    actualizar_lista_carrito()
    actualizar_lista_productos()

def vaciar_carrito():
    carrito.vaciarCarrito()
    actualizar_lista_carrito()
    actualizar_lista_productos()

def mostrar_carrito():
    frame_tienda.pack_forget()
    frame_carrito.pack(fill="both", expand=True)
    actualizar_lista_carrito()

def mostrar_tienda():
    frame_carrito.pack_forget()
    frame_tienda.pack(fill="both", expand=True)
    actualizar_lista_productos()

# -------------------------------------------------------------------------------------------------------
# CARGA DE PRODUCTOS
carrito = Carrito()
deposito = []
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            nombre, precio, cantidad = linea.split(";")
            deposito.append(Producto(nombre, float(precio), int(cantidad)))

# -------------------------------------------------------------------------------------------------------
# VENTANA PRINCIPAL
root = tk.Tk()
root.title("🛍️ Tienda Virtual")
root.geometry("640x450")
root.configure(bg="#f4f6f8")

# -------------------- FRAME TIENDA -------------------------------
frame_tienda = tk.Frame(root, bg="#f4f6f8")
frame_tienda.pack(fill="both", expand=True)

tk.Label(frame_tienda, text="🛒 Tienda", font=("Segoe UI", 20, "bold"), bg="#f4f6f8", fg="#333").pack(pady=10)

lista_productos = tk.Listbox(frame_tienda, width=55, height=10, font=("Segoe UI", 10))
lista_productos.pack(pady=5)

cantidad_frame = tk.Frame(frame_tienda, bg="#f4f6f8")
cantidad_frame.pack(pady=5)
tk.Label(cantidad_frame, text="Cantidad:", bg="#f4f6f8", font=("Segoe UI", 10)).pack(side="left")
spin_cantidad = tk.Spinbox(cantidad_frame, from_=1, to=100, width=5, font=("Segoe UI", 10))
spin_cantidad.pack(side="left", padx=5)

boton_frame = tk.Frame(frame_tienda, bg="#f4f6f8")
boton_frame.pack(pady=10)
tk.Button(boton_frame, text="🛒 Agregar al carrito", command=agregar_al_carrito, bg="#4CAF50", fg="white",
          font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", width=20).pack(pady=5)
tk.Button(boton_frame, text="🧺 Ver carrito", command=mostrar_carrito, bg="#2196F3", fg="white",
          font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", width=20).pack(pady=5)

# -------------------- FRAME CARRITO -------------------------------
frame_carrito = tk.Frame(root, bg="#f4f6f8")

tk.Label(frame_carrito, text="🧺 Tu Carrito", font=("Segoe UI", 20, "bold"), bg="#f4f6f8", fg="#333").pack(pady=10)

carrito_items_frame = tk.Frame(frame_carrito, bg="#f4f6f8")
carrito_items_frame.pack(pady=10)

lbl_total = tk.Label(frame_carrito, text="Total: $0.00", font=("Segoe UI", 14, "bold"), bg="#f4f6f8", fg="#444")
lbl_total.pack(pady=10)

btns_frame = tk.Frame(frame_carrito, bg="#f4f6f8")
btns_frame.pack(pady=10)

tk.Button(btns_frame, text="🗑 Vaciar carrito", command=vaciar_carrito, bg="#E53935", fg="white",
          font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", width=16).grid(row=0, column=0, padx=5)
tk.Button(btns_frame, text="⬅ Volver a tienda", command=mostrar_tienda, bg="#9E9E9E", fg="white",
          font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", width=16).grid(row=0, column=1, padx=5)

# Inicializa la vista
actualizar_lista_productos()
root.mainloop()
