# coding=utf-8
print("Programa de conversão de temperaturas\n")

print('[1] Fahrenheit para Celsius \n'
      '[2] Fahrenheit para Kelvin \n'
      '[3] Kelvin para Celsius \n'
      '[4] Kelvin para Fahrenheit \n'
      '[5] Celsius para Fahrenheit \n'
      '[6] Celsius para Kelvin \n'
      '[7] Sair\n')
temp = 0
while temp != 7:
    temp = int(input("Digite uma opção:\n"))
    if temp == 1:
        n1 = int(input(" Valor a ser convertido:\n"))
        c1 = (n1 - 32) * 5 / 9
        print(f"De {n1} Fahrenheit para {c1} Celsius")
    elif temp == 2:
        n1 = int(input(" Valor a ser convertido:\n"))
        k1 = n1 - 32 / (5/9) + 273
        print(f"De {n1} Fahrenheit para {k1} Kelvin")
    elif temp == 3:
        n1 = int(input(" Valor a ser convertido:\n"))
        f1 = (5/9) * (n1 - 273) + 32
        print("De" ,n1, "Kelvin para",f1, "Fahrenheit")
    elif temp == 4:
        n1 = int(input(" Valor a ser convertido:\n"))
        c = n1 - 273
        print("De %i Kelvin para %i Celsius"%(n1,c))
    elif temp == 5:
        n1 = int(input(" Valor a ser convertido:\n"))
        f = 9 * n1 / 5 + 32
        print(f"De {n1} Celsius para {f} Fahreneit")
    elif temp == 6:
        n1 = int(input(" Valor a ser convertido:\n"))
        k = n1 + 273
        print("De {} Celsius para {} Kelvin".format(n1,k))
    elif temp == 7:
        print("Finalizando")
    else:
        print("Opção invalida")
print("Fim")
