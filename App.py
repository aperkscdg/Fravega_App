import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import datetime

ventana = tk.Tk()

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

    from produtos import lista_productos
    
    frame_inventario = tk.Frame(ventana)
    frame_inventario.place(x=50,y=74)

    lista = tk.Listbox(frame_inventario,width=60,height=30,bd=0,font=("Impacto",12))
    for i, prod in enumerate(lista_productos, start=1):
        lista.insert(i, str(prod))

    def toggle():
        if lista.winfo_ismapped():
            lista.pack_forget()
        else:
            lista.pack()
            


    boton = tk.Button(frame_inventario, text="Inventario",
                    command=toggle, bg="DarkOrchid1", fg="white",font=("Impacto",12),bd=0)
                    

    boton.pack()

    carrito = tk.Listbox(frame_inventario, width=60, height=10, bd=0, font=("Impacto",12))
    carrito.pack(pady=10)

    boton_stock = tk.Button(frame_inventario, text="", state="disabled", bg="green", fg="white")
    boton_stock.pack()


    

    nombre_cliente = tk.Entry(ventana)
    nombre_cliente.pack()

    apellido_cliente = tk.Entry(ventana)
    apellido_cliente.pack()

    dni=tk.Entry(ventana)
    dni.pack()

    ciudad=tk.Entry(ventana)
    ciudad.pack()

    region=tk.Entry(ventana)
    region.pack()

    codigo_postal=tk.Entry(ventana)
    codigo_postal.pack()

    texto_nombre=tk.Label(ventana,text="Nombre Completo del Cliente")
    texto_nombre.pack()

    texto_apellido=tk.Label(ventana,text="Apellido del Cliente")
    texto_apellido.pack()

    texto_dni=tk.Label(ventana,text="DNI del Cliente")
    texto_dni.pack()

    texto_ciudad=tk.Label(ventana,text="ciudad del cliente")
    texto_ciudad.pack()

    texto_region=tk.Label(ventana,text="Region del cliente")
    texto_region.pack()

    texto_codigo_postal=tk.Label(ventana,text="Codigo postal de cliente")
    texto_codigo_postal.pack()




    def descargar_factura():
        variable_nombre = nombre_cliente.get()
        variable_apellido = apellido_cliente.get()
        variable_dni = dni.get()
        variable_ciudad = ciudad.get()
        variable_region = region.get()
        variable_codigo_postal = codigo_postal.get()

        # Validaciones
        if not variable_nombre or not variable_dni or not variable_region or not variable_codigo_postal or not variable_apellido:
            messagebox.showerror("Falta Información", "Todas las opciones tienen que estar completas")
            return
        elif not variable_nombre.isalpha() or not variable_ciudad.isalpha() or not variable_region.isalpha() or not variable_apellido.isalpha():
            messagebox.showerror("Error de Formato", "Las cajas (NOMBRE/APELLIDO/CIUDAD/REGION) deben contener solo letras.")
            return
        elif not variable_dni.isdigit() or not variable_codigo_postal.isdigit():
            messagebox.showerror("Formato Incorrecto", "Las cajas (DNI / CÓDIGO POSTAL) deben contener solo números.")
            return
        elif carrito.size() == 0:
            messagebox.showerror("Error", "El carrito está vacío. Agrega productos antes de generar la factura.")
            return


        # Generar PDF
        nombre_archivo = "factura.pdf"
        pdf = SimpleDocTemplate(nombre_archivo, pagesize=A4)
        elementos = []
        estilos = getSampleStyleSheet()

        # Encabezado
        titulo = Paragraph("<b>FACTURA</b>", estilos["Title"])
        elementos.append(titulo)
        elementos.append(Spacer(1, 20))

        fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        info_cliente = f"""
        <b>Cliente:</b> {variable_nombre} {variable_apellido}<br/>
        <b>DNI:</b> {variable_dni}<br/>
        <b>Ciudad:</b> {variable_ciudad}<br/>
        <b>Región:</b> {variable_region}<br/>
        <b>Código Postal:</b> {variable_codigo_postal}<br/>
        <b>Fecha:</b> {fecha}<br/>
        """
        elementos.append(Paragraph(info_cliente, estilos["Normal"]))
        elementos.append(Spacer(1, 20))

        # === Tabla de productos desde los objetos ===
        data = [["Producto", "Precio Unitario", "Cantidad", "IVA %", "Total"]]
        total_general = 0

        # Guardamos una referencia de objetos agregados al carrito
        productos_carrito = []

        for i in range(carrito.size()):
            texto = carrito.get(i)  # "Nombre - $precio"
            # Buscar el objeto real en lista_productos
            for prod in lista_productos:
                if prod.nombre in texto:
                    productos_carrito.append(prod)
                    break

        # Agrupamos productos iguales
        productos_agrupados = {}
        for prod in productos_carrito:
            if prod.nombre not in productos_agrupados:
                productos_agrupados[prod.nombre] = {"precio": prod.precio_unitario, "cantidad": 1}
            else:
                productos_agrupados[prod.nombre]["cantidad"] += 1

        # Construimos la tabla
        for nombre, datos in productos_agrupados.items():
            precio_unitario = datos["precio"]
            cantidad = datos["cantidad"]
            iva = 21
            total_producto = (precio_unitario * cantidad) * (1 + iva/100)
            total_general += total_producto

            data.append([nombre, f"${precio_unitario:.2f}", cantidad, f"{iva}%", f"${total_producto:.2f}"])

        tabla = Table(data, colWidths=[150, 100, 60, 60, 100])
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]))
        elementos.append(tabla)

        elementos.append(Spacer(1, 20))
        elementos.append(Paragraph(f"<b>Total a Pagar: ${total_general:.2f}</b>", estilos["Heading2"]))

        # Construir PDF
        pdf.build(elementos)
        messagebox.showinfo("Éxito", f"Factura generada correctamente: {nombre_archivo}")


    
# Botón
    boton_descargar_factura = tk.Button(ventana, text="DESCARGAR FACTURA DE LA COMPRA", command=descargar_factura)
    boton_descargar_factura.pack()

    


    def refrescar_lista():
        lista.delete(0, tk.END)
        for prod in lista_productos:
            lista.insert(tk.END, str(prod))
    
    refrescar_lista()

    def seleccionar_producto(event):
        if lista.curselection():
            index = lista.curselection()[0]
            prod = lista_productos[index]
            # Configuramos el botón con el stock actual
            boton_stock.config(
                text=f"Stock disponible: {prod.stock}  | Restar 1",
                state="normal",
                command=lambda: restar_stock(index)
            )
            boton_stock.pack(pady=5)

    def restar_stock(index):
        prod = lista_productos[index]
        if prod.stock > 0:
            prod.stock -= 1
            carrito.insert(tk.END, f"{prod.nombre} - ${prod.precio_unitario}")
            refrescar_lista()
            boton_stock.config(text=f"Stock disponible: {prod.stock}  | Restar 1")
        else:
            boton_stock.config(text="Sin stock", state="disabled")

    lista.bind("<<ListboxSelect>>", seleccionar_producto)

crear_header(ventana)
inventario(ventana)

ventana.mainloop()
