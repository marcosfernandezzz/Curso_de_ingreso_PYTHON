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

        total_kilos_3d = 0

        cant_1_dias = 0
        cant_3_dias = 0
        cant_5_dias = 0

        nombre_mas_altura = "Sin datos"
        dia_mas_elegido = "Sin datos"
        nombre_mas_joven_5 = "Sin datos"
        kilos_mas_joven = 0
        edad_mas_altura = 0

        altura_max = 0
        edad_min = 0



        bandera_altura = True
        bandera_edad = True
        bandera_while = True

        porcentaje_1_dia = 0
        promedio_kilos_3 = 0

        clientes_true_false = question("Cliente", "¿Desea ingresar un nuevo cliente?")

        while clientes_true_false:
            bandera_while = False

            nombre = prompt("Nombre", "Ingrese el nombre del cliente: ")

            edad = prompt("Edad", "Ingrese la edad del cliente: ")
            edad = int(edad)

            while edad <= 12:
                edad = prompt("Edad", "Incorrecto, ingrese una edad válida: ")
                edad = int(edad)

            altura = prompt("Altura", "Ingrese la altura del cliente en M (sin puntos): ")
            altura = float(altura)

            while altura < 1:
                altura = prompt("Altura", "Incorrecto, ingrese una altura válida: ")
                altura = float(altura)

            dias_semana = prompt("Dias a la semana", "Ingrese los dias que asiste el cliente a la semana (1, 3, 5): ") 
            dias_semana = int(dias_semana)

            while dias_semana != 1 and dias_semana != 3 and dias_semana != 5:
                dias_semana = prompt("Dias a la semana", "Incorrecto, ingresar los dias que asiste el cliente a la semana (1, 3, 5): ")
                dias_semana = int(dias_semana)

            kilos_peso_muerto = prompt("Kilos", "Ingrese los kilos que el cliente levanta en peso muerto: ")
            kilos_peso_muerto = int(kilos_peso_muerto)

            while kilos_peso_muerto < 1:
                kilos_peso_muerto = prompt("Kilos", "Incorrecto, ingrese los kilos que el cliente levanta en peso muerto: ")
                kilos_peso_muerto = int(kilos_peso_muerto)

        
            cant_clientes += 1

            if dias_semana == 1:
                cant_1_dias += 1
            else:
                if dias_semana == 3:
                    total_kilos_3d += kilos_peso_muerto
                    cant_3_dias += 1
                else:
                    cant_5_dias += 1
                    if bandera_edad == True:
                        edad_min = edad                         #5)
                        nombre_mas_joven_5 = nombre
                        kilos_mas_joven = kilos_peso_muerto
                    else:
                        if edad < edad_min:
                            edad_min = edad
                            nombre_mas_joven_5 = nombre


            if cant_1_dias > cant_3_dias and cant_1_dias > cant_5_dias: 
                dia_mas_elegido = "Los clientes eligen más ir un día a la semana"
            else:
                if cant_3_dias > cant_1_dias and cant_3_dias > cant_5_dias:
                    dia_mas_elegido = "Los clientes eligen mas ir tres días a la semana"   #4)
                else:
                    dia_mas_elegido = "Los clientes eligen mas ir cinco días a la semana"

            if bandera_altura == True:
                altura_max = altura
                altura_min = altura

                nombre_mas_altura = nombre
                edad_mas_altura = edad

                bandera_altura = False
            else:
                if altura > altura_max:
                    altura_max = altura         #3)
                    nombre_mas_altura = nombre
                    edad_mas_altura = edad


            clientes_true_false = question("Cliente", "¿Desea ingresar un nuevo cliente?")

            

            

            

        if bandera_while == False:
        #1)
            promedio_kilos_3 = total_kilos_3d / cant_3_dias
        #2)
            porcentaje_1_dia = (cant_1_dias * 100) / cant_clientes



        #Respuesta 1)
        print(f"Promedio de kilos que levantan las personas que solo van 3 dias a la semana: {promedio_kilos_3}KG")
        print(f"Porcentaje de personas que solo van 1 día a la semana: {porcentaje_1_dia}%")
        #Respuesta 3)
        print(f"Nombre y edad del cliente con más altura: {nombre_mas_altura} y {edad_mas_altura} años")
        #Respuesta 4)
        print(dia_mas_elegido)
        #Respuesta 5)
        print(f"Nombre y KG que levanta en peso muerto la persona mas joven que solo asista: {nombre_mas_joven_5} y {kilos_mas_joven}KG ")
        








            
            




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
