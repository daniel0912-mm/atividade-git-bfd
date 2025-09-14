# Dicionário para guardar novelas
novelas = {}

def adicionar_novela(nome, audiencia):
    novelas[nome] = audiencia
    print(f"Novela '{nome}' adicionada com audiência {audiencia} pontos.")

def consultar_audiencia(nome):
    return novelas.get(nome, "Novela não encontrada.")

def filtrar_sucessos():
    return {nome: aud for nome, aud in novelas.items() if aud > 40}

def calcular_media():
    if not novelas:
        return 0
    return sum(novelas.values()) / len(novelas)

def ranking():
    return dict(sorted(novelas.items(), key=lambda x: x[1], reverse=True))


# Exemplo de uso
adicionar_novela("Avenida Brasil", 46)
adicionar_novela("O Clone", 47)
adicionar_novela("Caminho das Índias", 38)
adicionar_novela("Pantanal", 42)

print("\n🔍 Consulta audiência:")
print(consultar_audiencia("O Clone"))

print("\n🔥 Sucessos (acima de 40):")
print(filtrar_sucessos())

print("\n📊 Média de audiência:")
print(calcular_media())

print("\n🏆 Ranking das novelas:")
print(ranking())
