__all__ = ["insere_jogador", "exclui_jogador", "get_jogador"]

jogadores = []

def insere_jogador(nome):
    nome = nome.strip()
    if nome == '':
        return 0
    jogadores.append(nome)
    return 1


def exclui_jogador(nome):
    for i in jogadores:
        if jogadores[i] == nome:
            jogadores.remove(i)
            return 1
    return 0

def get_jogadores():
    return jogadores

# def get_jogador(nome):
#     for i in jogadores:
#         if jogadores[i] == nome:
#             return 1
#     return 0



