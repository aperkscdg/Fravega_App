import tkinter as tk
from tkcalendar import Calendar

ventana = tk.Tk()
#con el calendar se crea un calendario, con el selectmode le asignas si el usuario puede elegir el dia o no
#con el locale el horario del pais
#con el year . moonth y el day en donde se encontrara el horario por defecto, aunque si no lo pones se pone el horario actual
#con el date paatter el orden del calendario
cal = Calendar(ventana, selectmode='day', locale='es_ES', year=2023, month=7, day=1, date_pattern='dd-mm-y')
cal.pack()

def print_date(date):
    print(date)
#evento de que dia elegimos se printea
cal.bind("<<CalendarSelected>>", lambda e: print_date(cal.get_date()))

ventana.mainloop()