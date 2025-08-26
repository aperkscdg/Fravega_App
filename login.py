import tkinter as tk
from tkinter import messagebox


ventana = tk.Tk()
ventana.title("LOGIN: FRÁVEGA")
ventana.configure(background="#000000")

ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}")

class usuario:
    def __init__(self,nombre="",contraseña="",correo="",dni=0):
        self.nombre = nombre
        self.contraseña = contraseña
        self.correo = correo
        self.dni = dni
    def __str__(self):
        cadena_print=str((self.nombre)+""+str(self.contraseña)+""+(self.correo)+""+(self.dni))
        return cadena_print
    def validar_datos():
        nombre_empleado = nombre_entry.get()
        contraseña_empleado = contraseña_entry.get()
        if not nombre_empleado or not contraseña_empleado:
            messagebox.showerror("Falta Informacion", "Todas las Opciones tiene que estar completas")
        elif nombre_empleado.isdigit():
            messagebox.showerror("No puedes poner numeros", "su nombre no puedo llevar numeros")
        else:
            usuario_objeto = usuario(nombre_empleado, contraseña_empleado)
            #messagebox.showinfo("Datos Guardados", f"Usuario creado:\n{usuario}")
            imagen.grid_forget()
            frame.grid_forget()
            etiqueta_nombre.grid_forget()
            etiqueta_nombre.grid_forget()
            nombre_entry.grid_forget()
            contraseña_entry.grid_forget()




# Configurar filas y columnas para centrar contenido
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# Imagen arriba de todo
logo = tk.PhotoImage(file="img/logo_fravega.png")
imagen = tk.Label(ventana, image=logo, bg="white")  # Fondo blanco
imagen.grid(row=0, column=0, pady=20)

# Frame centrado debajo de la imagen
frame = tk.Frame(ventana, bg="#000000")
frame.grid(row=1, column=0)

# Etiqueta Nombre
etiqueta_nombre = tk.Label(frame, text="Nombre", bg="#000000", fg="white")
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Entry Nombre
nombre_entry = tk.Entry(frame, width=30)
nombre_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Etiqueta Contraseña
etiqueta_contraseña = tk.Label(frame, text="Contraseña", bg="#000000", fg="white")
etiqueta_contraseña.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Entry Contraseña
contraseña_entry = tk.Entry(frame, width=30, show="*")
contraseña_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")




# Botón Ingresar
boton_ingresar = tk.Button(frame, text="Ingresar",command=usuario.validar_datos)
boton_ingresar.grid(row=2, column=0, columnspan=2, pady=15)






ventana.mainloop()