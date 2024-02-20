import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
(E/S)
Para saber el costo de un viaje necesitamos el siguiente algoritmo,
sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMP.T
Los datos a solicitar de dos personas son, nombre, edad y peso
Se pide  armar el siguiente mensaje
"Hola German y Marina , sus pesos son 80 kilos y 60 kilos respectivamente
, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos  
'''





class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        nombre1 = str(prompt("Nombre", "Ingrese el nombre de la primer persona: "))
        nombre2 = str(prompt("Nombre", "Ingrese el nombre de la segunda persona: "))
        edad1 = int(prompt("Edad", "Ingrese la edad de la primer persona: "))
        edad2 = int(prompt("Edad", "Ingrese la edad de la segunda persona: "))
        peso1 = int(prompt("Peso", "Ingrese el peso de la primer persona: "))       
        peso2 = int(prompt("Peso", "Ingrese el peso de la segunda persona: "))

        suma_peso = peso1 + peso2
        prom_edad = (edad1 + edad2) / 2

        viaje = suma_peso / 1000


        msj = f'''Hola {nombre1} y {nombre2}, sus pesos son {peso1} kilos y {peso2} respectivamente, sumados da {suma_peso} kilos, 
        el promedio de edad es {prom_edad} y su viaje cuesta {viaje} pesos.'''
        
        alert("Viaje", msj)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()