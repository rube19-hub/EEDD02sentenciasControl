#Bifurcaión

a=50
if a%2 == 0:
    print(f"El valor {a} es un número par")
else:
    print(f"El valor {a} es un número impar")



if a>50:
    print(f"El valor {a} es mayor de 50")
elif a<50:
    print(f"El valor {a} es menor de 50")
else:
    print(f"El valor {a} es  50")


num= input("Introduce un valor...")
print("Valor introducido",num)   #el input siempre devuelve una cadena de caracteres

num=int(num)
a=0
while a<num:
    print("a:",a)
    a+=1


#bucle que solicite números al usuario hasta se introduzca uno par
sum=0
for a in range(10):
    sum+=a
    print("a: ",a, ",sum:",sum)


numero= int (input("Pon un valor"))
while numero%2 !=0:
    num= int(input("Pon un valor"))
    print("Número de fin: ",num)
exit(0)