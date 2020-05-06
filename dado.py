# esse modulo lida com os dados e combinacoes
from random import randint
__all__ = ["combinacoes_possiveis","get_dados","rola_dados"]
dados = [0,0,0,0,0]

# retorna os valores do dice pool
def get_dados():
    return dados

# recebe as posicoes e rola os dados nelas
def rola_dados(posicoes):
    global dados
    for posicao in posicoes:
        dados[posicao] = randint(1,6)
    dados = dados.sort()
    return 1

# qualquer quantidade de 1 nos dados 
def jogada1(dados):
    for i in dados:
        if i == 1:
            return True
    return False

# qualquer quantidade de 2 nos dados
def jogada2(dados):
    for i in dados:
        if i == 2:
            return True
    return False

# qualquer quantidade de 3 nos dados 
def jogada3(dados):
    for i in dados:
        if i == 3:
            return True
    return False

# qualquer quantidade de 4 nos dados 
def jogada4(dados):
    for i in dados:
        if i == 4:
            return True
    return False

# qualquer quantidade de 5 nos dados 
def jogada5(dados):
    for i in dados:
        if i == 5:
            return True
    return False

# qualquer quantidade de 6 nos dados 
def jogada6(dados):
    for i in dados:
        if i == 6:
            return True
    return False

# qualquer tripla de dados iguais
def trinca(dados):
    c1 = dados.count(1)
    c2 = dados.count(2)
    c3 = dados.count(3)
    c4 = dados.count(4)
    c5 = dados.count(5)
    c6 = dados.count(6)
    if c1>=3 or c2>=3 or c3>=3 or c4>=3 or c5>=3 or c6>=3:
        return True
    return False

# qualquer quadra de dados iguais
def quadra(dados):
    c1 = dados.count(1)
    c2 = dados.count(2)
    c3 = dados.count(3)
    c4 = dados.count(4)
    c5 = dados.count(5)
    c6 = dados.count(6)

    if c1>=4 or c2>=4 or c3>=4 or c4>=4 or c5>=4 or c6>=4:
        return True
    return False
    
# qualquer tripla de dados iguais, junto com uma dupla de dados iguais
def full_house(dados):
    conta = [dados.count(v) for v in set(dados)]
    if (3 in conta) and (2 in conta) and len(dados)==5:
        return True
    else:
        return False

# sequencia de 2,3,4,5,6
def seq_a(dados):
    c2 = dados.count(2)
    c3 = dados.count(3)
    c4 = dados.count(4)
    c5 = dados.count(5)
    c6 = dados.count(6)

    if c2 == 1 and c3 == 1 and c4 == 1 and c5 == 1 and c6 == 1:
        return True
    return False

# sequencia de 1,2,3,4,5
def seq_b(dados):
    c1 = dados.count(1)
    c2 = dados.count(2)
    c3 = dados.count(3)
    c4 = dados.count(4)
    c5 = dados.count(5)

    if c2 == 1 and c3 == 1 and c4 == 1 and c5 == 1 and c1 == 1:
        return True
    return False

# todos os dados iguais
def yam(dados):
    if len(dados)!=5:
        return False
    if(len(set(dados)) == 1):
        return True
    return False


# testando a combinacoes_possiveis pode-se afirmar que todas as funcoes das combinacoes funcionam
# recebe uma lista de dados e retorna uma lista com todas as combinacoes possiveis
def combinacoes_possiveis(dados): 
    if not dados:
        return -1   
    lista_comb = []
    if jogada1(dados):
        lista_comb.append(1)
    if jogada2(dados):
        lista_comb.append(2)
    if jogada3(dados):
        lista_comb.append(3)
    if jogada4(dados):
        lista_comb.append(4)
    if jogada5(dados):
        lista_comb.append(5)
    if jogada6(dados):
        lista_comb.append(6)
    if trinca(dados):
        lista_comb.append(7)
    if quadra(dados):
        lista_comb.append(8)
    if full_house(dados):
        lista_comb.append(9)
    if seq_a(dados):
        lista_comb.append(10)
    if seq_b(dados):
        lista_comb.append(11)
    if yam(dados):
        lista_comb.append(12)
    return lista_comb

# glossario de combinacoes
# jogada de 1 - 1
# jogada de 2 - 2
# jogada de 3 - 3
# jogada de 4 - 4
# jogada de 5 - 5
# jogada de 6 - 6
# trinca - 7
# quadra - 8
# full-house - 9
# sequencia alta - 10
# sequencia baixa - 11
# yam - 12