"""
Entradas
nombre-->float-->n
costo-->float-->c
Salidas
descuento-->float-->d
descuento2-->float-->descuento2

"""
n=input("Digite su nombre: ")
c=float(input("Digite el valor del producto: "))

if c<50000:
  d=0
  descuento2=c*d
  f=c-descuento2

if c>50000 <=100000:
  d=0.5
  descuento2=c*d
  f=c-descuento2

if c>100000 <=700000:
  d=0.11
  descuento2=c*d
  f=c-descuento2

if c>700000 <=1500000:
  d=0.18
  descuento2=c*d
  f=c-descuento2

if c>1500000:
  d=0.25
descuento2=c*d
f=c-descuento2

print("Cliente:", n,
"El costo del producto es: ",str(c),
"El precio final sera de:",str(f),
"El descuento es de: ",str(descuento2,))