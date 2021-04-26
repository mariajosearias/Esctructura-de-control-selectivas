
"""
Entradas
edad-->int
hemoglobina-->int
genero-->int
salidas
sufre anemia
"""

edad = int (input (" Digite la edad del paciente: "))
hemoglobina = int (input ('Digite la hemoglobina del paciente: '))

if (edad>=0 and hemoglobina >=0.13 or edad<=0,1 and hemoglobina>=0.26):
    print ('no sufre anemia')
elif (edad>=0 and hemoglobina <=0.13 or edad<=0,1 and hemoglobina<=0.26):
    print ('sufre anemia')
if (edad>=0,1 and hemoglobina >=0.10 or edad<=0,6 and hemoglobina>=0.18):
    print ('no sufre anemia')
elif (edad>=0,1 and hemoglobina <=0.10 or edad<=0,6 and hemoglobina<=0.18):
    print ('sufre anemia')
if (edad>=0,6 and hemoglobina >=0.11 or edad<=1 and hemoglobina>=0.15):
    print ('no sufre anemia')
elif (edad>=0,6 and hemoglobina <=0.11 or edad<=1 and hemoglobina<=0.15):
    print ('sufre anemia')
if (edad>=1 and hemoglobina >=0.115 or edad<=5 and hemoglobina>=0.15):
    print ('no sufre anemia')
elif (edad>=1 and hemoglobina <=0.115 or edad<=5 and hemoglobina<=0.15):
    print ('sufre anemia')  
if (edad>=5 and hemoglobina >=0.126 or edad<=10 and hemoglobina>=0.155):
    print ('no sufre anemia')
elif (edad>=5 and hemoglobina <=0.126 or edad<=10 and hemoglobina<=0.155):
    print ('sufre anemia')
if (edad>=10 and hemoglobina >=0.13 or edad<=15 and hemoglobina>=0.155):
    print ('no sufre anemia')
elif (edad>=10 and hemoglobina <=0.13 or edad<=15 and hemoglobina<=0.155):
    print ('sufre anemia')  
        
print ()