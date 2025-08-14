import tkinter as tk

ventana = tk.Tk() 

boton1 = tk.Button(ventana, text="hola soy un boton") #esto crea un boton con el texto "hola soy un boton"
boton1.config(bg="red", fg="white", font=("arial", 20)) #configura el fondo, color de letra y tipo de letra
#bg: fondo, fg: color de letra, font: tipo de letra
boton1.config(width=20, height=5) #configura el ancho y alto    
boton1.pack() #esto lo coloca en la ventana

def cambiar_text():
    etiqueta.config(text="menti soy malo :3") #esto cambia el texto de la etiqueta al hacer click en el boton2

boton2=tk.Button(ventana, text="hola soy un boton", command=cambiar_text) #esto crea un boton con el texto "hola soy bueno" y al hacer click cambia el texto del boton2
boton2.config(bg="blue", fg="white", font=("arial", 20))    
boton2.config(width=20, height=5) #configura el ancho y alto
boton2.pack() #esto lo coloca en la ventana 

etiqueta = tk.Label(ventana, text="hola soy bueno") 
etiqueta.pack() 


ventana.mainloop() 