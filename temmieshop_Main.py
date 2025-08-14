import tkinter

ventana=tkinter.Tk()
#tamaño de la ventana bro y el maximo y el minimo
ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}+0+0")
ventana.minsize(500,300)
#el icono
ventana.iconbitmap("")
#color
ventana.configure(bg="aquamarine")



ventana.mainloop()