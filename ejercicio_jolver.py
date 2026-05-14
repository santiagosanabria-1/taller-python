n = int(input("Cuantos equipos hay en tu empresa :"))

emisiones_equipo = 0
emisiones_totales = 0
for i in range(n):
        
    nombre = input(f"Introduzca el nombre del equipo {i+1} : ")
    cantidad = int(input(f"Ingrese la cantidad de de equipos : "))
    potencia = int(input(f'Ingrese el nivel de pontencia del equipo {i+1} : '))
    horas = int(input(f'Ingrese la cantidad de horas que se utiliza el equipo {i+1} : '))
    dias = int(input(f'Ingrese la cantidad de dias al año que se utiliza el equipo {i+1} : '))
    factor = input(f'Ingrese el Factor del equipo {i+1} : ')

    potencia_total = cantidad * potencia
    potencia_KW = potencia_total / 1000
    energia = potencia_KW * horas * dias

    emisiones = energia * factor
    emisiones_totales = emisiones + emisiones

print(f'La cantidad de emisiones totales son : {emisiones_totales}')
