"""
Entradas
variable1-->int-->A
variable2-->int-->B
variable3-->int-->C
variable4-->int-->D
Salidas
miles-->int-->m
decenas-->int-->d
numero-->int-->n
"""
A=int(input("Digite el valor de la variable A: "))
B=int(input("Digite el valor de la variable B: "))
C=int(input("Digite el valor de la variable C: "))
D=int(input("Digite el valor de la variable D: "))

if (C>=5):
  m=A*1000
  d=B*100
  n=m+(d+100)
  print(n)
else:
  m=A*1000
  ds=B*100
  n=m+(d+100)
  print(n) 
 