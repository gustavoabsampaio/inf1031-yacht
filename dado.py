__all__ = ["combinacoes_possiveis"]


def jogada1(dados):
    for i in dados:
        if i == 1:
            return True
    return False

def jogada2(dados):
    for i in dados:
        if i == 2:
            return True
    return False

def jogada3(dados):
    for i in dados:
        if i == 3:
            return True
    return False

def jogada4(dados):
    for i in dados:
        if i == 4:
            return True
    return False

def jogada5(dados):
    for i in dados:
        if i == 5:
            return True
    return False

def jogada6(dados):
    for i in dados:
        if i == 6:
            return True
    return False

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
    

def full_house(dados):
    conta = [dados.count(v) for v in set(dados)]
    if (3 in conta) and (2 in conta) and len(dados)==5:
        return True
    else:
        return False

def seq_a(dados):
    c2 = dados.count(2)
    c3 = dados.count(3)
    c4 = dados.count(4)
    c5 = dados.count(5)
    c6 = dados.count(6)

    if c2 == 1 and c3 == 1 and c4 == 1 and c5 == 1 and c6 == 1:
        return True
    return False

def seq_b(dados):
    c1 = dados.count(1)
    c2 = dados.count(2)
    c3 = dados.count(3)
    c4 = dados.count(4)
    c5 = dados.count(5)

    if c2 == 1 and c3 == 1 and c4 == 1 and c5 == 1 and c1 == 1:
        return True
    return False


def yam(dados):
    if len(dados)!=5:
        return False
    for i in dados:
        if dados[i+1] != dados[0]:
            return False
    return True
    
    
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
    
    
    
