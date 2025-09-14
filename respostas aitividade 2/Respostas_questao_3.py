#Media aritmetica

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3
if n1 < 0 or n2 < 0 or n3 < 0:
    print("Valores inválidos. Por favor, insira notas não negativas.")
elif n1 > 10 or n2 > 10 or n3 > 10:
    print("Valores inválidos. As notas devem estar entre 0 e 10.")
else:
    print(f"A média aritmética é: {media:.2f}")