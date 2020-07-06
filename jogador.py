# insere, remove e devolve a lista de todos os jogadores
__all__ = ["insere_jogador", "exclui_jogador", "get_jogadores"]

jogadores = []

# recebe um nome e o insere na lista de jogadores
def insere_jogador(nome):
    global jogadores
    nome = nome.strip()
    if nome == '':
        return 0
    if len(get_jogadores()) > 5:
        return 0
    jogadores.append(nome)
    print(jogadores)
    return 1

# recebe o nome de um jogador e o exclui da lista de jogadores
def exclui_jogador(nome):
    global jogadores
    if nome not in get_jogadores():
        return 1
    jogadores.clear()
    return 0

# retorna a lista de jogadores
def get_jogadores():
    return jogadores