import tkinter as tk
from PIL import Image,ImageTk #necesario para abrir las imagenes

ventana=tk.Tk()
#con esto metes la imagen a python
imagen_pil1 = Image.open("Tkinter_Guia/clase 12/mugroso.png")
#esto cambia el tamaño de la imagen
imagen_redimensiona=imagen_pil1.resize((100,100))
#cambia la rotacion de la imagen
imagen_rotada=imagen_redimensiona.rotate(45)
#y con esto la asocias a tkinter 
imagen_tk1 = ImageTk.PhotoImage(imagen_rotada)



#con el image se le puede asignar una imagen al boton
boton = tk.Button(ventana, image=imagen_tk1)
boton.pack()

ventana.mainloop()