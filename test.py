def perfect_number(numero):
    comparado=0
    for i in range(1,numero):
        if numero%i==0:
            comparado=comparado+i
    return comparado

num=int(input("Ingresar numero para evaluar: "))
comparar=perfect_number(num)
if num==comparar:
    print("Es un numero perfecto")
else:
    print("No es un numero perfecto")

