from tkinter import filedialog
import tkinter as tk

ventana=tk.Tk()

def abrir_archivo():
    ruta = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')]) #esto es para poner el tipo de archivo que se va abrir
    if ruta: #comprueba que tenga texto
        with open(ruta, "r") as ruta: 
            contenido = ruta.read()
            text_objeto.delete(1.0,tk.END)
            text_objeto.insert(tk.INSERT,contenido)

text_objeto = tk.Text(ventana,wrap="word")
text_objeto.pack(expand=True,fill="both")

boton = tk.Button(ventana,text="Abriri Archivo",command=abrir_archivo)
boton.pack()





ventana.mainloop()