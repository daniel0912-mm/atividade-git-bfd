#operações aritméticas basicas

a = float(input("insira o valor de a: ")) #pega o valor de a
b = float(input("insira o valor de b: ")) #pega o valor de b   
soma = a + b #soma a e b
subtracao = a - b #subtrai b de a
multiplicacao = a * b #multiplica a e b
divisao_real = a / b #divide a por b e retorna um float
divisao_inteira = a // b #divide a por b e retorna um inteiro
potenciacao = a ** b #eleva a a b
modulo = a % b #retorna o resto da divisão de a por b

print(f'a + b = {soma}') #imprime o resultado da soma
print(f'a - b = {subtracao}') #imprime o resultado da subtração
print(f'a * b = {multiplicacao}') #imprime o resultado da multiplicação
print(f'a / b = {divisao_real}') #imprime o resultado da divisão real
print(f'a // b = {divisao_inteira}') #imprime o resultado da divisão inteira
print(f'a ** b = {potenciacao}') #imprime o resultado da potenciacao
print(f'a % b = {modulo}') #imprime o resultado do modulo