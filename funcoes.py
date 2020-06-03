import pandas as pd
import csv


def cadastrar(collection):
    codigo = int(input("Digite o ID do produto"))
    if collection.find_one({'_id': codigo}):
        print("Este codigo ja esta cadastrado")
    else:
        nome = input("Digite o nome do produto")
        preco = float(input("Digite o preco do produto"))
        descricao = input("Digite a descricao do produto")
        estoque = int(input("Digite a quantidade em estoque"))
        marca = input("Digite a marca do produto")
        collection.insert_one({
            '_id': codigo,
            'Nome': nome,
            'Preco': preco,
            'Descricao': descricao,
            'Estoque': estoque,
            'Marca': marca
        })


def remover(collection):
    codigo = int(input("Digite o ID do produto que sera excluido"))
    if collection.find_one({'_id': codigo}):
        print(collection.find_one({'_id': codigo}))
        pergunta = input("Realmente deseja deletar o produto? SIM | NAO").upper()
        if pergunta == 'SIM':
            collection.delete_one({'_id': codigo})
            print("Produto deletado")
        else:
            print("Produto nao deletado")
    else:
        print("Produto nao encontrado")


def atualizar(collection):
    codigo = int(input("Digite o ID do produto que sera atualizado"))
    if collection.find_one({'_id': codigo}):
        print(collection.find_one({'_id': codigo}))
        pergunta = input("Realmente deseja atualizar o produto? SIM | NAO").upper()
        if pergunta == 'SIM':
            info = input('Digite qual campo voce deseja alterar: ')
            dado = input('Digite o novo valor')
            if dado.isdigit():
                dado = float(dado)
            collection.update_one({'_id': codigo}, {'$set': {info: dado}})
            print(collection.find_one({'_id': codigo}))
            print('Produto atualizado com sucesso')
        else:
            print("Produto nao atualizado")
    else:
        print("Produto nao encontrado")


def listar(collection):
    pergunta = input('Deseja mostrar todos os dados ou apenas um?').upper()
    if pergunta == 'TODOS':
        resultados = collection.find({})
        for resultado in resultados:
            print(resultado)
    else:
        codigo = int(input("Digite o ID do produto que sera mostrado"))
        resultados = collection.find_one({"_id": codigo})
        print(resultados)


def comprar(collection):
    codigo = int(input("Digite o ID do produto que recebera mais estoque: "))
    if collection.find_one({'_id': codigo}):
        print(collection.find_one({'_id': codigo}))
        estoque = int(input('Digite quantos produtos serao adicionados ao estoque: '))
        collection.update_one({'_id': codigo}, {'$inc': {'Estoque': estoque}})
        print("Estoque atualizado")
    else:
        print("Produto nao encontrado")


def vender(collection):
    codigo = int(input("Digite o ID do produto que recebera mais estoque: "))
    if collection.find_one({'_id': codigo}):
        print(collection.find_one({'_id': codigo}))
        estoque = int(input('Digite quantos produtos serao removidos do estoque: '))
        estoque = 0 - estoque
        collection.update_one({'_id': codigo}, {'$inc': {'Estoque': estoque}})
        print("Estoque atualizado")
    else:
        print("Produto nao encontrado")


def excel(collection):
    columns = ['_id', 'Nome', 'Preco', 'Descricao', 'Estoque', 'Marca']
    resultados = list(collection.find({}))
    df = pd.DataFrame(resultados, columns=columns)
    df = df.set_index('_id')
    df.sort_values(by='_id', inplace=True, ignore_index=True)
    df.to_csv('dados.csv', encoding='iso8859-1', sep=';', index=False, quoting=csv.QUOTE_NONNUMERIC)
