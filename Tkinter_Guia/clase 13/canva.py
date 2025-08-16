import tkinter as tk



ventana=tk.Tk()


canvas=tk.Canvas(ventana,width=500,height=500,background="blue")
canvas.pack()

rentangulo = canvas.create_rectangle(50,50,150,150,fill="red",outline="black",width=5)

#si creamos una variable podemos decirle a esta que cree un rectangulo 
#obvio este rectangulo se crea dentro del canvas
# estos son los siguientes parametros
# el primero es la coordenada X
# el segundo es la coordenada Y
# el tercero es el tamano en X
# el cuarto es el tamano en Y
# el fill es el color de relleno
# el outline es el color del borde
# el width es el tamano del borde

canvas.move(rentangulo,0,50) #con esto podemos mover el rectangulo dentro del canvas a las coordenadas que nosotros le digamos

ovalo = canvas.create_oval(50,50,150,150,fill="yellow",outline="black",width=5)

# con esto podemos crear un ovalo dentro del canvas
# los parametros son los mismos que el rectangulo

poligono= canvas.create_polygon(350,50,400,100,350,150,fill="green",outline="black",width=5)
# con esto podemos crear un poligono dentro del canvas
# los parametros son los mismos que el rectangulo pero en este caso podemos agregar mas puntos para crear el poligono 
# en este caso el poligono tiene 3 puntos   

linea = canvas.create_line(10,300,100,300,fill="white",width=5)

# con esto podemos crear una linea dentro del canvas
# los parametros son los mismos que el rectangulo pero en este caso solo necesitamos 2 puntos   
# en este caso la linea tiene 2 puntos








ventana.mainloop()