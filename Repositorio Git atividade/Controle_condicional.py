#aplicação das funções condicionais

variavel = int(input("insira um numero: ")) #pega o valor da variavel
if variavel > 0: #verifica se a variavel é maior que 0
    print("o numero é positivo") #imprime se a variavel é maior que 0
elif variavel < 0: #verifica se a variavel é menor que 0
    print("o numero é negativo") #imprime se a variavel é menor que 0
else: #se a variavel não for maior nem menor que 0
    print("o numero é zero") #imprime que a variavel é zero

variavel_2 = 17 + 23 + int(input("insira um numero: ")) #pega o valor da variavel_2

if variavel_2 == 40 or variavel_2 >= 100: #verifica se a variavel_2 é igual a 40 ou maior que 100
    print("o numero é 40 ou maior que 100") #imprime se a variavel_2 é igual a 40 ou maior que 100
else:
    print("o numero não é 40 nem maior que 100") #imprime se a variavel_2 não é igual a 40 nem maior que 100

# foi criado um codigo que utiliza estruturas condicionais para verificar se 
# um numero é positivo, negativo ou zero, e se a soma de 17, 23 e um numero inserido pelo usuario é 
# igual a 40 ou maior que 100.