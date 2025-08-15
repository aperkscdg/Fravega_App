import tkinter as tk

ventana = tk.Tk()


entero = tk.IntVar(value=0)  # Esto establece el valor inicial de la variable IntVar

print("ESTA MAL", entero)  # Esto es malo, no imprime el valor de la variable

print("ESTA BIEN", entero.get())  # Esto imprime el valor de la variable IntVar

opciones = [tk.Radiobutton(ventana, text="Opción " + str(i + 1), variable=entero, value=i) for i in range(2)]
for opcion in opciones:
    opcion.pack(anchor=tk.W) 

def actualizar_texto():
    numero= entero.get()  # Obtiene el valor actual de la variable IntVar
    numero+=1
    print("Valor seleccionado:", numero)  # Imprime el valor actual de la variable IntVar 

entero.trace("w", lambda *args: actualizar_texto())  # El método trace permite que cada vez que se modifique el valor de la variable IntVar, se actualice el texto


ventana.mainloop()  