#Área do Retângulo

altura = float(input("Digite a altura do retângulo: "))
base = float(input("Digite a base do retângulo: "))
area = altura * base
if base <= 0 or altura <= 0: 
    print("valor invalido tente inserir um valor valido")
else:
    print(f"A área do retângulo é: {area:.2f}")