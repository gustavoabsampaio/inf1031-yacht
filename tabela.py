from jogador import get_jogadores
__all__ = ["cria_coluna","pontua_tabela","consulta_tabela","pontuacao_final","exclui_colunas"]

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
# descartada - -1

colunas = []

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

def cria_coluna(jogador):
    if jogador not in get_jogadores():
        return 0
    colunas.append([jogador,0,0,0,0,0,0,0,0,0,0,0,0])
    return 1

def pontua_tabela(jogador,dados,combinacao):
    if jogador not in get_jogadores():
        return -1
    if not(len(dados) < 6 and len(dados) > 0):
        return -2
    if combinacao < -1 or combinacao > 13 or combinacao == 0:
        return -3
    pontos = pontua(combinacao,dados)
    colunas[combinacao] = pontos
    return pontos
    
def consulta_tabela(jogador):
    if jogador not in get_jogadores():
        return -1
    return colunas[jogador]

def pontuacao_final(jogador):
    if jogador not in get_jogadores():
        return -1
    pontuacao = 0
    for pontos in colunas[jogador][1:]:
        pontuacao += pontos
    return

def exclui_colunas():
    colunas.clear()
    return 1

# cria_tabela() - cria uma tabela vazia, retorna 1 para operação com sucesso
# cria_coluna(jogador) - recebe um jogador e cria o seu respectivo espaço na tabela. Retorna 1 caso insira com sucesso e retorna 0 caso o jogador não exista
# combinacoes_possiveis(dados) - recebe uma jogada de dados e retorna uma lista com as combinacoes possiveis (lista de string), caso nao haja nenhuma combinacao o retorno sera vazio
# pontua_tabela(jogador,dados,combinacao) - recebe um jogador, os dados jogados e as combinacoes e calcula e insere seus pontos na tabela. Retorna um cálculo da pontuação feita, ou -1  caso o jogador, a  -2 jogada ou a -3 combinacao não existam.
# consulta_tabela(jogador) - recebe um jogador e retorna os seus dados da tabela ou retorna -1 caso o jogador não exista.
# pontuacao_final(jogador) - calcula pontuação final do jogador
