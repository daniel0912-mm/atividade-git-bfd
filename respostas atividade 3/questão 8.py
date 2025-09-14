# Lista de comidas típicas
comidas = [
    ("Feijoada", "Sudeste", 35.0),
    ("Acarajé", "Nordeste", 12.0),
    ("Churrasco", "Sul", 40.0),
    ("Tacacá", "Norte", 18.0),
    ("Pato no tucupi", "Norte", 50.0),
    ("Moqueca", "Sudeste", 45.0),
    ("Cuscuz", "Nordeste", 8.0)
]

def consultar_por_regiao(regiao):
    """Retorna todas as comidas de uma região"""
    return [c for c in comidas if c[1].lower() == regiao.lower()]

def preco_medio():
    """Calcula o preço médio de todas as comidas"""
    if not comidas:
        return 0
    return f"{(sum(c[2] for c in comidas) / len(comidas)):.2f}"

def analise_estatistica():
    """Retorna estatísticas da culinária"""
    if not comidas:
        return {}

    precos = [c[2] for c in comidas]
    mais_caro = max(comidas, key=lambda x: x[2])
    mais_barato = min(comidas, key=lambda x: x[2])

    return {
        "total_comidas": len(comidas),
        "preco_medio": preco_medio(),
        "mais_caro": mais_caro,
        "mais_barato": mais_barato
    }

# ---------------- EXEMPLO DE USO ----------------
print("\n Consulta por região (Nordeste):")
print(consultar_por_regiao("Nordeste"))

print("\n Preço médio das comidas:")
print(preco_medio())

print("\n Análise estatística:")
print(analise_estatistica())
