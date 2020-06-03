from pymongo import MongoClient
from CRUDLoja.funcoes import *

client = MongoClient("localhost", 27017)
db = client.CRUDLoja
collection = db.produto

menu = int(input("Selecione a operacao desejada \n"
                 "1-Cadastrar Produto \n"
                 "2-Remover Produto \n"
                 "3-Atualizar Produto \n"
                 "4-Listar todos os Produtos \n"
                 "5-Comprar Estoque \n"
                 "6-Vender Estoque \n"
                 "7-Exportar para Tabela no Excel \n"
                 "8-Sair \n"))
while menu != 8:
    if menu == 1:
        cadastrar(collection)
    if menu == 2:
        remover(collection)
    if menu == 3:
        atualizar(collection)
    if menu == 4:
        listar(collection)
    if menu == 5:
        comprar(collection)
    if menu == 6:
        vender(collection)
    if menu == 7:
        excel(collection)
    menu = int(input("Selecione a operacao desejada \n"
                     "1-Cadastrar Produto \n"
                     "2-Remover Produto \n"
                     "3-Atualizar Produto \n"
                     "4-Listar Produtos \n"
                     "5-Comprar Estoque \n"
                     "6-Vender Estoque \n"
                     "7-Exportar para Tabela no Excel \n"
                     "8-Sair \n"))
