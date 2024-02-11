import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
A)
La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer 
qué cantidad de materiales se necesita para la fabricación de distintos juguetes

La estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) 
del mismo material.
El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará 
un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. 
Tener en cuenta que los valores de entrada están expresados en Cms

AB = Diágonal mayor
DC = Diágonal menor
BD y BC = lados menores
AD y AC = lados mayores
---------
B)
Luego, necesitaremos saber cuánto papel de cada color necesitamos. Las entradas son las mismas.
---------
TODOS LOS DATOS SE INGRESAN CON PROMPT
'''
#dsds

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        AD = int(prompt("Lados mayores", "Ingrese la longitud de los lados mayores en cm (AD y AC): "))
        BD = int(prompt("Lados menores", "Ingrese la longitud de los lados menores en cm (BD y BC): "))
        
        AB = int(prompt("Diagonal mayor", "Ingrese la diagonal mayor (AB):"))
        DC = int(prompt("Diagonal menor", "Ingrese la diagonal menor (DC):"))

        varillas_cm = (BD * 2)  + (AD * 2) + AB + DC

        #Multiplicar por 10 unidades

        varillas_10u = varillas_cm * 10
        varillas_m = float(varillas_10u / 100)


        papel_area = (AB * DC) / 2 

        porc_cola = (papel_area * 10) / 100
        papel_total_unidad = papel_area + porc_cola

        papel_10u = papel_total_unidad * 10

        #Multiplicar por 10 unidades de cometa

        papel_colores_cu = papel_area / 2   #Saco el papel_cola porque no esta especificado en el ejercicio


        papel_colores_total = papel_colores_cu * 10

        msj = f"Segun los datos ingresados, se necesitarán {varillas_m} M de varillas de plastico y {papel_10u / 100} M de papel."
        msj2 = f"\nEn total se deberán utilizar {papel_colores_total / 100} M para cada color"

        alert("Resultado del cálculo", msj + msj2)





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

#Area de los dos triangulos para sacar los colores
#1. Lado mayor
'''
        Ac = math.sqrt((DC ** 2) + (AD ** 2))
        h1 = DC / 2   #Se divide por dos ya que es la mitad de la diagonal menor

        area_mayor = (Ac * h1) / 2
        
        #2. Lado menor
 
        Bc = math.sqrt((BD ** 2) + (DC ** 2))
        area_menor = (h1 * Bc) / 2  #Se utiliza la mitad de la diagonal menor como base

        area_colores = area_menor + area_mayor
        area_colores_m = float(area_colores * 100)
'''