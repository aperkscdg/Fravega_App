import tkinter as tk

ventana = tk.Tk()
ventana.geometry("1280x720")
ventana.resizable(False, False)  

etiqueta= tk.Label(ventana, text="lo de abajo es un entry")
etiqueta.pack()

def copiar_texto():
    texto = input_text.get()  # Obtiene el texto del campo de entrada
    etiqueta2.config(text=texto)  # Actualiza la etiqueta con el texto ingresado        
input_text = tk.Entry(ventana)  # Crea un campo de entrada de texto
input_text.config(bg="yellow", fg="black", font=("arial", 20))  # Configura el fondo, color de letra y tipo de letra
input_text.config(width=30, justify="center")  
input_text.insert(0, "Escribe algo aquí")  # Inserta un texto por defecto en el campo de entrada    
input_text.pack()  # Añade el campo de entrada a la ventana

boton = tk.Button(ventana, text="Copiar texto", command=copiar_texto) 
boton.pack() # Crea un botón que llama a la función copiar_texto al hacer clic


etiqueta2 = tk.Label(ventana, text="texto de lo que la persona ponga en el entry")
etiqueta2.pack()


ventana.mainloop()

