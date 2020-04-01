# Reglas
#1. No memorizar
#2. No tomar apuntes
#3. Seguiré inventando conforme se me ocurran

# Tipos de varibles
# Enteros (int) = números 1-9
# Strings (String) = cadenas de texto ----> ¡¡ Van en comillas !!
# Double (double) = números en coma flotante 
# Boolean (boolean) = Verdadero / False

#def ---> definir la función

#--------------------Integers---------------------

edadDaniel = 23
edadXimena = 22

def resta(a, b):
    return(a-b)

def suma(a, b):
    return(a+b)

def division(a, b):
    return(a/b)

def multiplicacion(a, b):
    return(a*b)

def potenciacion(a, b):
    return(a**b)

#valor=miEdad*(tuEdad+miEdad)

    
def ejercicio(a, b):
    return(multiplicacion(a, suma(a, b)))


#--------------------Strings---------------------

texto = "Ximena"

#lenght(longitud) retornar la longitud de una cadena de texto.
#print(texto+" y Daniel")


#--------------------Sentencias---------------------
#if(condicion):
#   haceralgo

mentira = False

if(edadXimena<=edadDaniel):
    mentira = True
elif(edadXimena>=edadDaniel):
    mentira = False

#--------------------Ciclos---------------------
#Algo que se repite

#haz un ciclo que cuente hasta 200

#for i in range (200):
 #   print(i)

#haz un ciclo que imprima las letras de mi nombre completo

texto10 = "Daniel Fernando Castañeda Torres"


#for i in range(50):
 #   for i in texto10:
  #      print (i)


#--------------------Arreglos---------------------
#Vector [0][1][2][3][4][5] [pollo][vaca][ximena][caballo]

vector1 = [1,2,3,3,5,6,2]
vector2 = [3,2,3,12,0,12,3]

#print(vector1[1]*vector2[0])

#for i in range (len(vector1)):
 #   print(vector1[i]*vector2[i])


#producto punto V1, V2 sumatoria de la multiplicación de sus componentes
#(V1[0]*V2[0])+(V1[1]*V2[1])+(V1[2]*V2[2])+...+(V1[n]*V2[n])

sumatoria = 0

for n in range (len(vector1)):
    sumatoria += vector1[n]*vector2[n]

#print(sumatoria)


bebes=["Sasha", "Ximena"]

for i in bebes:
    for n in i:
        print (n)