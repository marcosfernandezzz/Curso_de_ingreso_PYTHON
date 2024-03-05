import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
 edad(mayor a 0)
pedir datos por prompt y mostrar por print
Punto A-informar cual fue el sexo mas ingresado
Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

Punto C - por el número de DNI del alumno
DNI terminados en  0 o 1

1)informar la cantidad de personas de sexo  femenino
2) la edad promedio de  personas de sexo  masculino
3) el nombre de la persona la persona de sexo  nb con más temperatura(si la hay)


DNI terminados en  2 o 3

1) informar la cantidad de personas de sexo  masculino
2) la edad promedio de  personas de sexo  nb
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)


DNI terminados en  4 o 5

1)informar la cantidad de personas de sexo  nb
2) la edad promedio de  personas de sexo  femenino
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)


DNI terminados en  6 o 7

1)informar la cantidad de personas mayores de edad (desde los 18 años)
2)la edad promedio en total de todas las personas mayores de edad (18 años)
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)


DNI terminados en  8 o 9

1))informar la cantidad de personas menores de edad (menos de 18 años)
2)la temperatura promedio en total de todas las personas menores de edad
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)


Todos los alumnos: 
B-informar cual fue el sexo mas ingresado
C-el porcentaje de personas con fiebre y el porcentaje sin fiebre


'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        cant_personas = 0

        sexo_mas_ingresado = ""
        nombre_femenino_menos_temp = "Sin datos"

        porcentaje_con_fiebre = 0
        porcentaje_sin_fiebre = 0

        bandera_temp = False

        cant_masculino = 0
        cant_femenino = 0
        cant_nb = 0
        cant_fiebre = 0
        cant_sin_fiebre = 0
        edad_total_nb = 0

        temp_min = 0

        for i in range(0,5):
            nombre = prompt("Nombre", "Ingrese el nombre del paciente: ")

            sexo = prompt("Sexo", "Ingrese el sexo del paciente (m, f, nb): ")
            sexo = sexo.lower()

            while sexo != "m" and sexo != "f" and sexo != "nb":
                sexo = prompt("Sexo", "Incorrecto, ingrese nuevamente el sexo del paciente (m, f, nb): ")
                sexo = sexo.lower()

            edad = prompt("Edad", "Ingrese la edad del paciente: ")
            edad = int(edad)

            while edad < 0:
                edad = prompt("Edad", "Incorrecto, ingrese nuevamente la edad del paciente: ")
                edad = int(edad)

            temperatura = prompt("Temperatura corporal", "Ingrese la temperatura corporal del paciente: ")
            temperatura = int(temperatura)

            while temperatura < 35 or temperatura > 42:
                temperatura = prompt("Temperatura", "Incorrecto, ingrese nuevamente la temperatura corporal del paciente: ")
                temperatura = int(temperatura)

            cant_personas += 1
            

            if sexo == "m":
                cant_masculino += 1
            else:
                if sexo == "f":
                    cant_femenino += 1
                    if bandera_temp == False:
                        temp_min = temperatura
                        nombre_femenino_menos_temp = nombre
                        bandera_temp = True
                    else:
                        if temperatura < temp_min:
                            temp_min = temperatura
                            nombre_femenino_menos_temp = nombre
                else: 
                    cant_nb += 1
                    edad_total_nb += edad

            if cant_masculino > cant_femenino and cant_masculino > cant_nb:
                sexo_mas_ingresado = "Masculino"
            else:
                if cant_femenino > cant_masculino and cant_femenino > cant_nb:
                    sexo_mas_ingresado = "Femenino"
                else: 
                    sexo_mas_ingresado = "No binario"

            if temperatura > 37:
                cant_fiebre += 1
            else:
                cant_sin_fiebre += 1

        porcentaje_con_fiebre = (cant_fiebre * 100) / cant_personas
        porcentaje_sin_fiebre = (cant_sin_fiebre * 100) / cant_personas

        promedio_edad_nb = edad_total_nb / cant_nb

        print("Sexo mas ingresado: ", sexo_mas_ingresado)
        print("Porcentaje con fiebre: ", porcentaje_con_fiebre)
        print("Porcentaje sin fiebre: ", porcentaje_sin_fiebre)
        print("Cantidad de personas de sexo masculino: ", cant_masculino)
        print("Edad promedio de personas de sexo no binario: ", promedio_edad_nb)
        print("Nombre de la persona de sexo  femenino  con la temperatura mas baja: ", nombre_femenino_menos_temp)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

#https://onlinegdb.com/n8ho1oTiYQ#
