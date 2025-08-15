import tkinter as tk

ventana=tk.Tk()
ventana.title("ejemplo de pack")

label1=tk.Label(ventana,text="label 1")
label1.pack()

label2=tk.Label(ventana,text="label 2")
label2.pack()

#se guarda dentro de un frame

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

#van a venir los botones uno despues de otro dependiendo de que side le pongas
boton1 = tk.Button(frame_botones, text="Botón 1")
boton1.pack(side="left", padx=5)

boton2 = tk.Button(frame_botones, text="Botón 2")
boton2.pack(side="left", padx=5)

boton3 = tk.Button(frame_botones, text="Botón 3")
boton3.pack(side="left", padx=5)

ventana.mainloop()