#los labelframes son casi lo mismo que los frames pero con texto
import tkinter as tk

ventana=tk.Tk()

ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}")

#le asignas el texto en text=
labelframe=tk.LabelFrame (ventana,text="Hola papu",bg="yellow",padx=10,pady=10)
labelframe.configure(width=300,height=200)
labelframe.pack()


ventana.mainloop()