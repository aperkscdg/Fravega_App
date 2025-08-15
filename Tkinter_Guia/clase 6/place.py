import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de place")

# Creamos dos labels y los posicionamos con place
label1 = tk.Label(ventana, text="Label 1")
label1.place(x=50, y=50)

label2 = tk.Label(ventana, text="Label 2")
label2.place(x=100, y=100)

#con el place x , y asignamos en donde queremos que esten en terminos
#de pixeles los objetos


ventana.mainloop()