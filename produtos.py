import tkinter as tk

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








ventana.mainloop()