estoque = {}

while True:
    codigo = input('Digite o código do produto: ')
    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade do produto: '))

    item = {'codigo': codigo, 'nome': nome, 'quantidade': quantidade}
    estoque[codigo] = item

    print(f'Código: {codigo}\n'
          f'Nome: {nome}\n'
          f'Quantidade: {quantidade}\n'
          'Item adicionado com sucesso!')
    continuar = input('Deseja adicionar outro produto? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

for codigo, nome, quantidade in estoque:
    print(f'{codigo} | {nome} | {quantidade}')