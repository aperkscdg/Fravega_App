import tkinter as tk

ventana = tk.Tk()
variabledecontrol = tk.IntVar()

def opcion_seleccionada():
    color_opcion = variabledecontrol.get()  # Obtener el valor de la variable de control
    if color_opcion == 0:
        ventana.configure(bg="red")  
    elif color_opcion == 1:
        ventana.configure(bg="blue") 

opciones1 = tk.Radiobutton(ventana, text="opcion 1", value=1, command=opcion_seleccionada)
opciones2 = tk.Radiobutton(ventana, text="opcion 2", value=2, command=opcion_seleccionada)

opciones1.pack()
opciones2.pack()





ventana.mainloop()

