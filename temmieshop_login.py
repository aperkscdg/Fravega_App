import tkinter as tk


def hola():
    print("holaaaaaaa")

ventana=tk.Tk()

boton=tk.Button(ventana,text="hola",command=hola)
boton.pack()

ventana.mainloop()

