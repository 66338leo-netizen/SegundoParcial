import tkinter as tk
from tkinter import ttk

def mostrar_texto():
    texto=entrada.get()
    label_resultado.config(text=f"Escribiste: {texto}")

ventana=tk.Tk()
ventana.title("Ejemplo con Entry")
ventana.geometry("100x100")

entrada=tk.Entry(ventana,font=("Arial",16,"bold"))
entrada.pack(pady=20)

boton=tk.Button(ventana,text="Enviar",command= mostrar_texto())
boton.pack(pady=20)

label_resultado=ttk.Label(ventana, text="")
label_resultado.pack(pady=20)

ventana.mainloop


