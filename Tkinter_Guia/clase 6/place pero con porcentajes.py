import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo práctico de place")

ventana.geometry("300x300")
#con el relx se posiciona con porcentajes
#osea se posiciona dependiendo de las dimensiones de la pantalla

label1 = tk.Label(ventana, text="Label 1")
label1.place(relx=0.25, rely=0.25)

label2 = tk.Label(ventana, text="Label 2")
label2.place(relx=0.95, rely=0.95)

ventana.mainloop()