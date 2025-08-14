import tkinter as tk

ventana=tk.Tk()
#tamaño de la ventana bro y el maximo y el minimo
ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}")

frame1=tk.Frame(ventana)
frame1.configure(width=300,height=300,bg="red",bd=3)

