from tkinter import filedialog
import tkinter as tk


ventana = tk.Tk()

ventana.withdraw() #oculta la ventana principal

leer_archivo = filedialog.askopenfile(mode="r") #esto nos va abrir el sistema de archivos para que despues pueda leer lo que esta dentro de el como por ejemplo un archivo py o txt 

if leer_archivo: #aqui comprueba que no este vacio
    print(leer_archivo.read()) #printea lo que esta dentro
    leer_archivo.close() #y esto lo cierra el archivo para que libere espacio en memoria





ventana.mainloop()