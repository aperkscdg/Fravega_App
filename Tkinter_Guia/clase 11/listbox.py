import tkinter as tk

ventana = tk.Tk()

listbox=tk.Listbox(ventana,width=10,height=10,font=("Arial 12", 12 ), fg="Blue", bg="white")
listbox.insert(tk.END, "Elemento 1")
listbox.insert(tk.END, "Elemento 2" )

# el comando tk.listbox como dice el nombre es una lista que esta en un caja, que puede tener varios elementos
# listbox.insert es el comando para insertar un elemento a la lista. 
# el tk.end es para que se añada al final de la lista. si nosotros agregamos por ejemplo 
#listbox.insert(0, "Elemento 2" )
# si pones un numero y no el tk.END el cero lo que va a hacer es ponerlo en la primera fila de la lista lo mismo si ponemos uno o dos lo pondra en esa posicion de la lista

# su usamos este comando 

#listbox.delete(0) esto va a borrar el primer elemento 

def on_selleccionar(event): # este evento detecta que elemento esta tocando la personas
    indice = listbox.curselection()
    elementos = listbox.get(indice)
    print(f"Seleccionado:  {elementos}" )


listbox.bind("<<ListboxSelect>>", on_selleccionar) # esto activa el evento


listbox.pack()






ventana.mainloop()