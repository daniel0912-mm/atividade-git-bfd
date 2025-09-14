#identificador de numeros primos em listas

for n in range(2, 50): 
    primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(n,"é primo")
