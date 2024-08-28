name=(input("ingresa tu nombre: "))
def say_hi(name="don nadie"):
    print("Hola, " +name)   

if not name:
    say_hi()
else:
    say_hi(name)
