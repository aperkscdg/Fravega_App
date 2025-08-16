from tkinter import filedialog
import tkinter as tk


ventana= tk.Tk()

def abrir_archivo():
    archivo= filedialog.askopenfilename(filetypes={("Text Files ", "*.txt")})
    if archivo:
        with open(archivo,"r") as archivo:
            contenido = archivo.read()
            text.delete(1.0,tk.END)
            text.insert(tk.INSERT,contenido)

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(filetypes={("Text Files ", ".txt")})
    if archivo:
        with open(archivo, "w") as archivo:
            contenido=text.get(1.0,tk.END)
            archivo.write(contenido)

text = tk.Text(ventana,wrap="word")
text.pack()

botones = [
    tk.Button(ventana, text="Abrir archivo", command=abrir_archivo),
    tk.Button(ventana, text="Guardar archivo", command=guardar_archivo)
]

for boton in botones:
    boton.pack(side="left")








ventana.mainloop()