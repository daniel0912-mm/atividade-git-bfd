# Calculo do troco

valor_compra = float(input("Digite o valor da compra: "))
valor_pago = float(input("Digite o valor pago: "))
troco = valor_pago - valor_compra
if valor_pago < valor_compra:
    print(f"Valor pago insuficiente. Voce deve {-troco:.2f} R$".replace(".", ","))
else:
    print(f"O troco é: {troco:.2f} R$".replace(".", ","))