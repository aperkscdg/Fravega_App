# los frames son cuadros o contenedores que en los cuales yo puedo ir poniendo cosas
import tkinter as tk

#Esto queda igual
ventana=tk.Tk()

ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}")

#asignas el frame i entre parentesis pones en donde quiere que se ubique ese frame 
#en este caso la ventana
#con el . configure pones la altura , el color (bg), la anchura y el grosor del borde(bd)
#con el .pack haces que ese frame se reproduzca en pantalla

frame1=tk.Frame(ventana)
frame1.configure(width=300,height=200,bg="red",bd=5)
frame1.pack()

#puedes poner frames dentro de frames , solo tienes que cambiar el parentesis en donde quieres que se ubique
frame2=tk.Frame(frame1)
frame2.configure(width=200,height=100,bg="white",bd=5)
frame2.pack()

ventana.mainloop()



