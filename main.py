def funcion(a,b):
    resultado = a
    for i in range(1,b):
        resultado=resultado*a
    return resultado
a=int(input("Ingresar el numeroa elevar: "))
b=int(input("Ingresar el numeroa por el que se elevara: "))
resultado=funcion(a,b)
print(resultado)
while a != 0:
    a=int(input("Ingresar el numeroa elevar: "))
    b=int(input("Ingresar el numeroa por el que se elevara: "))
    resultado=funcion(a,b)
    print(resultado)