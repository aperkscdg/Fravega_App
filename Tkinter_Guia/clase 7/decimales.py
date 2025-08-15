import tkinter as tk

ventana = tk.Tk()


decimal = tk.DoubleVar(value=0.0)

control_deslizante = tk.Scale(ventana, from_=0 , to=10.0 ,resolution=0.1, variable=decimal) #crea un control deslizante que va de 0 a 10 con una resolución de 0.1
control_deslizante.pack()  # Empaqueta el control deslizante en la ventana

#la varaible decimal es para poner cual valor se va a mostrar en el control deslizante
#from_=0 y to=10.0 son los valores mínimo y máximo del control deslizante
#to es el valor máximo del control deslizante
#resolution=0.1 es la cantidad de cambio que se produce al mover el control deslizante








ventana.mainloop()  