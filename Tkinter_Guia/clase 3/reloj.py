import tkinter as tk
import time  # librería para manejar el tiempo

ventana = tk.Tk()

etiqueta = tk.Label(ventana, text="") 
etiqueta.config(bg="red", fg="white", font=("arial", 20))
etiqueta.config(width=20, height=5) 
etiqueta.pack()

def actualizar_tiempo():
    etiqueta.config(text=time.strftime("%H:%M:%S")) #actualiza el texto de la etiqueta con la hora actual
    #el metodo strftime formatea el tiempo en horas, minutos y segundos
    # %H: horas, %M: minutos, %S: segundos 
    ventana.after(1000, actualizar_tiempo) #llama a la función cada 1000 milisegundos (1 segundo)
    # el metodo after permite ejecutar una función después de un tiempo determinado


actualizar_tiempo()    #llama a la función para iniciar la actualización del tiempo

ventana.mainloop()
