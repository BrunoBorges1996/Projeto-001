import csv
import os

dados = []
estoque = []

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual, 'estoque.csv')

def carregar_estoque():
    if os.path.exists('estoque.csv'):
        with open('estoque.csv', 'r') as arquivo:
            reader = csv.reader(arquivo)
            estoque.extend(reader)
    else:
        with open('estoque.csv', 'w', newline=''):
            pass

def salvar_estoque():
    with open('estoque.csv', 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(estoque)

carregar_estoque()

while True:
    print('[0] - Sair e fechar o programa\n'
          '[1] - Consultar um item\n'
          '[2] - Adicionar um item\n'
          '[3] - Remover um item')
    opcao = input('Selecione a opção desejada: ')

    if opcao == '1':
        item_desejado = input('Digite o código da peça: ')
        for item in estoque:
            if item[0] == item_desejado:
                encontrados = []
                encontrados.append(item)
                if len(encontrados) == 1:
                    print(f'{item[0]} | {item[1]} | {item[2]}')
                if len(encontrados) == 0:
                    print('Código não encontrado.')

    elif opcao == '2':
        while True:
            dados.append(input('Digite o código do produto: '))
            dados.append(input('Digite o nome do produto: '))
            dados.append(int(input('Digite a quantidade que deseja adicionar: ')))
            estoque.append(dados[:])
            dados.clear()
            continuar = input('Deseja adicionar outro produto?[S/N]: ').strip().upper()[0]
            if continuar in 'N':
                break

    elif opcao == '0':
        salvar_estoque()
        break