import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Fravega")
ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}+0+0")

label_fondo_no=Image.open("Imagenes/fra.png")
fondo_res=label_fondo_no.resize((1400,800))
label_fondo_si=ImageTk.PhotoImage(fondo_res)


label_fondo = tk.Label(ventana, image=label_fondo_si)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)



def crear_header(ventana):
    

    header = tk.Frame(ventana, bg="plum1", height=70)
    header.pack(fill="x")

    
    fravega_no = Image.open("Imagenes/logo-fravega.png").convert("RGBA")
    
    
    alto_header = 70
    ancho_logo = int(fravega_no.width * (alto_header / fravega_no.height))
    fravega_no = fravega_no.resize((ancho_logo, alto_header), Image.LANCZOS)

    fravega_logo = ImageTk.PhotoImage(fravega_no)
    logo = tk.Label(header, image=fravega_logo, bg="plum1")
    logo.image = fravega_logo
    logo.pack(side="left", padx=10)

   
    ubicacion = tk.Label(header, text="Bienvenido niko!", font=("Impacto",18),fg="white", bg="plum1")
    ubicacion.pack(side="left", padx=10)



    usuario_no = Image.open("Imagenes/Usuario.png").convert("RGBA")



    ancho_usuario = int(usuario_no.width * (alto_header / usuario_no.height))


    usuario_red = usuario_no.resize((ancho_usuario, alto_header), Image.LANCZOS)


    usuario = ImageTk.PhotoImage(usuario_red)

  
  
    boton_usuario = tk.Button(header, image=usuario,bg="plum1",activebackground="white",bd=0)
    boton_usuario.image = usuario
    boton_usuario.pack(side="right", padx=10)
    




def inventario(ventana):
    
    frame_inventario = tk.Frame(ventana,bg="MediumOrchid4")
    frame_inventario.place(x=50,y=74)

    lista = tk.Listbox(frame_inventario,width=60,height=30,bd=0,font=("Impacto",12),highlightthickness=5,highlightbackground="MediumOrchid4")
    lista.insert(1, "niko")
    lista.insert(2, "Cuphead")
    lista.insert(3, "Gabriel")

    def toggle():
        if lista.winfo_ismapped():
            lista.pack_forget()
        else:
            lista.pack()

    def toggle2():
        if lista.winfo_ismapped():
            lista.pack_forget()
        else:
            lista.pack()

    pedido_no=Image.open("Imagenes/ppedidos.png")
    pedido_res=pedido_no.resize((250,100))
    pedidos_si=ImageTk.PhotoImage(pedido_res)
    boton = tk.Button(frame_inventario, image=pedidos_si,
                      command=toggle, bg="MediumOrchid4",border=0,activebackground="MediumOrchid4")
    boton.image=pedidos_si
    boton.pack()
    
    factura_no=Image.open("Imagenes/factura.png")
    factura_res=factura_no.resize((250,100))
    factura_si=ImageTk.PhotoImage(factura_res)
    boton2 = tk.Button(frame_inventario, image=factura_si,
                      command=toggle2, bg="MediumOrchid4",border=0,activebackground="MediumOrchid4")
    boton.image=pedidos_si
    boton2.image=factura_si
    boton2.pack()
    

crear_header(ventana)
inventario(ventana)

ventana.mainloop()
