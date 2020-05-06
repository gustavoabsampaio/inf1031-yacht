from jogador import get_jogadores
__all__ = ["cria_coluna","pontua_tabela","consulta_tabela","pontuacao_final","exclui_colunas"]

colunas = []

# recebe uma combinacao e a lista de dados e retorna o valor dos pontos
def pontua(combinacao,dados):
    if combinacao == 1:
        return dados.count(1)
    if combinacao == 2:
        return dados.count(2)*2
    if combinacao == 3:
        return dados.count(3)*3
    if combinacao == 4:
        return dados.count(4)*4
    if combinacao == 5:
        return dados.count(5)*5
    if combinacao == 6:
        return dados.count(6)*6
    if combinacao == 7:
        return sum(dados)
    if combinacao == 8:
        return sum(dados)
    if combinacao == 9:
        return 25
    if combinacao == 10:
        return 30
    if combinacao == 11:
        return 40
    if combinacao == 12:
        return 50

# recebe o nome do jogador e cria uma coluna na tabela com seu nome.
# retorna 0 caso o jogador nao exista e 1 caso crie com sucesso
def cria_coluna(jogador):
    if jogador not in get_jogadores():
        return 0
    colunas.append([jogador,0,0,0,0,0,0,0,0,0,0,0,0])
    return 1

# recebe o id de um jogador, a lista de dados, e a combinacao e insere os pontos na tabela.
# retorna -1 caso o jogador nao exista, -2 caso os dados sejam invalidos, -3 caso a combinacao seja invalida ou os pontos.
def pontua_tabela(jogador,dados,combinacao):
    if jogador > len(get_jogadores()):
        return -1
    if len(dados) != 5:
        return -2
    if combinacao < -1 or combinacao > 12 or combinacao == 0:
        return -3
    pontos = pontua(combinacao,dados)
    colunas[jogador][combinacao] = pontos
    return pontos
    
# recebe o id de um jogador e retorna sua coluna na tabela
def consulta_tabela(jogador):
    if jogador >= len(get_jogadores()):
        return -1
    return colunas[jogador]

# recebe o id de um jogador.
# retorna -1 caso jogador nao exista ou a pontuacao caso exista.
def pontuacao_final(jogador):
    if jogador >= len(get_jogadores()):
        return -1
    pontuacao = 0
    for pontos in colunas[jogador][1:]:
        if pontos != -1:
            pontuacao += pontos
    return pontuacao

# exclui todas as colunas da tabela
def exclui_colunas():
    colunas.clear()
    return 1