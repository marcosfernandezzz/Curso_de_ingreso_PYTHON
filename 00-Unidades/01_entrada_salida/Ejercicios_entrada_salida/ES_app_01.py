import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marcos
apellido: Fernandez
---
Ejercicio: entrada_salida_01
---
Enunciado:
        
        Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

    Nombre   
    Edad (debe ser mayor a 12)
    Altura (no debe ser negativa)
    Días que asiste a la semana (1, 3, 5)
    Kilos que levanta en peso muerto (no debe ser cero, ni negativo)
No sabemos cuántos clientes serán consultados.
Se debe informar al usuario:
El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

El porcentaje de clientes que asiste solo 1 día a la semana.

Nombre y edad del cliente con más altura.

Determinar si los clientes eligen más ir 1, 3 o 5 días

Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''  

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        cant_clientes = 0
        cant_un_dias = 0
        cant_tres_dias = 0
        cant_cinco_dias = 0
        
        total_kilos_tres_dias = 0

        nombre_mas_altura = ""
        edad_mas_altura = 0

        edad_mas_joven_cinco_dias = 0
        nombre_mas_joven_cinco_dias = "Sin datos"
        kilos_mas_joven_cinco_dias = 0

        altura_max = 0
        edad_min_cinco_dias = 0

        bandera_altura = True
        bandera_edad = True

        nuevo_cliente = question("Cliente", "¿Desea ingresar un nuevo cliente?")

        while nuevo_cliente == True:
            nombre =  prompt("Nombre", "Ingrese el nombre: ")

            edad = prompt("Edad", "Ingrese la edad: ")
            edad = int(edad)

            while edad < 12:
                edad = prompt("Edad", "Incorrecto, ingrese la edad: ")
                edad = int(edad)

            altura = prompt("Altura", "Ingrese la altura del cliente en M (sin puntos): ")
            altura = float(altura)

            while altura < 0:
                altura = prompt("Altura", "Incorrecto, ingrese una altura válida: ")
                altura = float(altura)

            while altura < 0:
                altura = prompt("Altura", "Incorrecto, ingrese la altura: ")
                altura = float(edad)

            dias_semana = prompt("Dia", "Ingrese cuantos dias a la semana asiste: ")
            dias_semana = int(dias_semana)

            while dias_semana != 1 and dias_semana != 3 and dias_semana != 5:
                dias_semana = prompt("Letra", "Incorrecto, ingrese cuantos diass a la semana asiste (1, 3 o 5): ")
                dias_semana = int(dias_semana)

            kilos = prompt("Altura", "Ingrese los kilos que levanta en peso muerto: ")
            kilos = float(kilos)

            while kilos < 1:
                kilos = prompt("Altura", "Incorrecto, ingrese los kilos que levanta en peso muerto: ")
                kilos = float(edad)

            cant_clientes += 1

            nuevo_cliente = question("Cliente", "¿Desea ingresar un nuevo cliente?")


            if dias_semana == 1:
                cant_un_dias += 1

            elif dias_semana == 3:               
                cant_tres_dias += 1

                total_kilos_tres_dias += kilos

            
            else:
                cant_cinco_dias += 1

                if bandera_edad == True:
                    edad_mas_joven_cinco_dias = edad
                    nombre_mas_joven_cinco_dias = nombre
                    kilos_mas_joven_cinco_dias = kilos

                    bandera_edad = False
                else:
                    if edad < edad_min_cinco_dias:
                        edad_min_cinco_dias = edad
                        nombre_mas_joven_cinco_dias = nombre
                        kilos_mas_joven_cinco_dias = kilos

            
            if bandera_altura == True:
                altura_max = altura
                nombre_mas_altura = nombre
                edad_mas_altura = edad


                bandera_altura == False
            else:
                if altura > altura_max:
                    altura_max = altura
                    nombre_mas_altura = nombre
                    edad_mas_altura = edad

            
            if cant_un_dias > cant_tres_dias and cant_un_dias > cant_cinco_dias:
                dias_mas_asistidos = "Los clientes asisten mayormente un dia por semana"
            elif cant_tres_dias > cant_un_dias and cant_tres_dias > cant_cinco_dias:
                dias_mas_asistidos = "Los clientes asisten mayormente tres dias por semana"
            else: 
                dias_mas_asistidos = "Los clientes asisten mayormente cinco dias por semana"

            


        #1)
                
        if cant_tres_dias != 0:
            promedio_kilos_tres_dias = total_kilos_tres_dias / cant_tres_dias  
            print(f"Promedio de kilos que levantan las personas que asisten solo 3 días a la semana: {promedio_kilos_tres_dias}")

        #2)
        if cant_un_dias != 0:
            porcentaje_un_dia = (cant_un_dias * 100) / cant_clientes
            print(f"Porcentaje de clientes que asiste solo 1 día a la semana: {porcentaje_un_dia}")

        #3)
        print(f"Nombre y edad del cliente con más altura: {nombre_mas_altura} y {edad_mas_altura} años")

        #4)
        print(dias_mas_asistidos)

        #5)
        print(f"Nombre y cantidad de kilos levantados en peso muerto de la persona más joven que solo asista 5 días a la semana: {nombre_mas_joven_cinco_dias} y {kilos_mas_joven_cinco_dias}KG")




            




        #CTRL + D + D + D ----> selecciona la palabra que esta parada el cursor y podes editarlas a la vez

        #Ej 4 y 5 de while copiar los tipos de validaciones
        







#Para sacar un porcentaje se necesita variable_especifica
            
#https://onlinegdb.com/6dMXAB3dw




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
