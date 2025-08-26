import tkinter as tk

ventana = tk.Tk()
ventana.title("Fravega")
ventana.geometry("800x100")



def crear_header(ventana):
    #la parte de arriba
    header = tk.Frame(ventana, bg="DarkOrchid1", height=60)
    header.pack(fill="x")

    #logito
    logo = tk.Label(header, text="FRÁVEGA", font=("Arial", 16, "bold"), bg="lightgray", fg="purple")
    logo.pack(side="left", padx=10)

    # bienvenida
    ubicacion = tk.Label(header, text="Bienvenido niko",font=("Arial"))
    ubicacion.pack(side="left", padx=10)


crear_header(ventana)



ventana.mainloop()