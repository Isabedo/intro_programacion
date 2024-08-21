
name=str(input("Ingresa tu nombre: "))
age=int(input("Ingresa tu año de nacimiento: "))
años=2024-age
print("hola,", name, "tienes", años, "años" )


if age >=1930 and age <=1948:
    print("eres un niño de la posguerra")
elif age >=1949 and age <=1968:
    print("eres un baby boomer")
elif age >=1969 and age <=1980:
    print("eres un gen x")
elif age >=1981 and age <=1993:
    print("eres parte de los millenials")
elif age >=1994 and age <=2010:
    print("eres un gen z")
else:
   print("eres de la generación Alfa")

  