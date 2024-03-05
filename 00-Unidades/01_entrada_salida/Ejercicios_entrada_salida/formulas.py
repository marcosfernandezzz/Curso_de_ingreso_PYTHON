#WHILE TRUE
'''

nombre = prompt("Nombre", "Ingrese el nombre del cliente: ")

edad = prompt("Edad", "Ingrese la edad del cliente: ")
edad = int(edad)

while edad <= 12:
    edad = prompt("Edad", "Incorrecto, ingrese una edad válida: ")
    edad = int(edad)

while dias_semana != 1 and dias_semana != 3 and dias_semana != 5:
    dias_semana = prompt("Dias a la semana", "Incorrecto, ingresar los dias que asiste el cliente a la semana (1, 3, 5): ")
    dias_semana = int(dias_semana)

cant_personas += 1
'''




#FORMULAS

'''
promedio_kilos_tres_dias = total_kilos_tres_dias / cant_tres_dias     <------ PROMEDIO


porcentaje_un_dia = (cant_un_dias * 100) / cant_clientes             <--------- PORCENTAJE


aumento = (sueldo * incremento_porc) / 100                           <---------- AUMENTO
importe_aumento = sueldo + aumento


descuento = (importe * 20) / 100                                <-------- DESCUENTO
importe_decremento = importe - descuento



'''