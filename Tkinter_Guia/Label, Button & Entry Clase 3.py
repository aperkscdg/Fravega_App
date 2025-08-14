import tkinter as tk
import time #libereria para manejar el tiempo

ventana = tk.Tk()

# ETIQUETA Y ACTUALIZAR HORA EN TIEMPO REAL EN LA ETIQUETA

etiqueta = tk.Label(ventana,text="esto crea un texto") #esto crear una etiqueta (texto)
etiqueta.config(bg="red", fg="white", font=("arial", 20) ) #configura el fondo, color de letra y tipo de letra
#bg: fondo, fg: color de letra, font: tipo de letra 
etiqueta.config(width=20, height=5) #configura el ancho y alto  
etiqueta.pack() #esto lo coloca en la ventana 



def actualizar_tiempo():
    etiqueta.config(text=time.strftime("%H:%M:%S")) #actualiza el texto de la etiqueta con la hora actual
    #el metodo strftime formatea el tiempo en horas, minutos y segundos
    # %H: horas, %M: minutos, %S: segundos 
    ventana.after(1000, actualizar_tiempo) #llama a la función cada 1000 milisegundos (1 segundo)
    # el metodo after permite ejecutar una función después de un tiempo determinado


actualizar_tiempo() #llama a la función para iniciar la actualización del tiempo

#BOTONES

def boton_presionado():
    print("Botón presionado") #esto imprime un mensaje en la consola cuando se presiona el botón
    etiqueta2.config(text="menti soy malo") #actualiza el texto de la etiqueta2 al presionar el botón

boton = tk.Button(ventana, text="Presioname" ) #crea un boton
boton.config(bg="blue", fg="white", font=("arial", 20) ) #configura el fondo, color de letra y tipo de letra
boton.config(width=20, height=5) #configura el ancho y alto 
boton.config(command=boton_presionado) #asigna la función que se ejecutará al presionar el botón
boton.pack() #esto lo coloca en la ventana

frame = tk.Frame(ventana)
frame.pack() #esto coloca el frame en la ventana
etiqueta2 = tk.Label(frame, text="hola soy bueno") 
etiqueta2.pack()




ventana.mainloop()