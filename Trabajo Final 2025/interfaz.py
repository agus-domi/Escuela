import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sv_ttk

from carrito import Carrito
from producto import Producto

# ------------------- FUNCIONES AUXILIARES -----------------------

def actualizar_tienda():
    for widget in frame_productos.winfo_children():
        widget.destroy()

    columnas = 3

    for i, producto in enumerate(deposito):
        fila = i // columnas
        columna = i % columnas
        crear_card_producto(frame_productos, producto, fila, columna)

def crear_card_producto(parent, producto, fila, columna):
    card = ttk.Frame(parent, padding=10, style="Card.TFrame")
    card.grid(row=fila, column=columna, padx=15, pady=15)

    try:
        imagen = Image.open(f"images/{producto.nombre.lower().replace(' ', '_')}.png")
        imagen = imagen.resize((130, 130))
        foto = ImageTk.PhotoImage(imagen)
    except:
        foto = None

    if foto:
        lbl_img = ttk.Label(card, image=foto)
        lbl_img.image = foto
        lbl_img.pack(pady=5)

    ttk.Label(card, text=producto.nombre, font=("Segoe UI", 11, "bold")).pack()
    ttk.Label(card, text=f"${producto.precio:.2f}",
              font=("Segoe UI", 10, "bold"), foreground="#4dd0e1").pack(pady=3)

    cantidad_frame = ttk.Frame(card)
    cantidad_frame.pack(pady=3)

    cantidad = tk.IntVar(value=1)

    ttk.Button(cantidad_frame, text="–",
               command=lambda: cantidad.set(max(1, cantidad.get() - 1)),
               width=3).pack(side="left")

    ttk.Label(cantidad_frame, textvariable=cantidad,
              font=("Segoe UI", 10, "bold")).pack(side="left", padx=5)

    ttk.Button(cantidad_frame, text="+",
               command=lambda: cantidad.set(cantidad.get() + 1),
               width=3).pack(side="left")

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

    ttk.Button(card, text="🛒 Agregar al carrito", command=agregar, width=20).pack(pady=5)

# ------------------- CARRITO -----------------------

def actualizar_carrito():
    for widget in carrito_items_frame.winfo_children():
        widget.destroy()

    if not carrito.productos:
        ttk.Label(carrito_items_frame, text="🛍️ El carrito está vacío",
                  font=("Segoe UI", 12, "italic")).pack(pady=30)
    else:
        for producto, cantidad in carrito.productos:
            crear_card_carrito(carrito_items_frame, producto, cantidad)

    lbl_total.config(text=f"Total: ${carrito.total:.2f}")

def crear_card_carrito(parent, producto, cantidad):
    card = ttk.Frame(parent, padding=10, style="Card.TFrame")
    card.pack(pady=6, padx=15, fill="x")

    ttk.Label(card, text=producto.nombre,
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

    control_frame = ttk.Frame(card)
    control_frame.pack(side="right", padx=10)

    ttk.Button(control_frame, text="–", command=restar, width=3).pack(side="left")
    ttk.Label(control_frame, textvariable=cantidad_var, width=3).pack(side="left")
    ttk.Button(control_frame, text="+", command=sumar, width=3).pack(side="left")

    ttk.Button(control_frame, text="✖",
               command=lambda: eliminar_producto(producto),
               width=3).pack(side="left", padx=5)

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

# ------------------- APLICAR TEMA OSCURO -----------------------
sv_ttk.set_theme("dark")   # ← ← ← MODO OSCURO

# ------------------- FRAME TIENDA -----------------------
frame_tienda = ttk.Frame(root)
frame_tienda.pack(fill="both", expand=True)

# ------------------- BANNER SUPERIOR -----------------------
banner = tk.Frame(frame_tienda, bg="#3b2fa3", height=70)  # color diferente al fondo
banner.pack(fill="x")

titulo = tk.Label(
    banner,
    text="🎮 GamerZone Store",
    bg="#3b2fa3",
    fg="white",
    font=("Segoe UI", 20, "bold")
)
titulo.pack(pady=15)

# -----------------------------------------------------------

frame_productos = ttk.Frame(frame_tienda)
frame_productos.pack(expand=True)

ttk.Button(frame_tienda, text="🧺 Ver carrito",
           command=mostrar_carrito, width=20).pack(pady=20)

# ------------------- FRAME CARRITO -----------------------
frame_carrito = ttk.Frame(root)

ttk.Label(frame_carrito, text="Tu Carrito",
          font=("Segoe UI", 18, "bold")).pack(pady=15)

carrito_items_frame = ttk.Frame(frame_carrito)
carrito_items_frame.pack(pady=10, fill="both", expand=True)

lbl_total = ttk.Label(frame_carrito, text="Total: $0.00",
                      font=("Segoe UI", 14, "bold"))
lbl_total.pack(pady=10)

frame_botones = ttk.Frame(frame_carrito)
frame_botones.pack(pady=15)

ttk.Button(frame_botones, text="⬅ Volver a tienda",
           command=mostrar_tienda, width=18).grid(row=0, column=0, padx=5)
ttk.Button(frame_botones, text="🗑 Vaciar carrito",
           command=vaciar_carrito, width=18).grid(row=0, column=1, padx=5)

actualizar_tienda()
root.mainloop()
