import tkinter as tk
ventana = tk.Tk()

scrollbar_horizontal = tk.Scrollbar(ventana, orient=tk.HORIZONTAL)
scrollbar_horizontal.pack(fill="x")

ventana.mainloop()