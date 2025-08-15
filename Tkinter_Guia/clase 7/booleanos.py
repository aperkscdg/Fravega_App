import tkinter as tk

ventana = tk.Tk()


booleano = tk.BooleanVar(value=False)  # Esto establece el valor inicial de la variable BooleanVar

print("ESTA MAL", booleano)  # Esto es malo, no imprime el valor de la variable

print("ESTA BIEN", booleano.get())  # Esto imprime el valor de la variable BooleanVar

def actualizar_texto():
    estado = booleano.get()  # Obtiene el valor actual de la variable BooleanVar
    print("Estado de la casilla:", estado)  # Imprime el estado actual de la casilla


casilla = tk.Checkbutton(ventana, text="aceptar condiciones", variable=booleano, command=actualizar_texto) 
casilla.pack()


ventana.mainloop() 