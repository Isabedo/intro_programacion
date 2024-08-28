num1=int(input("ingresa un número: "))
num2=int(input("ingresa otro número: "))

def min(num1,num2):
    if num1==num2: 
        return("iguales")
    elif num1<num2:
        return num1
    else:
        return num2
    

minimo= min(num1,num2)
print(minimo)