"""
Entradas
capitalinvertir-->float-->ci 
Salidas
tasainteres-->float-->ti
"""
ci=float(input("Digite el capital a invertir"))
ti=float(input("Digite la tasa de interes"))
if(ci>100000):
 g=(ci*ti)
print("La ganancia sera de: "+str(g))
g1=ci+g
print("El dinero total que esta en la cuenta sera de: " +str(g1))

