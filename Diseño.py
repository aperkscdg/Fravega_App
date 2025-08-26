import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Fravega")
ventana.geometry("800x100")

def crear_header(ventana):
    header = tk.Frame(ventana, bg="DarkOrchid1", height=70)
    header.pack(fill="x")

    
    fravega_no = Image.open("Imagenes/logo-fravega.png").convert("RGBA")
    
    
    alto_header = 70
    ancho_logo = int(fravega_no.width * (alto_header / fravega_no.height))
    fravega_no = fravega_no.resize((ancho_logo, alto_header), Image.LANCZOS)

    fravega_logo = ImageTk.PhotoImage(fravega_no)
    logo = tk.Label(header, image=fravega_logo, bg="DarkOrchid1")
    logo.image = fravega_logo
    logo.pack(side="left", padx=10)

   
    ubicacion = tk.Label(header, text="Bienvenido niko!", font=("Impacto",18),fg="white", bg="DarkOrchid1")
    ubicacion.pack(side="left", padx=10)



    usuario_no = Image.open("Imagenes/Usuario.png").convert("RGBA")



    ancho_usuario = int(usuario_no.width * (alto_header / usuario_no.height))


    usuario_red = usuario_no.resize((ancho_usuario, alto_header), Image.LANCZOS)


    usuario = ImageTk.PhotoImage(usuario_red)

  
  
    boton_usuario = tk.Button(header, image=usuario,bg="DarkOrchid1",activebackground="white",bd=0)
    boton_usuario.image = usuario
    boton_usuario.pack(side="right", padx=10)
    




def inventario(ventana):
    
    frame_inventario = tk.Frame(ventana)
    frame_inventario.place(x=50,y=74)

    lista = tk.Listbox(frame_inventario,width=60,height=30,bd=0,font=("Impacto",12))
    lista.insert(1, "niko")
    lista.insert(2, "Cuphead")
    lista.insert(3, "Gabriel")

    def toggle():
        if lista.winfo_ismapped():
            lista.pack_forget()
        else:
            lista.pack()

    boton = tk.Button(frame_inventario, text="Inventario",
                      command=toggle, bg="DarkOrchid1", fg="white",font=("Impacto",12),bd=0)
    
    
    boton.pack()

crear_header(ventana)
inventario(ventana)

ventana.mainloop()
