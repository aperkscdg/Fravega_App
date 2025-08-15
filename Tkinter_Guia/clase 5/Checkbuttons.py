import tkinter as tk

ventana = tk.Tk()

check1_var = tk.BooleanVar()


def mostrar_seleccion():
    if check1_var.get():
        boton.config(state="normal")
    else:
        boton.config(state="disabled")

check1 = tk.Checkbutton(ventana, text="Opción 1", variable=check1_var, command=mostrar_seleccion)
check1.pack()
boton = tk.Button(ventana, text="Mostrar selección", state="disabled")
boton.pack()


ventana.mainloop()