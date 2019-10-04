#PROGRAMA QUE CALCULA EL AREA DE UN TRIANGULO CON LA BASE Y LA ALTURA INTRODUCIDOS POR TECLADO

a, b = map(int, input('Escribe base y altura del triangulo separado por espacio: \n').strip().split())
print("El area del triangulo es {}".format(b*a/2))


#Programa que cambia la temperatura de grados celsius a fahrenheit con introducción por teclado


c= int(input('Introduce una temperatura en grados celsius:'))
print("La temperatura en grados fahrenheit es {:.2f}".format(c*(9/5)+32))


#PROGRAMA QUE CLASIFICA EL NUMERO INTRODUCIDO EN PAR O INPAR


n=int(input("Introduce un numero para saber si es par: "))
if n%2==0:
    print("El numero {} es par".format(n))
else:
    print("El numero {} es inpar".format(n))


#PROGRAMA QUE IMPRIME CUAL DE LOS DOS NUMEROS INTRODUCIDOS ES EL MÁS GRANDE


a, b= map(int, input('Escribe dos numeros para comparar cual es mayor: ').strip().split())
print ("El numero mayor es {}".format(max(a,b)))






