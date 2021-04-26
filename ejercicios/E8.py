"""
Entradas
valor entero 1-->int-->x
valor entero 2-->int-->y
salidas
valores de x u y
"""
x=int(input("Digite el valor del entero: "))
y=int(input("Digite el valor del entero: "))

 

expre=(x**3+y**4-2*x**2)
    
if (expre<=680):
   print("X y Y satisfacen la expresión "+str(expre)) 
elif(expre>=680):
    print("la expresion es mayor a 680 ")