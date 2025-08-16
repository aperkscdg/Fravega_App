import tkinter as tk

ventana=tk.Tk()

canvas = tk.Canvas(ventana,width=500,height=500,bg="blue")
canvas.pack(fill="both",expand=True)


canvas.create_text(150,50,text="holaaaaa soy un texto", fill="darkgreen",font=("Arial", 12, "italic"), justify="center" )

#esto crea un texto en el canvas 
# el primer parametro es la coordenada x y el segundo la coordenada y 
#el tercer parametro es el texto, 
# el fill es el color del texto
# el quinto es la fuente que se va a usar
# y el ultimo si el texto va a estar justificado en el centro


ventana.mainloop()