import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from carrito import Carrito
from producto import Producto

# ------------------- FUNCIONES AUXILIARES -----------------------

def actualizar_tienda():
    for widget in frame_productos.winfo_children():
        widget.destroy()

    filas = 1
    columnas = 3

    for i, producto in enumerate(deposito):
        fila = i // columnas
        columna = i % columnas
        crear_card_producto(frame_productos, producto, fila, columna)

    frame_productos.update_idletasks()
    frame_productos.place(relx=0.5, rely=0.5, anchor="center")

def crear_card_producto(parent, producto, fila, columna):
    card = tk.Frame(parent, bg="white", bd=1, relief="solid")
    card.grid(row=fila, column=columna, padx=15, pady=15)

    try:
        imagen = Image.open(f"images/{producto.nombre.lower().replace(' ', '_')}.png")
        imagen = imagen.resize((130, 130))
        foto = ImageTk.PhotoImage(imagen)
    except:
        foto = None

    if foto:
        lbl_img = tk.Label(card, image=foto, bg="white")
        lbl_img.image = foto
        lbl_img.pack(pady=5)

    tk.Label(card, text=producto.nombre, bg="white", fg="#333333",
             font=("Segoe UI", 11, "bold")).pack()
    tk.Label(card, text=f"${producto.precio:.2f}", bg="white",
             fg="#00bcd4", font=("Segoe UI", 10, "bold")).pack(pady=3)

    cantidad_frame = tk.Frame(card, bg="white")
    cantidad_frame.pack(pady=3)

    cantidad = tk.IntVar(value=1)

    tk.Button(cantidad_frame, text="–", command=lambda: cantidad.set(max(1, cantidad.get() - 1)),
              bg="#ffb74d", fg="white", font=("Segoe UI", 9, "bold"),
              relief="flat", width=2).pack(side="left")

    tk.Label(cantidad_frame, textvariable=cantidad, bg="white",
             font=("Segoe UI", 10, "bold")).pack(side="left", padx=5)

    tk.Button(cantidad_frame, text="+", command=lambda: cantidad.set(cantidad.get() + 1),
              bg="#00bcd4", fg="white", font=("Segoe UI", 9, "bold"),
              relief="flat", width=2).pack(side="left")

    def agregar():
        cant = cantidad.get()
        resultado = carrito.agregarProducto(producto, cant)
        if resultado is True:
            messagebox.showinfo("Agregado", f"Se agregó {cant} {producto.nombre} al carrito.")
        else:
            if resultado <= 0:
                messagebox.showwarning("Sin stock", f"No hay stock disponible.")
            else:
                messagebox.showwarning("Stock limitado", f"Solo quedan {resultado} disponibles.")
        actualizar_tienda()

    tk.Button(card, text="🛒 Agregar al carrito", command=agregar,
              bg="#00bcd4", fg="white", relief="flat", cursor="hand2",
              font=("Segoe UI", 9, "bold"), width=20).pack(pady=5)

# ------------------- CARRITO -----------------------

def actualizar_carrito():
    for widget in carrito_items_frame.winfo_children():
        widget.destroy()

    if not carrito.productos:
        tk.Label(carrito_items_frame, text="🛍️ El carrito está vacío",
                 bg="#f4f6f8", fg="#888", font=("Segoe UI", 12, "italic")).pack(pady=30)
    else:
        for i, (producto, cantidad) in enumerate(carrito.productos):
            crear_card_carrito(carrito_items_frame, producto, cantidad)

    lbl_total.config(text=f"Total: ${carrito.total:.2f}")

