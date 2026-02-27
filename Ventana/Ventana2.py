import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Primera Aplicacion")
ventana.geometry("100x100")
etiqueta=tk.Label(ventana, text="Hola mundo",font=("Arial", 16,"bold"))

etiqueta.pack(pady=26)
ventana.mainloop()
