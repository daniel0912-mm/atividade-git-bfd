#Calculadora de idade

import time

print("calculadora de idade")

time.sleep(2)

ano_nascimento = int(input("insira o seu ano de nascimento: "))

idade = 2025 - ano_nascimento 

if ano_nascimento > 2025:
    print("ano invalido, por favor insira uma data possivel")
else:
    print(f"você tem {idade} anos em 2025")