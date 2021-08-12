
#ejercicio1

#ganador=1000
#num=int(input("Ingrese un  numero: "))
#if num==ganador:
 #   print("Ganaste el premio")
#else:
 #       print("perdiste")




#ejercicio2
#Debe pedir al usuario una nota (entre 1 y 7).
#  Luego se debe comprobar que el número 
# efectivamente esté en ese rango, si no 
# lo está imprima un mensaje de error. 
# Si lo está, imprima reprobado si la 
# nota es inferior a 4, regular si está
#  entre 4 y 5, ok si está entre 5 y 6,
#  y por último, bien si está entre 6 y 7

#nota1=int(input("Ingrese una nota : "))
#if (nota1==1 and nota1 <7):
 #   print("Su nota esta entre el rango")

#if nota1<4:
 #       print("Reprobado ")
#if nota1==4 and nota1<=5:
 #          print("regular")
#if nota1==6 and nota1<=7:
 #               print("Bien")

#else:
   #print("Ingrese de nuevo su nota")



#ejercicio3
#import random
#num1=random.randint(1, 100)
#num2=random.randint(1, 100)
#num3=random.randint(1, 100)
#print(num1, num2, num3)
#if num1==7 and num2==7 and num3==7:
#    print("You Win")
#else:
 #        print("Sad Partner")


#coleccion=[2,4,5,7,8,9,3,4]
#for e in coleccion:
 #   if e % 2!=0:
  #      continue
   # print(e)

#for i in range(100, 200):
 #   print(i)
  
#suma = 0

#for i in range(0,101):
 #     suma=i+suma

#print(suma)


#ejemplo ciclo infinito
#i = 1

#while i <= 3:

 #   print(i)

  #  i += 1

#print("Programa terminado")
4



#ejerciciowhile
#res = 0
#entrada=1
#print("para cancelar ponga el numero 0")
#while entrada!= 0:
 #  entrada=int(input("Ingrese enteros: "))
   
  # res = res + entrada


#print(f"su suma es: {res}")


numero=int(input("Escriba un número 0 para salir: "))
suma=0
while (numero != 0):
   suma+=numero
   numero = int(input("Escriba un número: "))
   
print(suma)

