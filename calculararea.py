import sys

print ("Programa para calcular area de objeto geometricos\n")

print ('[1]Calcular area de um triangulo'
       '[2] Calculalr area de um quadrado'
       '[3]Calcular area de um retangulo'
       '[4]calculara area de um losango'
       '[5] Terminar o programa')
opca = 0
opcao = int(input("Escolha uma opção:\n")
while opcao != 5:
if opcao == 1:
    n1 = str(input("Ddigite o valor da base:\n"))
    n2 = str(input("Digite o valor da altura:\n"))
        triangulo = (n1*n2)/2
        print ("Area do triangulo é {triangulo}\n")

elif opcao == 2:
    n3 = str(input("Digite o valo de algum lado do quadrado:\n"))
        quadrado = n3*n3
    print ("Área do quadrado {quadrado}\n")
elif opcao == 3:
    n4 = str(input("Digite o valor da base do retangulo :\n"))
    n5 = str(input("Digite o valor da altura do retangulo:\n"))
         retangulo = n4*n5
    print ("Área do retangulo é {retangulo}\n")
elif opcao == 4:
    n6 = str(input("Digite o valor da diagonal maior do losango:\n"))
    n7 = str(input("Digite o valor da diaginal menos do losango:\n"))
        losango = (n6*n7)/2
    print = ("Área do losango é {losango}\n")
elif opcao == 5:
        Print ("Fim!")

else :
    print ("Opção invalida")

print ("Obrigado")