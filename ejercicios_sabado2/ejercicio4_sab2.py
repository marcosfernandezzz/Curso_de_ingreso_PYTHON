import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter



'''
Se pide ingresar un numero del 100 al 1000 inclusive y informar desde el cero a ese número:
a- Cuántos pares hay 
b- Cuantos multiplos de 5  
c- La suma de los números divisibles por 100
d- La suma acumulada de todos los números 
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador = 0
        contador_pares = 0
        contador_mult_cinco = 0
        contador_divisibles = 0
        sumatoria = 0

        numero = prompt("Número", "Ingresar un número del 100 al 1000:")
        numero = int(numero)
        
        while (numero <= 100 or numero >= 1000):
            numero = prompt("Incorrecto", "Ingresar un número del 100 al 1000:")
            numero = int(numero)

        while contador <= numero:

            if contador % 2 == 0:
                contador_pares += 1
            
            if contador % 5 == 0:
                contador_mult_cinco += 1
            

            if contador % 100 == 0:
                contador_divisibles += contador

            contador += 1  

            sumatoria += contador



            
        msj = f"Hay {contador_pares} pares, {contador_mult_cinco} multiplos de 5, la suma de todos los numeros divisibles por 100 da {contador_divisibles},\n y la sumatoria de todos los numeros da {sumatoria} "

        alert("UTN", msj)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()



