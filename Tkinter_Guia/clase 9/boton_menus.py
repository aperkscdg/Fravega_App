import tkinter as tk

ventana = tk.Tk()

menu_boton=tk.Menubutton(ventana, text="Opciones") #esto crea un botón de menú
menu_boton.pack()

menu = tk.Menu(menu_boton) #esto crea un menú que se asocia al botón de menú
menu_boton.config(menu=menu)

def abrir():
    print("Abrir")


menu.add_command(label="v1", command=abrir) #añade un comando al boton de menú al primero 
menu.add_command(label="v2")

ventana.mainloop()