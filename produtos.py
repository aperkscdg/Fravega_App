import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry("1280x720")

lista=["Nombre", "Costo de Compra"," Costo de Venta", "Cantidad en Stock"]


entradas = [tk.Entry(ventana) for i in range(4)]
for i, entrada in enumerate(entradas):
    entrada.grid(row=i, column=1, padx=80, pady=5)
    entrada.config(width=50)
etiquetas = [tk.Label(ventana, text=texto) for texto in lista]
for i, etiqueta in enumerate(etiquetas):    
    etiqueta.grid(row=i, column=0, padx=150, pady=5)
    etiqueta.config(font=("Arial", 12))

boton=tk.Button(ventana, text="agregar producto")
boton.grid(row=4, column=1, padx=80, pady=5)

box = tk.Listbox(ventana, width=100, height=20)
box.grid(row=6, column=1, columnspan=2, padx=80, pady=5)



class Producto: # Clase Producto que representa un producto con sus atributos y métodos
    def __init__(self, nombre="", costo_compra=0, costo_venta=0, cantidad_stock=0): # Inicializa los atributos del producto
        self.nombre = nombre 
        self.costo_compra = costo_compra
        self.costo_venta = costo_venta
        self.cantidad_stock = cantidad_stock

    
    def __str__(self):
        return f"{self.nombre} - {self.costo_compra} - {self.costo_venta} - {self.cantidad_stock}"  
    
    def agregar_producto():
        nombre = entradas[0].get() # Obtiene el nombre del producto
        costo_compra = entradas[1].get() # Obtiene el costo de compra
        costo_venta = entradas[2].get()  # Obtiene el costo de venta
        cantidad_stock = entradas[3].get() # Obtiene la cantidad en stock   
        if not costo_compra.isdigit() or not costo_venta.isdigit() or not cantidad_stock.isdigit():
            messagebox.showerror("Error de Formato", "Los campos de costo y cantidad deben ser números enteros.")   
        elif not nombre.isalpha():
            messagebox.showerror("Error de Formato", "El nombre del producto debe contener solo letras.")
        else:
            if nombre and costo_compra and costo_venta and cantidad_stock:
                producto = Producto(nombre, costo_compra, costo_venta, cantidad_stock)
                box.insert(tk.END, str(producto))
                for entrada in entradas:
                    entrada.delete(0, tk.END)
                entradas[0].focus()
        
boton.config(command=Producto.agregar_producto)









ventana.mainloop()