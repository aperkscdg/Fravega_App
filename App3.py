import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import datetime

ventana = tk.Tk()
ventana.title("Fravega")
ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()
ventana.geometry(f"{ancho}x{alto}+0+0")
ventana.iconbitmap("imagenes/fravega.ico")

# Fondo
label_fondo_no = Image.open("Imagenes/fra.png")
fondo_res = label_fondo_no.resize((1400, 800))
label_fondo_si = ImageTk.PhotoImage(fondo_res)
label_fondo = tk.Label(ventana, image=label_fondo_si)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)


def crear_header(ventana,nombre_empleado):
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

    #ubicacion = tk.Label(header, text="Bienvenido"+{nombre_empleado}, font=("Impacto", 18), fg="white", bg="plum1")
    ubicacion = tk.Label(header, text=f"Bienvenido {nombre_empleado}", font=("Impacto", 18), fg="white", bg="plum1")
    ubicacion.pack(side="left", padx=10)

    usuario_no = Image.open("Imagenes/Usuario.png").convert("RGBA")
    usuario_red = usuario_no.resize((50, 50))
    usuario = ImageTk.PhotoImage(usuario_red)
    boton_usuario = tk.Button(header, image=usuario, bg="plum1", activebackground="white", bd=0)
    boton_usuario.image = usuario
    boton_usuario.pack(side="right", padx=10)

    config_no = Image.open("Imagenes/Config.png").convert("RGBA")
    config_red = config_no.resize((50, 50))
    config = ImageTk.PhotoImage(config_red)
    boton_config = tk.Button(header, image=config, bg="plum1", activebackground="white", bd=0)
    boton_config.image = config
    boton_config.pack(side="right", padx=10)


