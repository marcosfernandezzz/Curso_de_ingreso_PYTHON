import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
El siguiente ejercicio debe tener un solo alert escrito en el código
SI SI , uno solo.
La palabra alert escrita una sola vez.
Si si nuevamente , una sola vez en todo su código

Ejercicio 07 BIS V1 (Realizar en los archivos  del ejercicio 07 del IF):

1. Si es menor de 13 , mostrar el mensaje “feliz día”.
2.Si es adolescente el mensaje es “usted es adolescente”
  a. Si tiene 17 años además mostrar el mensaje “último año!!!”
3. Si es mayor de edad mostrar el mensaje “tenes edad de laburar”.
  a. Si tiene 33 años , además mostrar el mensaje “como cristo”
  b. Si tiene más de 60 años, además mostrar el mensaje “A jubilarse”.
  c. Si tiene 88, además mostrar el mensaje “lindo número''
4.Si la edad es par , además mostrar , “sos par!!”.

'''




class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Tipo")
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.combobox_tipo = customtkinter.CTkComboBox(master=self, values=["NATIVO", "NATURALIZADO"])
        self.combobox_tipo.grid(row=1, column=1, padx=20, pady=10)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad = int(self.txt_edad.get())


        if edad < 13:
            msj = "feliz día"

        elif edad <= 17:
            msj = "usted es adolescente"
            if edad == 17:
                msj += " último año!!!"
        else:
            msj = "tenes edad de laburar"
            if edad == 33:
                msj += " como cristo"
            elif edad > 60: 
                msj += " A jubilarse"
                if edad == 88:
                    msj += " lindo número"
        
        if (edad % 2) == 0:
            msj += " sos par!!"

        alert("Alert", msj)
        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

    '''
    Menor = edad < 13 "feliz dia"
    adolescente = edad > 13 y edad <= 17. Si edad == 17 "útimo año!!!"
    mayor = edad >= 18, "tenes edad de laburar". Si edad == 33 "como cristo". Si edad > 60 "A jubilarse". Si edad == 88 "lindo numero"

    par o impar = Si (edad % 2) == 0 es par, sino impar
 
    '''