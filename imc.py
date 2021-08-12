print("Bienvenido usuario ")

nombre=str(input("Ingrese su primer nombre: "))

apellido=str(input("Ingrese su primer apellido: "))

print("")

conversionakg=float(input("convierta sus libras en kg:  "))

kg=(conversionakg/2.2046)

print("Su peso en kg es de: ",kg)

estatura=float(input("Ingrese su estatura en metros: "))

peso=float(input("Ingrese su peso actual en kg: "))

print("Hola ",nombre + " " +apellido +" En unos momentos tendra su resultado" )


indice=peso/(estatura**2)
print("Su indice de masa corporal es:{0} y su clasificacion es: ".format(indice), end="")

if (indice ==16.00):

                print("Infrapeso:Delgadez Severa")

if (indice>=16.00 and indice<= 16.99):

                print("Infrapeso:Delgadez moderada")

elif (indice>=17.00 and indice<=18.49):

                print("Infrapeso:Delgadez aceptable")

elif (indice>=18.50 and indice<=24.99):

                print("Peso normal")

elif (indice>=25.00 and indice<=29.99):

                print("Sobrepeso ")

elif (indice>=30.00 and indice<=34.99):

                print("Obeso:Tipo I ")

elif (indice>=35.00 and indice<=40.00):

                print("Obeso: Tipo II ")

elif (indice>= 40.00):

                print("Obesidad:Tipo III, riesgo de muerte")

