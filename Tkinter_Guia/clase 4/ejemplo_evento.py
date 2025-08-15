import tkinter as tk
#para definir un evento se pone la variable event adentro de la funcion
#un evento es algo que hace el usuario como por ejemplo tocar el mouse en algo , tocar un boton etc
ventana=tk.Tk()

#Con esto sabes si tocaste un boton o no
def on_click(event):
    print("boton presionado")
boton=tk.Button(ventana,text="haz click aqui")
boton.pack()

boton.bind("<Button-1>",on_click)

#Con este para saber que tecla tocaste
def tocar_tecla(event):
#Si cierta tecla se toca en este caso a , se printea tal cosa
    if event.char=="a":
        print("one shot (tecla a presionada)")
ventana.bind("<KeyPress>",tocar_tecla)

#Con esto cuanto tamaño tiene la ventana 
def ventana_minimizada(event):
    print(f"la ventana a sido redimenzionada a {event.width}x{event.height}")

ventana.bind("<Configure>",ventana_minimizada)

#En que posicion esta el mouse
def ubicacion_mouse(event):
    print(f"La ubicacion del cursor es {event.x}x{event.y}")

ventana.bind("<Motion>",ubicacion_mouse)

#Generar varios botones y saber cual presionamos
def clickear_boton(event):
#en el text pone el texto que ponemos despues
    print(f"{event.widget['text']} presionado")
#Generador de botones
#aqui es donde asignamos el texto al principio
botones = [tk.Button(ventana, text=f"Botón {i}") for i in range(3)]

for button in botones:
    button.pack()
    button.bind("<Button-1>", clickear_boton)

ventana.mainloop()
