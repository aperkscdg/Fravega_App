from tkinter import filedialog
import tkinter as tk



ventana = tk.Tk()

ventana.withdraw() #oculta la ventana principal

archivo_copy =filedialog.askopenfilename() #esto es para acceder al sistema de archivos y el archivo que la persona elija nos va a tirar toda la ruta hasta llegar a esa archivo 
#C:/Users/byron/OneDrive/Escritorio/43434.PNG

#archivo_copy =filedialog.askopenfilenames() si ponemos este comando se van a poder selecionar varios archivos con el que se creara una lista con todas las direciones de cade archivo selecionado 

print(archivo_copy)





ventana.mainloop()