import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Ingresar el valor del dólar oficial y el valor del dólar blue.
Mostrar la diferencia expresada en porcentaje entre una cotización y otra.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        dolar_oficial = float(prompt("Dolar oficial", "Ingrese el valor del dolar oficial"))
        dolar_blue = float(prompt("Dolar blue", "Ingrese el valor del dolar blue"))

        porcentaje_dolares = (dolar_blue / dolar_oficial) * 100

        dif_porcentaje = porcentaje_dolares - 100


        alert("Diferencia porcentual", f"La diferencia porcentual es: {porcentaje_dolares}%")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
