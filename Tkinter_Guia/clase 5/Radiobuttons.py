import tkinter as tk

ventana = tk.Tk()


variabledecontrol = tk.IntVar()

i=0



def opcion_seleccionada():
    variable = variabledecontrol.get() # el get método obtiene el valor de la variable de control
    variable+=1 #hice esto para que el valor de la variable sea 1,2,3,4,5 en vez de 0,1,2,3,4
    print("Opción seleccionada:", variable) # el get método obtiene el valor de la variable de control
    if variable == 1:
        ventana.configure(bg="red")
    elif variable == 2:
        ventana.configure(bg="blue")
    elif variable == 3:
        ventana.configure(bg="green")   
    elif variable == 4:
        ventana.configure(bg="yellow")
    elif variable == 5:
        ventana.configure(bg="purple")

opciones = [tk.Radiobutton(ventana, text="opciones "+ str(i+1) + "", variable=variabledecontrol, value=i , ) for i in range(0,5)]
for opcion in opciones:
    opcion.pack(anchor=tk.W) #este codigo agrega los radiobuttons a la ventana con un bucle 

boton=tk.Button(ventana, text="Click para saber la opcion", command=opcion_seleccionada )
boton.pack()



ventana.mainloop()