print('=' * 35)
print('HOLA ESTIMADO USUARIO')
print('=' * 35)
n = int(input('Cuantos dispositivos desea analizar : '))
totaldeemiciones = 0

for i in range(n):
    nombre = input(f'Nombre del equipo {i + 1} : ')
    cantidad = int(input('Ingrese la cantidad de dispositivos : '))
    potencia = int(input('Ingrese la potencia de los dispositivos [W] : '))
    horas = int(input('Ingrese la cantidad de horas que se utilizan los dispositivos : '))
    dias = int(input('Ingrese la cantidad de dias que se utiliza el equipo : '))
    tasasC02 = float(input('Ingrese la tasa del c02 : '))

potenciattl = cantidad * potencia
kw = potenciattl / 1000

energia = kw * horas * dias
c02 = energia * tasasC02
print('=' * 35)
print(f'Total de emisiones al año de {c02} co2 de tu equipo llamada {nombre}')
print('=' * 35)


