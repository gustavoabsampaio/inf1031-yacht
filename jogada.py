# lida com as variaveis da partida (rodada, jogada e jogador_atual)
from jogador import get_jogadores
__all__ = ["get_jogador_atual","proximo_jogador","get_rodada","get_jogada","incrementa_jogada","incrementa_rodada","reseta_jogada","reseta_rodada","reseta_jogador_atual"]

jogador_atual = 0
rodada = 0
jogada = 0

# retorna o id do jogador atual
def get_jogador_atual():
    return jogador_atual

# passa de turno
def proximo_jogador(jogadores):
    global jogador_atual
    if jogador_atual == len(jogadores):
        jogador_atual = 0
    else:
        jogador_atual += 1
    return 1

# retorna a rodada
def get_rodada():
    return rodada

# retorna a jogada
def get_jogada():
    return jogada

# incrementa a jogada
def incrementa_jogada():
    global jogada
    jogada += 1
    return 1

# incrementa a rodada
def incrementa_rodada():
    global rodada
    rodada += 1
    return 1

# define a jogada como 0
def reseta_jogada():
    global jogada
    jogada = 0
    return 1

# define a jogada como 0
def reseta_rodada():
    global rodada
    rodada = 0 
    return 1

# define o jogador atual como 0
def reseta_jogador_atual():
    global jogador_atual
    jogador_atual = 0
    return 1