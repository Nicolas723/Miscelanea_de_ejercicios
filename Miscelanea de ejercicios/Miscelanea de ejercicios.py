#1 Operadores

#1.1 Área de un triangulo
print ("Área de un triangulo")
a1 = float(input("Ingrese la base del triangulo:\n"))
a2 = float(input("Ingrese la altura del triangulo:\n"))
a3 = a1 * a2 / 2
print("el área del triangulo es:" , a3)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#1.2 Suma de dos números
print("suma de dos números")
b1 = float(input("Ingrese el primer número:\n"))
b2 = float(input("Ingrese el segundo número:\n"))
b3 = b1 + b2
print("el resultado de la suma es:" , b3)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#1.3 Elevar al cuadrado
print("Elevar un númeto al cuadrado")
c1 = int(input("Ingrese un número:\n"))
c2 = c1 ** 2
print(c1, "^ 2")
print("el resultado de la potenciación es:" , c2)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#1.4 Algoritmo euros a dolares
print("Conversión euros a dolares")
d1 = float(input("ingrese cantidad de euros:\n"))
d2 = d1 * 1.05
print("tienes " , d2, " dolares")
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#1.5 Área y perimetro de un cuadrado
print("Área y perimetro de un cuadrado")
e1 = float(input("ingrese medida de un lado del cuadrado:\n"))
e2 = e1 * 4
e3 = e1 * e1
print("el área del cuadrado es:", e3)
print("el perimetro del cuadrado es:", e2)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#1.6 Área y volumen de un cilindro
print("Área y volumen de un cilindro")
f1 = float(input("ingrese radio del cilindro:\n"))
f2 = float(input("ingrese altura del cilindro:\n"))
f3 = (2 * 3.14 * f1 * f2) + 2 * 3.14 * (f1 * f1)
f4 = 3.14 * (f1 * f1) * f2
print("el área del cilindro es:", f3)
print("el volumen del cilindro es:", f4)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#1.7 Longitud y área de un circulo
print("Longitud y área de un circulo")
g1 = float(input("ingrese radio de la circunferencia\n"))
g2 = g1 * 2 * 3.14
g3 = (3.14 * g1) * (3.14 * g1)
print("la longitud de la circunferencia es:", g2)
print("el área del circulo es:", g3)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#1.8 Promedio de tres números
print("Promedio de tres números")
h1 = float(input("ingrese el primer número:\n"))
h2 = float(input("ingrese el segundo número:\n"))
h3 = float(input("ingrese el tercer número:\n"))
h4 = (h1 + h2 + h3)/3
print("el promedio es:", h4)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#2 Condicionales
#2.1 Número positivo o negativo
print("Número positivo o negativo")
i1 = float(input("ingrese un número:\n"))
if i1 == 0:
  print(i1, "es neutro")
else:
  if i1 > 0:
    print(i1, "es positivo")
  else:
    print(i1, "es negativo")
print("\n")
print("\n")

#2.2 Mayor y menor
print("Número mayor y menor")
j1 = float(input("ingrese el primer número:\n"))
j2 = float(input("ingrese el segundo número:\n"))
if j1 == j2:
  print(j1, "los dos numeros son iguales")
else:
    if j1 > j2:
      print(j1, "es mayor que", j2)
    else:
      print(j2, "es mayor que", j1)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#2.3 Mayor y menor de tres numeros
print("Número mayor y menor de tres números")
k1 = float(input("ingrese el primer número:\n"))
k2 = float(input("ingrese el segundo número:\n"))
k3 = float(input("ingrese el tercer número:\n"))
if k1 > k2:
  if k2 > k3:
    print(k1, "es el número mayor y", k3, "es el número menor")
  else:
    print(k1, "es el número mayor y", k2, "es el número menor")
elif k3 > k2:
  if k2 > k1:
    print(k3, "es el número mayor y", k1, "es el número menor")
  else:
    print(k3, "es el número mayor y", k2, "es el número menor")
else:
  if k3 > k1:
    print(k2, "es el número mayor y", k1, "es el número menor")
  else:
    print(k2, "es el número mayor y", k3, "es el número menor")
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#2.4 Sumar si a<b, restar si a>b
print("sumar si primer número es menor, restar si es mayor")
l1 = float(input("ingrese primer numero:\n"))
l2 = float(input("ingrese segundo numero:\n"))
if l1 > l2:
  l3 = l1 - l2
  print("la resta de ", l1, "-", l2, "es igual a:", l3)
else:
  l3 = l1 + l2
  print("la suma de ", l1, "+", l2, "es igual a:", l3)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#2.5 cociente entre a y b
print("cociente entre a y b")
m1 = float(input("ingrese el dividendo:\n"))
m2 = float(input("ingrese el divisor:\n"))
if m1 == 0 or m2 == 0:
  print("no se puede dividir por cero")
else:
  m3 = m1 / m2
  print("el cociente de ", m1, "divido entre ", m2, "es igual a:", m3)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#2.6 Sumar a y b si alguno es negativo, si no multiplicarlo
print("Sumar si alguno es negativo, si no multiplicarlos")
n1 = float(input("ingrese el primer número:\n"))
n2 = float(input("ingrese el segundo número:\n"))
if n1 < 0 or n2 < 0:
  n3 = n1 + n2
  print("la suma de ", n1, "+", n2, "es igual a:", n3)
else:
  n3 = n1 * n2
  print("la multiplicación de ", n1, "*", n2, "es igual a:", n3)
print("\n")
print("-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-")
print("\n")

#2.7 Algoritmo para determinar si un año es bisiesto
print("Algoritmo para determinar si un año es bisiesto")
o1 = ("ingrese el año:\n")