import tkinter as tk

ventana=tk.Tk()

#tamaño de la ventana adaptable a la pc
ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}+0+0")
#el +0´+0 es donde quieres que se ponga la ventana

#tamaño de la ventana personalizado
#ventana.geometry("600x400")

#tamaño maximo y minimo de la ventana
ventana.maxsize(600,400)
ventana.minsize(500,300)

#el icono
#ventana.iconbitmap("pon la dirreccion de la imagen aqui")

#color del fondo
ventana.configure(bg="aquamarine")

#bloquear la redimension de la ventana en x y y
#ventana.resizable(True,False)
#True si se puede , false si no

#transparencia de la ventana
ventana.attributes('-alpha',0.3)


ventana.mainloop()