import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_negativos = 0
        suma_positivos = 0
        cant_positivos = 0
        cant_negativos = 0
        cant_ceros = 0
        dif_positivos_negativos = 0
        
        while True:

            numero = prompt("Numero", "Ingrese un numero: ")

            if numero == None:
                break

            else: 
                numero = int(numero)

                if numero > 0:
                    suma_positivos += numero  #Acumulador

                    cant_positivos += 1       #Contador

                else:
                    if numero < 0:
                        suma_negativos += numero      #Acumulador

                        cant_negativos += 1           #Contador

                    else:                        #Por descarte, la unica opcion que queda es el 0
                        cant_ceros += 1 

            dif_positivos_negativos = cant_positivos - cant_negativos

        msj = f'''La suma acumulada de los números negativos es {suma_negativos}, y la de los positivos es {suma_positivos}. Hay {cant_positivos} positivos, {cant_negativos} negativos y {cant_ceros} ceros. La diferencia entre la cantidad de numeros positivos y negativos es {dif_positivos_negativos} '''


        alert("Ejercicio 10", msj)
           







    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
