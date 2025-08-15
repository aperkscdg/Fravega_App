import tkinter as tk

ventana = tk.Tk()

texto = tk.StringVar(value="hola mundo")  #esto setea el valor de una variable StringVar con el comando value

print("ESTA MAL", texto) #esto es malo, no imprime el valor de la variable

print("ESTA BIEN", texto.get())  #esto imprime el valor de la variable StringVar 

texto.set("adios mundo")  #esto cambia el valor de la variable StringVar

print("CAMBIO A", texto.get())  #esto imprime el nuevo valor de la variable StringVar

texto.set("hola de nuevo")  #esto cambia el valor de la variable StringVar nuevamente


label = tk.Label(ventana, textvariable=texto)  #esto crea un label que muestra el valor de la variable StringVar
label.pack()  #esto empaqueta el label en la ventana

def actualizar_texto():
    label.config(text=texto.get())  # Actualiza el texto de la etiqueta


entrada = tk.Entry(ventana, textvariable=texto,)  #esto crea una entrada de texto que modifica el valor de la variable StringVar
entrada.pack() 

texto.trace("w", lambda *args: actualizar_texto())  #el funcion trace permite que cada vez que se modifique el valor de la variable StringVar, se actualice el label el valor w es importante porque significa que se va a modificar el valor de la variable StringVar



ventana.mainloop()  # Inicia el bucle principal de la ventana