import tkinter as tk
#aclaracion no hagamos esto , importgar imagenes asi es una basura XDDDDDDDDDDDDDDDD
ventana = tk.Tk()
#se importa las imagenes asi con el tk.photoimage
#aunque no se tiene mucho control
imagen = tk.PhotoImage(file="Tkinter_Guia/clase 12/cuphead.gif")
imagen2 = tk.PhotoImage(file="Tkinter_Guia/clase 12/niko.gif")

etiqueta = tk.Label(ventana, image=imagen)
boton = tk.Button(ventana, image=imagen2)

etiqueta.pack()
boton.pack()

ventana.mainloop()
