# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

print("***CALCULADORA DE DOIS NÚMEROS****\n")
def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("A Soma é = ",x+y)

def subtracao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("A Subtracao é = ",x-y)

def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("A Multiplicacao é = ",x*y)

def divisao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("A Divisao é = ",x/y)

opcao=1

while opcao:
    print("\n0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")

    opcao = int(input("Opção: "))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()