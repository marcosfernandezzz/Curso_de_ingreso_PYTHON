import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente  (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

                                                                            ##APELLIDO##

        apellido = prompt("Apellido", "Ingrese su apellido: ")

        while apellido == None or apellido == "":
            apellido = prompt("Apellido", "Ingrese su apellido: ")

        apellido = apellido.lower()
        
        # while True:
        #     apellido = prompt("Apellido", "Ingrese su apellido: ")    ##OR PORQUE UNA DE LAS DOS CONDICIONES TIENE QUE SER TRUE PARA QUE SE EJECUTE EL IF

        #     if apellido == None or apellido == "":
        #         break
        #     else:
        #         apellido = apellido.lower()
        #         break                                          ##Ctrl + K + C para comentar multiple


                                                                                ##EDAD##

        # while True:                                                   ##WHILE TRUE
        #     edad = prompt("Edad", "Ingrese su edad: ")            

        #     if edad == None:
        #         continue

        #     edad = int(edad)

        #     if edad <= 18 or edad >= 90:
        #         continue
        #     else:
        #         break

        edad = prompt("Edad", "Ingrese su edad: ")

        while edad == None or edad == "":                                              ##WHILE CONDICION
            edad = prompt("Edad", "Incorrecto, ingrese su edad nuevamente: ")       

        edad = int(edad)

        while edad < 18 or edad > 90:    #Cuando es menor a 18 "O" mayor a 90 (es decir, fuera del rango pedido), se ejecuta el bloque del while para pedir denuevo la edad
            edad = prompt("Edad", "Incorrecto, ingrese su edad nuevamente: ")

            if edad == "":
                edad = 0
                continue
            
            edad = int(edad)

            if edad == 0:
                continue

                                                                            ##ESTADO CIVIL##
            
        # estado_civil = prompt("Estado civil", "Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a y Viudo/a): ")
        # estado_civil = estado_civil.lower()
            
        # while estado_civil == None or (estado_civil != "soltero" and estado_civil != "soltera" and estado_civil != "casado" and estado_civil != "casada" and estado_civil != "viudo" and estado_civil != "viuda" and estado_civil != "divorciado" and estado_civil != "divorciada"):
        #     estado_civil = prompt("Estado civil", "Incorrecto, ingrese nuevamente su estado civil (Soltero/a, Casado/a, Divorciado/a y Viudo/a): ")

        # match estado_civil:
        #     case "soltero" | "soltera":
        #         estado_civil = "Soltero/a"
        #     case "casado" | "casada":
        #         estado_civil = "Casado/a"
        #     case "divorciado" | "divorciada":
        #         estado_civil = "Divorciado/a"
        #     case "viudo" | "viuda":
        #         estado_civil = "Viudo/a"
            

        bandera_estado_civil = False
        # prompt("Ingrese Valor", "Ingrese su estado civil")
        while bandera_estado_civil == False:
            estado_civil = prompt("Ingrese Valor", "Ingrese su estado civil")

            if estado_civil == None:
                continue
            estado_civil = estado_civil.lower()

            # Voy a CHEQUEAR QUE EL ESTADO CIVIL SEA CORRECTO
            match estado_civil:
                case "casado" | "casada":
                    bandera_estado_civil = True         #Si la bandera es TRUE, entonces estado_civil es correcto
                    estado_civil = "Casado/a"          
                case "soltero" | "soltera":
                    bandera_estado_civil = True
                    estado_civil = "Soltero/a"
                case "divorciado" | "divorciada":
                    bandera_estado_civil = True
                    estado_civil = "Divorciado/a"
                case "viudo" | "viuda":
                    bandera_estado_civil = True
                    estado_civil = "Viudo/a"
                case _:
                    estado_civil = prompt("Ingrese Valor", "Ingrese su estado civil")

                                                                                ##LEGAJO##

            # legajo = prompt("Legajo", "Ingrese su numero de legajo (sin ceros a la izquierda): ")
            # legajo = int(legajo)  

            #            #FALSE#                   #TRUE           
            # #             |                #False  |        #True      
            # #             V                   |     v        |
            # while legajo == None or (legajo < 1000 or legajo > 9999):   #legajo = 11111 -----> Como es TRUE, se ejecuta el while
            #     legajo = prompt("Legajo", "Incorrecto, ingrese el número de legajo nuevamente: ")
            #     legajo = int(legajo)
            while True:
                legajo = prompt("Legajo", "Ingrese su numero de legajo: ")

                if legajo == None:
                    continue

                legajo = int(legajo)

                if legajo >= 1000 and legajo <= 9999:      #legajo = 1111    Como las dos condiciones son verdaderas, el "AND" es TRUE, por lo tanto tira el BREAK
                    break



        apellido_txt = self.txt_apellido.delete(0,100)
        apellido_txt = self.txt_apellido.insert(0, apellido.upper())

        edad_txt = self.txt_edad.delete(0,100)
        edad_txt = self.txt_edad.insert(0, edad)  

        estado_civil_txt = self.combobox_tipo.set(estado_civil)

        legajo_txt = self.txt_legajo.delete(0, 100)
        legajo_txt = self.txt_legajo.insert(0, legajo)

            




                
        
        






        # https://onlinegdb.com/yxJxQE1kOa



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
