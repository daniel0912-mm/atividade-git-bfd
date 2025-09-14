# Calculadora de media de notas + status aluno

num_notas = int(input("Quantas notas você quer inserir? "))
notas = []
for i in range(num_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"A média das notas é: {media}")

if media >= 7:
    print("Aluno aprovado!")
elif media >= 5:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")
