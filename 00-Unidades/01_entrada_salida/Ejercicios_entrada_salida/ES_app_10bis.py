import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marcos  
apellido: Fernandez
---
Ejercicio: entrada_salida_10bis
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txt_importe y txt_descuento), 
transformarlos en números y mostrar el importe actualizado con el descuento utilizando el Dialog Alert.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Importe")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_importe = customtkinter.CTkEntry(master=self)
        self.txt_importe.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(
            master=self, text="% de Descuento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_descuento = customtkinter.CTkEntry(master=self)
        self.txt_descuento.grid(row=1, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        importe = float(self.txt_importe.get())
        descuento_porc = int(self.txt_descuento.get())

        descuento = (importe * descuento_porc) / 100
        importe_incremento = importe - descuento

        alert("Importe con descuento", f"El importe de ${importe} con el descuento del {descuento_porc}% sera de ${importe_incremento}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
