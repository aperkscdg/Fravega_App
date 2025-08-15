import tkinter as tk

ventana = tk.Tk()

barra_menu = tk.Menu(ventana)  # Crea una barra de menú
ventana.config(menu=barra_menu)  # Asocia la barra de menú a la ventana

archivo_menu = tk.Menu(barra_menu)  # Crea un submenú para "Archivo"
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)

archivo_menu.add_command(label="Nuevo") # Añade un comando al submenú "Archivo"
archivo_menu.add_command(label="Abrir") #añade otro comando al submenú "Archivo"
archivo_menu.add_command() #separador
archivo_menu.add_command(label="Guardar") #añade otro comando al submenú "Archivo"

editar_menu = tk.Menu(barra_menu)  # Crea un submenú para "Editar"
barra_menu.add_cascade(label="Editar", menu=editar_menu)

editar_menu.add_command(label="Deshacer")  # Añade un comando al submenú "Editar"
editar_menu.add_command(label="Rehacer")  # Añade otro comando al submenú "Editar"









ventana.mainloop()