# listas 

print("\n listas") # imprime o texto

frutas = ["maçã", "banana", "laranja", "uva"] # lista de frutas
print(frutas) # imprime a lista completa
print('primeiro elemento:', frutas[0]) # imprime o primeiro item da lista
print('segundo elemento:', frutas[1]) # imprime o segundo item da lista

frutas.append("abacaxi") # adiciona "abacaxi" ao final da lista
print(frutas) # imprime a lista atualizada

frutas.remove("banana") # remove "banana" da lista
print(frutas) # imprime a lista atualizada

frutas[0] = "manga" # altera o primeiro item para "manga"
print(frutas) # imprime a lista atualizada

# dicionários

print("\n dicionários") # imprime o texto

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"} # dicionário com informações de uma pessoa
print(pessoa) # imprime o dicionário completo
print('nome:', pessoa["nome"]) # imprime o valor associado à chave "nome"
print('idade:', pessoa["idade"]) # imprime o valor associado à chave "idade"

pessoa['profissão'] = "Engenheiro" # adiciona uma nova chave "profissão" com o valor "Engenheiro"
print(pessoa) # imprime o dicionário atualizado

pessoa.pop("cidade") # remove a chave "cidade" e seu valor
print(pessoa) # imprime o dicionário atualizado

pessoa["idade"] = 26 # altera o valor da chave "idade" para 26

print(pessoa) # imprime o dicionário atualizado
