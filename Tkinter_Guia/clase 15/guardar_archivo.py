from tkinter import filedialog
import tkinter as tk


ventana=tk.Tk()

ventana.withdraw()

guardar_objeto = filedialog.asksaveasfile(mode="w", defaultextension=".txt") #esto es para que la persona pueda guardar un archivo en formato txt
if guardar_objeto: #se fija que el objeto no esta en blanco y lo guarda con el texto "hola putitas"
    guardar_objeto.write("hola putitas")
    guardar_objeto.close() #y despues lo cierra







ventana.mainloop()