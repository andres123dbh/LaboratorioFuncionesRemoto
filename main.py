def a_power_b(a,b)
    for 1 in range(1,b+1):
        resultado=resultado*resultado
    return resultado

a=float(input("Ingresar el numeroa elevar"))
b=float(input("Ingresar el numeroa por el que se elevara"))
resultado=a_power_b(a,b)
print(resultado)