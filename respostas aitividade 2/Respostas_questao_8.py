# Calculadora simples de investimento
import time

valor_inicial = float(input("Digite o valor inicial do investimento: "))
rendimento_por_periodo = float(input("Digite o rendimento por período (em %): "))
aporte_mensal = float(input("Digite o valor do aporte mensal: "))
total_periodos = int(input("Digite o total de períodos (em meses): "))

rend = (valor_inicial * rendimento_por_periodo)/100
semi_total = valor_inicial + rend
total = semi_total + (aporte_mensal * total_periodos)

if valor_inicial < 0 or aporte_mensal < 0 or total_periodos < 0 or rendimento_por_periodo < 0:
    print("Valores inválidos. Todos os valores devem ser não negativos.")
else:
    print("Aqui estão os valores:")
    time.sleep(1)
    print(f"Valor inicial: {valor_inicial:.2f} R$".replace(".", ","))
    time.sleep(1)
    print(f"Rendimento por período: {rendimento_por_periodo:.2f} %".replace(".", ","))
    time.sleep(1)
    print(f"Aporte mensal: {aporte_mensal:.2f} R$".replace(".", ","))
    time.sleep(1)
    print(f"Total de períodos: {total_periodos} meses")
    time.sleep(1)
    print(f"Total acumulado: {total:.2f} R$".replace(".", ","))
