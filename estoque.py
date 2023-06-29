temporario = []
estoque = []

while True:
    print('[1] - Consultar um item\n'
          '[2] - Adicionar um item\n'
          '[3] - Remover um item')
    opcao = input('Selecione a opção desejada: ')

    if opcao == '1':
        for item in estoque:
            print(f'{item[0]} | {item[1]} | {item[2]}')

    elif opcao == '2':
        while True:
            temporario.append(input('Digite o código do produto: '))
            temporario.append(input('Digite o nome do produto: '))
            temporario.append(int(input('Digite a quantidade que deseja adicionar: ')))
            estoque.append(temporario[:])
            temporario.clear()
            continuar = input('Deseja adicionar outro produto?[S/N]: ').strip().upper()[0]
            if continuar in 'N':
                break