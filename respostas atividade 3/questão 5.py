#Soma dos números inteiros de 1 a N

numero_total = int(input("Digite o numero total: "))
soma = 0
for n in range(1, numero_total + 1):
    soma += n
print("a soma total é ",soma)

'''pelo oq eu entendi essa formula não é nem um pouco eficiente pq pra numeros
gigantes ela simplesmente consome muito mais memoria e tempo de processamento
'''

# n = int(input("Digite um numero de termos: ")) # metodo alternativo 
# soma = n * (n + 1) // 2

# print("a soma total é ",soma)