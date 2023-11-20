
operaciones = """
¿Qué operacion quieres realizar?

1. Suma
2. Resta
3. Multiplicacion
4. Divicion

"""

opcion = input(operaciones)

if opcion == "1":  
    numero_1 = input("Introduce un numero 1: ")
    numero_1 = float(numero_1)
  
    numero_2 = input("Introduce un numero 2: ")
    numero_2 = float(numero_2)
    
    numero_3 = numero_1 + numero_2
    numero_3 = str(numero_3)
    print("El resultado de la suma es: " + numero_3)

elif opcion == "2":  
    numero_1 = input("Introduce un numero 1: ")
    numero_1 = float(numero_1)
  
    numero_2 = input("Introduce un numero 2: ")
    numero_2 = float(numero_2)
    
    numero_3 = numero_1 - numero_2
    numero_3 = str(numero_3)
    print("El resultado de la resta es: " + numero_3)

elif opcion == "3":  
    numero_1 = input("Introduce un numero 1: ")
    numero_1 = float(numero_1)
  
    numero_2 = input("Introduce un numero 2: ")
    numero_2 = float(numero_2)
    
    numero_3 = numero_1 * numero_2
    numero_3 = str(numero_3)
    print("El resultado de la multiplicacion es: " + numero_3)

elif opcion == "4":  
    numero_1 = input("Introduce un numero 1: ")
    numero_1 = float(numero_1)
  
    numero_2 = input("Introduce un numero 2: ")
    numero_2 = float(numero_2)
     
    numero_3 = numero_1 / numero_2
    numero_3 = str(numero_3)
    print("El resultado de la divicion es: " + numero_3)
