import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1=float(entrada1.get())
        num2=float(entrada2.get())
        operacion= opcion.get()

        if operacion==1:
            resultado=num1+num2
        elif operacion==2:
            resultado=num1-num2
        elif operacion==3:
            resultado=num1*num2
        elif operacion==4:
            if num2==0:
                messagebox.showerror("Error","No se puede dividir entre cero")
                return
            resultado=num1/num2
        else:
            messagebox.showerror("Advertencia","Slecciona una operacion")
            return
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa numeros validos")


ventana=tk.Tk()
ventana.title("Calculadora de Radiobotones")
ventana.geometry("350x300")

tk.Label(ventana,text="Primer numero:").grid(row=3,column=0)
entrada1=tk.Entry(ventana)
entrada1.grid(row=3,column=1)

tk.Label(ventana,text="Segundo numero:").grid(row=5,column=0)
entrada2=tk.Entry(ventana)
entrada2.grid(row=5,column=1)

opcion=tk.IntVar()

tk.Label(ventana, text="Selecciona la operacion: ").grid(row=7,column=1)

tk.Radiobutton(ventana, text="Suma",variable=opcion, value=1).grid(row=9,column=0,columnspan=1)
tk.Radiobutton(ventana, text="Resta",variable=opcion, value=2).grid(row=11,column=0,columnspan=1)
tk.Radiobutton(ventana, text="Multiplicacion",variable=opcion, value=3).grid(row=9,column=2,columnspan=2)
tk.Radiobutton(ventana, text="Division",variable=opcion, value=4).grid(row=11,column=2,columnspan=2)

tk.Button(ventana, text="Calcular", command=calcular).grid(row=13,column=1)

etiqueta_resultado=tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.grid(row=15,column=1,pady=10)

ventana.mainloop()