def inventario(ventana):
    from produtos import lista_productos

    frame_inventario = tk.Frame(ventana, bg="orchid2")
    frame_inventario.place(x=50, y=74)

    frame_pedido = tk.Frame(ventana, bg="orchid2")
    frame_pedido.place(x=700, y=74)

    # Lista de productos
    lista = tk.Listbox(frame_inventario, width=50, height=20, bd=0, font=("Impacto", 12),
                    highlightthickness=5, highlightbackground="orchid2")

    def toggle_pedidos():
        if lista.winfo_ismapped():
            lista.pack_forget()
        else:
            lista.pack(side="bottom", fill="x")

    pedido_no = Image.open("Imagenes/ppedidos.png")
    pedido_res = pedido_no.resize((200, 75))
    pedidos_si = ImageTk.PhotoImage(pedido_res)
    boton = tk.Button(frame_inventario, image=pedidos_si, command=toggle_pedidos,
                    bg="orchid2", border=0, activebackground="orchid2")
    boton.image = pedidos_si
    boton.pack()

    # ===== Frame para carrito y boton_stock cerca de frame_cliente =====
    frame_carrito = tk.Frame(frame_pedido, bg="orchid2")
    frame_carrito.pack(pady=10)

    carrito = tk.Listbox(frame_carrito, width=60, height=10, bd=0, font=("Impacto", 12))
    carrito.pack(pady=5)

    boton_stock = tk.Button(frame_carrito, text="Stock", state="disabled", bg="white", fg="black")
    boton_stock.pack()

    # Inicialmente ocultos
    frame_carrito.pack_forget()

    # ===== Frame Cliente =====
    frame_cliente = tk.Frame(frame_pedido, bg="orchid2")

    tk.Label(frame_cliente, text="Nombre", bg="orchid2").pack()
    nombre_cliente = tk.Entry(frame_cliente)
    nombre_cliente.pack()

    tk.Label(frame_cliente, text="Apellido", bg="orchid2").pack()
    apellido_cliente = tk.Entry(frame_cliente)
    apellido_cliente.pack()

    tk.Label(frame_cliente, text="DNI", bg="orchid2").pack()
    dni = tk.Entry(frame_cliente)
    dni.pack()

    tk.Label(frame_cliente, text="Ciudad", bg="orchid2").pack()
    ciudad = tk.Entry(frame_cliente)
    ciudad.pack()

    tk.Label(frame_cliente, text="Región", bg="orchid2").pack()
    region = tk.Entry(frame_cliente)
    region.pack()

    tk.Label(frame_cliente, text="Código Postal", bg="orchid2").pack()
    codigo_postal = tk.Entry(frame_cliente)
    codigo_postal.pack()

    # ===== Función para generar factura =====
    def descargar_factura():
        variable_nombre = nombre_cliente.get()
        variable_apellido = apellido_cliente.get()
        variable_dni = dni.get()
        variable_ciudad = ciudad.get()
        variable_region = region.get()
        variable_codigo_postal = codigo_postal.get()

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

        nombre_archivo = "factura.pdf"
        pdf = SimpleDocTemplate(nombre_archivo, pagesize=A4)
        elementos = []
        estilos = getSampleStyleSheet()

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

        data = [["Producto", "Precio Unitario", "Cantidad", "IVA %", "Total"]]
        total_general = 0
        productos_carrito = []

        for i in range(carrito.size()):
            texto = carrito.get(i)
            for prod in lista_productos:
                if prod.nombre in texto:
                    productos_carrito.append(prod)
                    break

        productos_agrupados = {}
        for prod in productos_carrito:
            if prod.nombre not in productos_agrupados:
                productos_agrupados[prod.nombre] = {"precio": prod.precio_unitario, "cantidad": 1}
            else:
                productos_agrupados[prod.nombre]["cantidad"] += 1

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

        pdf.build(elementos)
        nombre_cliente.delete(0,tk.END)
        apellido_cliente.delete(0,tk.END)
        dni.delete(0,tk.END)
        ciudad.delete(0,tk.END)
        region.delete(0,tk.END)
        codigo_postal.delete(0,tk.END)
        carrito.delete(0,tk.END)
        messagebox.showinfo("Éxito", f"Factura generada correctamente: {nombre_archivo}")

    # ===== Toggle Factura =====
    def toggle_factura():
        if frame_cliente.winfo_ismapped():
            frame_cliente.pack_forget()
            frame_carrito.pack_forget()
        else:
            frame_cliente.pack(pady=10)
            frame_carrito.pack(pady=10)

    factura_no = Image.open("Imagenes/factura.png")
    factura_res = factura_no.resize((200, 75))
    factura_si = ImageTk.PhotoImage(factura_res)
    boton_descargar_factura = tk.Button(frame_pedido, image=factura_si, command=toggle_factura,
                                        bg="orchid2", border=0, activebackground="orchid2")
    boton_descargar_factura.image = factura_si
    boton_descargar_factura.pack()

    boton_generar_factura = tk.Button(frame_cliente, text="Generar Factura", command=descargar_factura,
                                    bg="plum1", fg="white", bd=0)
    boton_generar_factura.pack(pady=10)

    # ===== Lista productos =====
    def refrescar_lista():
        lista.delete(0, tk.END)
        for prod in lista_productos:
            lista.insert(tk.END, str(prod))

    refrescar_lista()

    # ===== Seleccionar producto =====
    def seleccionar_producto(event):
        if lista.curselection():
            index = lista.curselection()[0]
            prod = lista_productos[index]
            boton_stock.config(
                text=f"Stock disponible: {prod.stock}  | Restar 1",
                state="normal",
                command=lambda: restar_stock(index)
            )

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


def login(ventana):
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
                logo.grid_forget()
                frame.grid_forget()
                etiqueta_nombre.grid_forget()
                etiqueta_nombre.grid_forget()
                nombre_entry.grid_forget()
                contraseña_entry.grid_forget()
                crear_header(ventana,nombre_empleado)
                inventario(ventana)

    # Configurar filas y columnas para centrar contenido
    ventana.grid_rowconfigure(0, weight=1)
    ventana.grid_rowconfigure(1, weight=1)
    ventana.grid_columnconfigure(0, weight=1)

    # Imagen arriba de todo
    fravega_no = Image.open("Imagenes/logo-fravega.png").convert("RGBA")
    fravega_logo = ImageTk.PhotoImage(fravega_no)
    logo = tk.Label(ventana, image=fravega_logo, bg="plum1")
    logo.image = fravega_logo
    logo.grid(row=0, column=0, pady=20)

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

login(ventana)
ventana.mainloop()
