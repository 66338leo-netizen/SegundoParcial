import tkinter as tk

def saludo():
    label_resultado.config(text="Hola alumnos de Python")

ventana = tk.Tk()
ventana.title("Mi Primera Aplicacion")
ventana.geometry("100x100")

boton=tk.Button(ventana,text="Saludar", command=saludo)
boton.pack(pady=20)
label_resultado=tk.Label(ventana,text="",font=("Arial",16,"bold"))
label_resultado.pack(pady=20)

ventana.mainloop()