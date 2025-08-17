import tkinter as tk
ventana = tk.Tk()

texto = tk.Text(ventana)
#se importa la barra de scroll
scrollbar_vertical = tk.Scrollbar(ventana)
#se define en que lado quieres que este , y si es x o y
scrollbar_vertical.pack(side="right", fill="y")
#se define en donde quieres que este la barra y si se vera en x o y
scrollbar_vertical.config(command=texto.yview)
#sirve para que al soltar la barra se quede en el mismo lugar y se adapte al texto
texto.config(yscrollcommand=scrollbar_vertical.set)
texto.pack(side="left", fill="both", expand=True)

ventana.mainloop()