def crear_card_carrito(parent, producto, cantidad):
    card = tk.Frame(parent, bg="white", relief="groove", bd=1)
    card.pack(pady=6, padx=15, fill="x")

    tk.Label(card, text=producto.nombre, bg="white", fg="#333",
             font=("Segoe UI", 11, "bold")).pack(side="left", padx=10)

    cantidad_var = tk.IntVar(value=cantidad)

    def sumar():
        if producto.stock > 0:
            carrito.agregarProducto(producto, 1)
            cantidad_var.set(cantidad_var.get() + 1)
            actualizar_carrito()

    def restar():
        if cantidad_var.get() > 1:
            carrito.eliminarProducto(producto)
            carrito.agregarProducto(producto, cantidad_var.get() - 1)
        else:
            carrito.eliminarProducto(producto)
        actualizar_carrito()

    control_frame = tk.Frame(card, bg="white")
    control_frame.pack(side="right", padx=10)

    tk.Button(control_frame, text="–", command=restar, bg="#ffb74d",
              fg="white", relief="flat", width=2).pack(side="left")
    tk.Label(control_frame, textvariable=cantidad_var, bg="white",
             font=("Segoe UI", 10, "bold"), width=3).pack(side="left")
    tk.Button(control_frame, text="+", command=sumar, bg="#00bcd4",
              fg="white", relief="flat", width=2).pack(side="left")

    tk.Button(control_frame, text="✖", command=lambda: eliminar_producto(producto),
              bg="#e53935", fg="white", relief="flat", width=2).pack(side="left", padx=5)

def eliminar_producto(producto):
    carrito.eliminarProducto(producto)
    actualizar_carrito()

def vaciar_carrito():
    carrito.vaciarCarrito()
    actualizar_carrito()
    actualizar_tienda()

def mostrar_carrito():
    frame_tienda.pack_forget()
    frame_carrito.pack(fill="both", expand=True)
    actualizar_carrito()

def mostrar_tienda():
    frame_carrito.pack_forget()
    frame_tienda.pack(fill="both", expand=True)
    actualizar_tienda()

# ------------------- INICIALIZACIÓN -----------------------
carrito = Carrito()
deposito = []
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, precio, stock = linea.strip().split(";")
        deposito.append(Producto(nombre, float(precio), int(stock)))

root = tk.Tk()
root.title("Tienda")
root.geometry("800x600")
root.configure(bg="#f4f6f8")

# ------------------- FRAME TIENDA -----------------------
frame_tienda = tk.Frame(root, bg="#f4f6f8")
frame_tienda.pack(fill="both", expand=True)

titulo = tk.Label(frame_tienda, text="Nuestros Productos",
                  bg="#f4f6f8", fg="#333333", font=("Segoe UI", 18, "bold"))
titulo.pack(pady=15)

frame_productos = tk.Frame(frame_tienda, bg="#f4f6f8")
frame_productos.pack(expand=True)

btn_carrito = tk.Button(frame_tienda, text="🧺 Ver carrito", command=mostrar_carrito,
                        bg="#00bcd4", fg="white", font=("Segoe UI", 11, "bold"),
                        relief="flat", cursor="hand2", width=15)
btn_carrito.pack(pady=20)

# ------------------- FRAME CARRITO -----------------------
frame_carrito = tk.Frame(root, bg="#f4f6f8")

tk.Label(frame_carrito, text="Tu Carrito",
         bg="#f4f6f8", fg="#333333", font=("Segoe UI", 18, "bold")).pack(pady=15)

carrito_items_frame = tk.Frame(frame_carrito, bg="#f4f6f8")
carrito_items_frame.pack(pady=10, fill="both", expand=True)

lbl_total = tk.Label(frame_carrito, text="Total: $0.00",
                     bg="#f4f6f8", fg="#333333", font=("Segoe UI", 14, "bold"))
lbl_total.pack(pady=10)

frame_botones = tk.Frame(frame_carrito, bg="#f4f6f8")
frame_botones.pack(pady=15)

tk.Button(frame_botones, text="⬅ Volver a tienda", command=mostrar_tienda,
          bg="#9e9e9e", fg="white", relief="flat", width=18, font=("Segoe UI", 10, "bold")).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="🗑 Vaciar carrito", command=vaciar_carrito,
          bg="#e53935", fg="white", relief="flat", width=18, font=("Segoe UI", 10, "bold")).grid(row=0, column=1, padx=5)

actualizar_tienda()
root.mainloop()
