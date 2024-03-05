import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marcos  
apellido: Fernandez
---
Ejercicio: entrada_salida_03
---
Enunciado:
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        cant_mascotas = 0

        cant_f = 0
        cant_m = 0
        sexo_menos_ingresado = ""

        cant_perro = 0
        cant_gato = 0
        cant_exotico = 0

        bandera_peso = True
        peso_min = 0
        nombre_menos_pesada = ""
        tipo_menos_pesada = ""

        edad_min_perro = 0
        nombre_perro_mas_joven = "Sin datos"
        bandera_edad_perro = True

        total_peso = 0

        while cant_mascotas < 5:
            nombre = prompt("Nombre", "Ingrese el nombre de la mascota: ")

            edad = prompt("Edad", "Ingrese la edad de la mascota: ")
            edad = int(edad)

            while edad < 0:
                edad = prompt("Edad", "Incorrecto, ingrese  nuevamente la edad de la mascota: ")
                edad = int(edad)

            sexo = prompt("Sexo", "Ingrese el sexo de la mascota (F o M): ")
            sexo = sexo.upper()

            while sexo != "F" and sexo != "M":
                sexo = prompt("Sexo", "Incorrecto, ingrese nuevamente el sexo de la mascota (F o M): ")
                sexo = sexo.upper()

            tipo = prompt("Tipo", "Ingrese el tipo de mascota (gato, perro o exotico): ")
            tipo = tipo.lower()

            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = prompt("Tipo", "Incorrecto, ingrese nuevamente el tipo de mascota (gato, perro o exotico):")
                tipo = tipo.lower()

            peso = prompt("Peso", "Ingrese el peso de la mascota: ")
            peso = float(peso)

            while peso < 10 or peso > 80:
                peso = prompt("Peso", "Incorrecto, ingrese nuevamente el peso de la mascota: ")
                peso = float(peso)

            cant_mascotas += 1    #Contador

            total_peso += peso    #Acumulador

            if sexo == "M":
                cant_m += 1
            else:
                cant_f += 1


            if cant_f < cant_m:
                sexo_menos_ingresado = f"El sexo menos ingresado es: M"
            else:
                if cant_m < cant_f:
                    sexo_menos_ingresado = "El sexo menos ingresado es: F"

            if tipo == "perro":
                cant_perro += 1
                if bandera_edad_perro == True:
                    nombre_perro_mas_joven = nombre
                else:
                    if edad < edad_min_perro:
                        nombre_perro_mas_joven = nombre
            elif tipo == "gato":
                cant_gato += 1
            else:
                cant_exotico += 1


            if bandera_peso == True:
                peso_min = peso
                nombre_menos_pesada = nombre
                tipo_menos_pesada = tipo

                bandera_peso = False

            else:
                if peso < peso_min:
                    peso_min = peso
                    nombre_menos_pesada = nombre
                    tipo_menos_pesada = tipo


        promedio_peso_total = total_peso / cant_mascotas


        #B)
        if cant_gato != 0:
            porcentaje_gato = (cant_gato * 100) / cant_mascotas
            print(f"El porcentaje de gatos es: {porcentaje_gato}%")
        if cant_perro != 0: 
            porcentaje_perro = (cant_perro * 100) / cant_mascotas
            print(f"El porcentaje de perros es: {porcentaje_perro}%")
        if cant_exotico != 0:
            porcentaje_exotico = (cant_exotico * 100) / cant_mascotas
            print(f"El porcentaje de exoticos es: {porcentaje_exotico}%")


        

            
            #A)
            print(sexo_menos_ingresado)
            #C)
            print(f"El nombre y tipo de la mascota menos pesada es: {nombre_menos_pesada} y {tipo_menos_pesada}")
            #D)
            print(f"El nombre del perro mas joven es: {nombre_perro_mas_joven}")
            #E)
            print(f"El promedio de los pesos de todas las mascotas da como resultado: {promedio_peso_total}KG")



        


                
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()