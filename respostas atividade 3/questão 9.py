#Calculadora interativa 

def calcular(): 
    while True:
        operação = input("Escolha a operação (+, -, *, /) ou 'sair' para encerrar: ")
        if operação == 'sair':
            print("Calculadora encerrada.")
            break
        if operação in ('+', '-', '*', '/'):
            print("Digite dois números: ")
            num1 = float(input())
            num2 = float(input())
        if operação == '+':
            print(f"{num1} + {num2} = {num1 + num2:.2f}")
        elif operação == '-':
            print(f"{num1} - {num2} = {num1 - num2:.2f}")
        elif operação == '*':
            print(f"{num1} * {num2} = {num1 * num2:.2f}")
        elif operação == '/':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2:.2f}")
            else:
                print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida.")
# Exemplo de uso
calcular()