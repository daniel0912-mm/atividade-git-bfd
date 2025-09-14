#Gerenciador de times de futebol 

times = ['fluminense', 'vasco', 'botafogo', 'flamengo', 'nova iguaçu', 'bangu',
         'palmeiras', 'corinthians', 'são paulo', 'santos',
         'grêmio', 'internacional', 'athletico paranaense', 'cuiabá']

while True:
    print('\n 1- mostrar todos os times: ')
    print('\n 2- mostrar times por letra inicial: ')
    print('\n 3- adicionar novo time: ')
    print('\n 4 - excluir um time existente: ')
    print('\n 5 - filtrar time por nome: ')
    print('\n 6 - fatias de lista: ')
    print('\n 7 - sair: ')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print(f"\ntodos os times: \n{times}")
    elif opcao == '2':
        letra = input('digite a letra inicial desejada: ')
        for t in times:
            if t.startswith(letra):
                print(f"times que começam com a letra {letra}: {t}")
    elif opcao == '3':
        novo_time = input('Digite o nome do novo time: ')
        times.append(novo_time)
        print(f"\ntime adicionado: {novo_time}")
    elif opcao == '4':
        time_excluir = input('Digite o nome do time a ser excluído: ')
        if time_excluir in times:
            times.remove(time_excluir)
            print(f"\ntime excluído: {time_excluir}")
        else:
            print(f"\ntime não encontrado: {time_excluir}")
    elif opcao == '5':
        time_filtrar = input('Digite o nome do time a ser filtrado: ')
        for t in times:
            if time_filtrar in t:
                print(f"\ntime encontrado: {t}")
    elif opcao == '6':
        print(f"\nfatias de lista: {times[0:3]}")  # Exemplo de fatia
    elif opcao == '7':
        print("\nsaindo...")
        break
    else:
        print("\nopção inválida.")