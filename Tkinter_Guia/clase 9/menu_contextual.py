import tkinter as tk

ventana = tk.Tk()

def mostrar_menu_contextual(event):
    menu_contextual.post(event.x_root, event.y_root)

menu_contextual = tk.Menu(ventana, tearoff=0)  # Crea un menú contextual sin separación
menu_contextual.add_command(label="Opción 1")  # Añade una opción al menú contextual
menu_contextual.add_command(label="Opción 2")  # Añade otra opción al menú contextual    

ventana.bind("<Button-3>", mostrar_menu_contextual)  # Asocia el botón derecho del ratón al menú contextual

ventana.mainloop()