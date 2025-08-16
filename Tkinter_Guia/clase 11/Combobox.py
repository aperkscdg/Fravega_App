import tkinter as tk
from tkinter import ttk # esto es necesario para poder usar el elemento combobox de tkinter

ventana = tk.Tk()

combobox = ttk.Combobox(ventana, width=20, font=("Arial", 12 ), foreground="blue", background="white") #e
#esto agrega un combobox que es un menu donde puedes selecionar varios elementos
combobox.pack()

elementos = ["Elemento 1 ", "Elemento 2", "Elemento 3"]
#para lograr esto tenemos que crear una lista con todos los elementos que va a tener
combobox["values"] = elementos
# y con este comando ponemos que los valores de cada conbobox son iguales a los de la lista entoces
# 0 = 0 y el valor cero es el "Elemento 1"

#elementos.remove("Elemento 1") esto elimina un elemento de la lista osea del combobox 
#combobox["values"] = elementos (pero para que esto tengo efecto tenemos que actualizar con el nuevo index de la lista)
#antes la lista era de 2 (0=elemento 1, 1=elemento 2 y 2 = elemento 3)
#elementos = ["Elemento 1 ", "Elemento 2", "Elemento 3"]
#la nueva lista seria de 1 osea 0=elemento 2 y 1= elemeneto 3
#elementos = ["Elemento 2", "Elemento 3"]

#esto es para modificar una opcion del combobox

#indice = 1 # esto seria el index de la lista 
#nuevo_valor= "Elemento modificado" # esta variable es  por que queremos cambiar ese indice osea si era elemento 1 ahora seria elemento modificado 
#elemento[indice]= nuevo_valor #aqui decimos que en la lista modifica el numero del indice que tiene esa variable por el nuevo valor que sea elemento modificado
#combobox["values"] = elementos (aqui lo hacemos que tenga efecto en el combobox)

#tambien lo podemos hacer de esta forma
# #elemento[1]= "elemento modificado"
#combobox["values"] = elementos # lo actualizamos 

#la mejor forma es la primera forma es mas automatizado que la segunda que tenemos que repetir lineas de codigo
#con el primer metodo podemos hacer una funcion y que reciba los parametro de cual indice quiere modificar

def on_seleccionar(event):
    valor_seleccionado = combobox.get()
    print(f"Seleccionado: {valor_seleccionado}")

combobox.bind("<<ComboboxSelected>>", on_seleccionar)






ventana.mainloop()