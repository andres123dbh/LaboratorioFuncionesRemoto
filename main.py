def funcion(a,b):
    resultado = a
    for i in range(1,b):
        resultado=resultado*a
    return resultado

contador_potencia=0
contador_pares=0
contador_impares=0

while True:
    try:
        a=int(input("Ingresar el numeroa elevar: "))
        b=int(input("Ingresar el numeroa por el que se elevara: "))
        break
    except ValueError:
        print("No son validos.Intente denuevo")
while a != 0:
    resultado=funcion(a,b)
    print(resultado)
    contador_potencia += 1
    if resultado%2==0 :
        contador_pares += 1
    else:
        contador_impares += 1
    print("Se calcularon ",contador_potencia," potencias")
    print("Se calcularon ",contador_pares," potencias pares")
    print("Se calcularon ",contador_impares," potencias impares")
    while True:
        try:
            a=int(input("Ingresar el numeroa elevar: "))
            b=int(input("Ingresar el numeroa por el que se elevara: "))
            break
        except ValueError:
            print("No son validos.Intente denuevo")