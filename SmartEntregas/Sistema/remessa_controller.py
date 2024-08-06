from controlador_carro import *
from random import randint

def criar_remessa(ponto_1,ponto_2,ponto_3,ponto_4,ponto_5, ponto_6):
    # Lógica para criar uma nova remessa

    print("yuppie, a funçao foi chamada")
    dados_remessa = []
    if (ponto_1 != ''):
        dados_remessa.append(int(ponto_1))
    if (ponto_2 != ''):
        dados_remessa.append(int(ponto_2))
    if (ponto_3 != ''):
        dados_remessa.append(int(ponto_3))
    if (ponto_4 != ''):
        dados_remessa.append(int(ponto_4))
    if (ponto_5 != ''):
        dados_remessa.append(int(ponto_5))
    if (ponto_6 == ''):
        print('O ponto final não foi preenchido, erro!')
    dados_remessa.append(int(ponto_6))
    menor_caminho = tsp(dados_remessa)
    print(dados_remessa)
    print("E..")
    print(menor_caminho)


    return escrever_instrucao(menor_caminho)

def escrever_instrucao(menor_caminho):
    instrucoes = ''
    for i in menor_caminho:

        instrucoes = instrucoes + 'Acelerar para ponto (' + str(menor_caminho[menor_caminho.index(i)]) + ');\n'
        instrucoes = instrucoes + 'Rotacionar para graus (' + str(randint(0,360)) + ');\n'

    return instrucoes


