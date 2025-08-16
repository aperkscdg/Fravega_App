import tkinter as tk

ventana =tk.Tk()

canvas = tk.Canvas(ventana,width=500,height=500,background="black")
canvas.pack()

objeto_sellecionado = None

rentangulo = canvas.create_rectangle(100,100,200,200, fill="blue",tags="rentangulo")

def iniciar_arrastre(event):
    global objeto_sellecionado
    objeto_sellecionado = canvas.find_closest(event.x,event.y)


def Terminar_arrastre(event):
    global objeto_sellecionado
    if objeto_sellecionado:
        x , y = event.x , event.y
        canvas.move(objeto_sellecionado, x - canvas.coords(objeto_sellecionado)[0], y - canvas.coords(objeto_sellecionado)[1])
        objeto_sellecionado=None


canvas.tag_bind("rentangulo","<ButtonPress-1>",iniciar_arrastre)
canvas.tag_bind("rentangulo","<ButtonRelease-1>", Terminar_arrastre)





ventana.mainloop()