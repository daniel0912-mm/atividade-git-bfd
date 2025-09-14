# Cálculo do preço com desconto

preço_produto = float(input("Digite o preço do produto: "))
desconto_porcentagem = float(input("Digite o valor do desconto: "))
preço_original = preço_produto
preço_final = preço_produto - preço_produto * (desconto_porcentagem / 100)

if preço_produto < 0 or preço_final < 0:
    print("Valores inválidos. O preço do produto e o preço final devem ser não negativos.")
elif desconto_porcentagem > preço_original:
    print("Valores inválidos. O desconto não pode ser maior que o preço original.")
elif desconto_porcentagem < 0:
    print("Valores inválidos. O desconto deve ser não negativo.")
else:
    print(f"O preço final do produto é: {preço_final:.2f} R$".replace(".", ","))
    print(f"O preço original do produto é: {preço_original:.2f} R$".replace(".", ","))