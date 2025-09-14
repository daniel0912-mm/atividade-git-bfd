#criar estruturas de repetição com for e while 

lista_for = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #cria uma lista com 10 elementos
for i in lista_for: #inicia um loop for
    print(i) #imprime cada elemento da lista
for i in lista_for: #inicia um loop for
    if i % 2 == 0: #verifica se o elemento é par
        print(f"{i} é par") #imprime se o elemento é par
    else: #se o elemento não for par
        print(f"{i} é impar") #imprime se o elemento é impar

contador = 0 #inicia um contador
while contador <= 10: #inicia um loop while
    print(contador) #imprime o valor do contador
    contador += 1 #incrementa o contador em 1   