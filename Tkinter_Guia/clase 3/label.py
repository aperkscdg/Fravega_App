import tkinter as tk

ventana = tk.Tk()

# ETIQUETA Y ACTUALIZAR HORA EN TIEMPO REAL EN LA ETIQUETA

etiqueta = tk.Label(ventana,text="esto crea un texto") #esto crear una etiqueta (texto)
etiqueta.config(bg="red", fg="white", font=("arial", 20) ) #configura el fondo, color de letra y tipo de letra
#bg: fondo, fg: color de letra, font: tipo de letra 
etiqueta.config(width=20, height=5) #configura el ancho y alto  
etiqueta.pack() #esto lo coloca en la ventana 

ventana.mainloop()