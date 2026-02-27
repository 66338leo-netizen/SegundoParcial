import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def sumar():
    try:
        num1=float(entrada1.get())
        num2=float(entrada2.get())
        resultado=num1+num2
        label_resultado.config(text=f"Resultado: {resultado}",font=("Arial", 16,"bold"))

    except ValueError:
        messagebox.showerror("Error","Por favor ingresa numeros validos")

ventana = tk.Tk()
ventana.title("Mi Primera Aplicacion")
ventana.geometry("500x200")

tk.Label(ventana, text="Num1",font=("Arial", 16,"bold")).grid(row=1,column=0)
entrada1=tk.Entry(ventana,font=("Arial", 16,"bold"))
entrada1.grid(row=1,column=3)

tk.Label(ventana, text="Num2",font=("Arial", 16,"bold")).grid(row=3,column=0)
entrada2=tk.Entry(ventana,font=("Arial", 16,"bold"))
entrada2.grid(row=3,column=3)


tk.Button(ventana,text="Sumar", command=sumar).grid(row=8,column=0)

label_resultado= ttk.Label(ventana, text="")
label_resultado.grid(row=8,column=3)


ventana.mainloop()