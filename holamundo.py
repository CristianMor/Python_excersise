import subprocess

#Initial values
myvar, _myvar2, MyVar = 'my', "Abuelo", 'Neo';

print(myvar+' '+_myvar2+' '+ MyVar);

#Desempaquetar  
fruits = ["Pera", "Manzana", "Durazno"]
x, y, z = fruits

print(x)
print(y)
print(z)

#Variables globales

def myfunc():
    global _var_global
    _var_global= 'Carlos'
    #print('Python is '+ _var_global)

myfunc()

print("Python is "+ _var_global)

saludo = ''
#subprocess.call('clear', shell=True)

#Bucles
nombre = "Valeria";
print("""Longitud: %d""", len(nombre))
for x in nombre:
    print("i" not in x);
    if 'i' not in x:
        print('Aqui encontramos a i')
