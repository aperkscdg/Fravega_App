class productos():
    def __init__(self,codigo_producto=0,nombre="",fabricante="",categoria="",desc_producto="",garantia_producto="",resenias="",precio_unitario=0,stock=0,iva=0):
        self.codigo_producto=codigo_producto
        self.nombre=nombre
        self.fabricante=fabricante
        self.categoria=categoria
        self.desc_producto=desc_producto
        self.garantia_producto=garantia_producto
        self.resenias=resenias
        self.precio_unitario=precio_unitario
        self.stock = stock
        self.iva = iva
    def __str__(self):
        cadena_texto = (
        str(self.nombre) + "," +
        str(self.fabricante) + "," +
        "$" + str(self.precio_unitario) + "," +
        "STOCK ACTUAL: " + str(self.stock) + "," +
        "iva: " + str(self.iva)
        )
        return cadena_texto

p1 = productos(codigo_producto=1, nombre="Televisor", fabricante="Sony", categoria="Electrónica",
    desc_producto="Televisor LED 50 pulgadas", garantia_producto="2 años",
    resenias="Buena calidad de imagen", precio_unitario=200000, stock=10, iva=21)

p2 = productos(codigo_producto=2, nombre="Notebook", fabricante="HP", categoria="Computación",
    desc_producto="Notebook 15 pulgadas, Intel i5", garantia_producto="1 año",
    resenias="Rápida y liviana", precio_unitario=350000, stock=5, iva=21)

p3 = productos(codigo_producto=3, nombre="Celular", fabricante="Samsung", categoria="Telefonía",
    desc_producto="Celular Galaxy A52", garantia_producto="1 año",
    resenias="Excelente cámara", precio_unitario=150000, stock=20, iva=21)

p4 = productos(codigo_producto=4, nombre="Heladera", fabricante="Whirlpool", categoria="Electrodomésticos",
    desc_producto="Heladera no frost", garantia_producto="2 años",
    resenias="Muy eficiente", precio_unitario=400000, stock=3, iva=10.5)

p5 = productos(codigo_producto=5, nombre="Auriculares", fabricante="JBL", categoria="Audio",
    desc_producto="Auriculares inalámbricos", garantia_producto="6 meses",
    resenias="Buen sonido", precio_unitario=30000, stock=15, iva=21)

lista_productos = [p1, p2, p3, p4, p5]

for producto in lista_productos:
    print(producto)


