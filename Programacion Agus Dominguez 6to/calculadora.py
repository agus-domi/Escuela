import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("260x430")
        self.root.resizable(False, False)
        
        self.root.configure(bg="#f0f0f0")

        self.expresion = ""

        # Pantalla
        self.display = tk.Entry(
            root, 
            font=("Arial", 20), 
            bd=5, 
            relief="ridge", 
            justify="right",
            bg="#ffffff"
        )
        self.display.pack(fill="both", padx=10, pady=10)

        # Frame para los botones
        frame = tk.Frame(root, bg="#f0f0f0")
        frame.pack()

        botones = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("C", 3, 2), ("+", 3, 3)
        ]

        for (texto, fila, columna) in botones:
            
            bg_color = "#fafafa"
            
            if texto in "/*-+":
                bg_color = "#d6eaf8"
            elif texto == "C":
                bg_color = "#ff4d4d"
            if texto == "C":
                cmd = self.borrar
            else:
                cmd = lambda t=texto: self.boton(t)

            b = tk.Button(
                frame,
                text=texto,
                font=("Arial", 16),
                width=4,
                height=2,
                bg=bg_color,
                fg="black",
                relief="groove",
                bd=2,
                command=cmd
            )
            b.grid(row=fila, column=columna, padx=3, pady=3)

        b_igual = tk.Button(
            frame,
            text="=",
            font=("Arial", 16),
            height=2,
            bg="#a9dfbf",
            fg="black",
            relief="groove",
            bd=2,
            command=self.calcular
        )

        b_igual.grid(row=4, column=0, columnspan=4, padx=3, pady=3, sticky="nsew")

    def boton(self, valor):
        self.expresion += str(valor)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expresion)

    def borrar(self):
        self.expresion = ""
        self.display.delete(0, tk.END)

    def calcular(self):
        try:
            resultado = eval(self.expresion)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, resultado)
            self.expresion = str(resultado)
        except:
            messagebox.showerror("Error", "Expresión inválida")
            self.borrar()


if __name__ == "__main__":
    root = tk.Tk()
    Calculadora(root)
    root.mainloop()