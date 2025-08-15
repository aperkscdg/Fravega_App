import tkinter as tk

ventana=tk.Tk()
ventana.title("ejemplo de grid")

#creamos dos labels y los posicionamos con grid

label1 = tk.Label(ventana, text="Celda 1,1")
label1.grid(row=0, column=0, padx=5, pady=5)

label2 = tk.Label(ventana, text="Celda 1,2")
label2.grid(row=0, column=1, padx=5, pady=5)

label3 = tk.Label(ventana, text="Celda 2,1")
label3.grid(row=1, column=0, padx=5, pady=5)

label4 = tk.Label(ventana, text="Celda 2,2")
label4.grid(row=1, column=1, padx=5, pady=5)

#columna=x , row=y, padx y pady son los espacios de pixeles entre uno y otro



ventana.mainloop()
