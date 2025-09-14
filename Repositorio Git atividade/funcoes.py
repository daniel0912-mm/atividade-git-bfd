#vamos criar algumas funções 

def somar (a, b): #cria uma função que soma dois números
    return a + b #retorna a soma dos dois números
def soma_cumulativa (numero): #cria uma função que soma todos os números de 1 até o número inserido
    soma = 0 #inicia a soma em 0
    for i in range(1, numero + 1): #inicia um loop for de 1 até o número inserido
        soma += i #soma o valor de i na soma
    return soma #retorna a soma

def fatorial (numero): #cria uma função que calcula o fatorial de um número
    if numero == 0: #verifica se o número é 0
        return 1 #retorna 1 se o número for 0
    else: #se o número não for 0
        return numero * fatorial(numero - 1) #retorna o número multiplicado pelo fatorial do número - 1
    
#testando as funções
print(somar(3, 5)) #imprime a soma de 3 e 5
print(soma_cumulativa(5)) #imprime a soma cumulativa de 1 até 5 
print(fatorial(5)) #imprime o fatorial de 5