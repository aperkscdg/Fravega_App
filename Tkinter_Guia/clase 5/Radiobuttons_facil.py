import tkinter as tk

ventana = tk.Tk()
variabledecontrol = tk.IntVar() # Variable de control para los Radiobuttons

def opcion_seleccionada():
    color_opcion = variabledecontrol.get()  # Obtener el valor de la variable de control
    if color_opcion == 0: #if la opción es 0, cambia el color de fondo a rojo
        ventana.configure(bg="red")  #cambia el color de fondo a rojo
    elif color_opcion == 1: #if la opción es 1, cambia el color de fondo a azul
        ventana.configure(bg="blue") #cambia el color de fondo a azul

opciones1 = tk.Radiobutton(ventana, text="opcion 1", value=1, command=opcion_seleccionada) #crea la primera opción
opciones2 = tk.Radiobutton(ventana, text="opcion 2", value=2, command=opcion_seleccionada) #crea la segunda opción

opciones1.pack() #agrega la primera opción a la ventana
opciones2.pack() #agrega la segunda opción a la ventana





ventana.mainloop()

