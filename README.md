# Projeto-001
Criação de um controle de estoque para a empresa atual para qual trabalho.
Com o objetivo de colocar em prática e treinar a atual linguagem de programação que estudo (Python3.x) decidi dar início a este simples projeto de um programa que tive em mente, que terá como objetivo:

 - Cadastrar usuários e superusuários (administradores);
 - Cadastrar os produtos do estoque (Código, nome, quantidade);
 - Ter uma planilha do Excel como banco de dados, que pode ser consultado para inventários;
 - Excluir produtos da lista;
 - Atualizar a entrada e saída de peças;
 - Permitir que outros usuários façam requisições de separação de peças.

O programa será feito totalmente em Python. Será meu primeiro projeto para começar a colocar em prática o que aprendo.

03/07/2023 - Passos iniciais

Comecei criando um menu simples e 'cru', com as opções de cadastrar um produto, consultar um produto, excluir um produto e sair do programa. Armazenar as inforamções diretamente em uma planilha é extremamente complicado e gera diversos problemas no código. O melhor caminho que consegui tomar por ora foi armazenar as informações em cvs, usando a biblioteca do Python que leva o mesmo nome.

Apesar dos primeiros passos iniciais estarem funcionando, o programa apresenta um problema atualmente: ele não exibe a mensagem de 'produto não encontrado'. Tentei de todas as formas que conheço contornar o problema, porém, até o momento, sem sucesso.