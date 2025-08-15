from tkinter import *

ventana =Tk()
ventana.title("Ventana Principal")
ventana.geometry("600x400")

#se le pone lo que medira esa ventana
ventana_topLevel = Toplevel(ventana)
ventana_topLevel.title("Ventana TopLevel")
ventana_topLevel.geometry("300x200+50+50")
label = Label(ventana_topLevel, text="Ventana TopLevel")
label.pack()

#funcion que permite cerrar la ventana
def cerrar_ventana_topLevel(ventana_topLevel):
    ventana_topLevel.destroy()
#aqui creamos el boton y se le asigna el texto y a que funcion va a llamar
#el boton solo se va a ejecutar cuando lo presiones , para que se pueda hacer se untiliza el lambda:
boton_cerrar = Button(ventana, text="Cerrar ventana top level", command=lambda: cerrar_ventana_topLevel(ventana_topLevel))
boton_cerrar.pack()

ventana.mainloop()