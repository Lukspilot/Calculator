print("******************************")
print("*         Calculator !       *")
print("******************************")

print("> Menu <")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division entera")
print("6. Exponente")
print("7. Modulo o resto \n")

opcion = int(input("Selecciona opcion deseada: "))

if opcion == 1:
  num1 = int(input("Introduce el primer numero: "))
  num1 += int(input("Introduce el segundo valor: "))
  
  print("El resultado de la suma es:", num1)

elif opcion == 2:
  num1 = int(input("Introduce el primer numero: "))
  num1 -= int(input("Introduce el segundo valor: "))
  
  print("El resultado de la resta es:", num1)

elif opcion == 3:
  num1 = int(input("Introduce el primer numero: "))
  num1 *= int(input("Introduce el segundo valor: "))
  
  print("El resultado de la multiplicacion es:", num1)

elif opcion == 4:
  num1 = int(input("Introduce el primer numero: "))
  num1 /= int(input("Introduce el segundo valor: "))
  
  print("El resultado de la division es:", round(num1))

elif opcion == 5:
  num1 = int(input("Introduce el primer numero: "))
  num1 //= int(input("Introduce el segundo valor: "))
  
  print("El resultado es:", num1)

elif opcion == 6:
  num1 = int(input("Introduce el primer numero: "))
  num1 **= int(input("Introduce el segundo valor: "))
  
  print("El resultado es:", num1)

elif opcion == 7:
  num1 = int(input("Introduce el primer numero: "))
  num1 %= int(input("Introduce el segundo valor: "))
  
  print("El resultado es:", num1)