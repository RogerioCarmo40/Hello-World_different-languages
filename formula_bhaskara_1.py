# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Fórmula de Bhaskara

print("***FÓRMULA DE BHASKARA****")
def bhaskara(a,b,c):
  delta = (b**2) - (4*a*c)
  x1 = (((-1)*b) + (delta**0.5))/(2*a)
  x2 = (((-1)*b) - (delta**0.5))/(2*a)
  if delta == 0:
    print()
    print("Equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta = 0, tem-se um único valor de raiz (X1 = x2): ",x1)
  elif delta > 0:
    print()
    print("Equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta > 0, tem-se dois valores distintos de raízes: ",x1,"e",x2)
  else:
    print()
    print("Equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta < 0, sem raízes reais!")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
bhaskara(a,b,c)