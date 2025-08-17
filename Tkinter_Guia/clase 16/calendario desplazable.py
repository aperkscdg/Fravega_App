import tkinter as tk
from tkcalendar import DateEntry

ventana = tk.Tk()
#con el date entry hace que se haga un cuadro de texto con un horario desplazable
date_entry = DateEntry(ventana, selectmode="day", locale="es_ES", year=2023, month=7, day=1, date_pattern='dd-mm-y')
date_entry.pack()
#con esto hse imprimira el dia que el usuaario selecione
date_entry.bind("<<DateEntrySelected>>", lambda e: print(date_entry.get()))

ventana.mainloop()