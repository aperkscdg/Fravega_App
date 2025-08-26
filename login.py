import tkinter as tk


ventana = tk.Tk()
ventana.title("LOGIN: FRÁVEGA")
ventana.configure(background="#000000")

ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}")

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
nombre = tk.Entry(frame, width=30)
nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Etiqueta Contraseña
etiqueta_contraseña = tk.Label(frame, text="Contraseña", bg="#000000", fg="white")
etiqueta_contraseña.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Entry Contraseña
contraseña = tk.Entry(frame, width=30, show="*")
contraseña.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Botón Ingresar
boton_ingresar = tk.Button(frame, text="Ingresar")
boton_ingresar.grid(row=2, column=0, columnspan=2, pady=15)








ventana.mainloop()