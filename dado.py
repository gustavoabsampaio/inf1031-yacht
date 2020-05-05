
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

# def trinca(dados):

# def quadra(dados):

# def full_house(dados):

# def seq_a(dados):

# def seq_b(dados):

# def yam(dados):
#     if len(dados)!=5:
#         return False
#     for i in dados:
#         if dados[i] != dados[0]:
#             return False
#     return True
    
    
def combinacoes_possiveis(dados):    
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
    if full_houes(dados):
        lista_comb(9)
    if seq_a(dados):
        lista_comb.append(10)
    if seq_b(dados):
        lista_comb.append(11)
    if yam(dados):
        lista_comb.append(12)
    
    
    
# def trinca
# def quadra
# def full_house
# def seq-
# def seq+
# def yathzee

#def combinacoes_possiveis(dados):

