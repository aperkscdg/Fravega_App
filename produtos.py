import tkinter as tk
from CTkMessagebox import CTkMessagebox

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
    def __init__(self, nombre, costo_compra, costo_venta, cantidad_stock): # Inicializa los atributos del producto
        self.nombre = nombre #
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
        
        if nombre and costo_compra and costo_venta and cantidad_stock: # Verifica que todos los campos estén completos
            producto = Producto(nombre, costo_compra, costo_venta, cantidad_stock) # Crea una instancia de Producto para que? se agregue a la lista
            box.insert(tk.END, str(producto)) # Agrega el producto a la lista
            # Limpia las entradas para que el usuario pueda agregar otro producto
            for entrada in entradas: # Limpia cada entrada
                entrada.delete(0, tk.END) # Limpia el contenido de la entrada
            entradas[0].focus() # Enfoca la primera entrada para facilitar la adición de nuevos productos por
        else:                           
            CTkMessagebox(title="Error", message="Por favor, complete todos los campos.", icon="cancel", option_1="Aceptar")
        
boton.config(command=Producto.agregar_producto)









ventana.mainloop()