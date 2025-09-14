# Lista de produtos: cada produto é um dicionário
produtos = []

def adicionar_produto(nome, categoria, preco):
    produto = {"nome": nome, "categoria": categoria, "preco": preco}
    produtos.append(produto)
    print(f"✅ Produto '{nome}' adicionado com sucesso!")

def listar_por_categoria(categoria):
    resultado = [p for p in produtos if p["categoria"].lower() == categoria.lower()]
    return resultado

def buscar_produto(nome):
    for p in produtos:
        if p["nome"].lower() == nome.lower():
            return p
    return None

def preco_medio():
    if not produtos:
        return 0
    soma = sum(p["preco"] for p in produtos)
    return soma / len(produtos)

# ---------------- EXEMPLO ----------------
adicionar_produto("Café do Cerrado", "Bebida", 15)
adicionar_produto("Açaí", "Fruta", 10)
adicionar_produto("Queijo Minas", "Laticínio", 25)

print("\n Produtos da categoria 'Bebida':")
print(listar_por_categoria("Bebida"))

print("\n Busca pelo produto 'Açaí':")
print(buscar_produto("Açaí"))

print("\n Preço médio dos produtos:")
print(preco_medio())
