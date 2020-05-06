__all__ = ["get_jogador_atual","proximo_jogador","get_rodada","get_jogada","incrementa_jogada","incrementa_rodada","reseta_jogada","reseta_rodada","reseta_jogador_atual"]

jogador_atual = ''
rodada = 0
jogada = 0


def get_jogador_atual():
    return jogador_atual

def proximo_jogador(jogadores):
    global jogador_atual
    jogador_atual = jogadores[jogadores.index(jogador_atual)+1]
    return 1

def get_rodada():
    return rodada

def get_jogada():
    return jogada

def incrementa_jogada():
    global jogada
    jogada += 1
    return 1

def incrementa_rodada():
    global rodada
    rodada += 1
    return 1

def reseta_jogada():
    global jogada
    jogada = 0
    return 1

def reseta_rodada():
    global rodada
    rodada = 0 
    return 1

def reseta_jogador_atual():
    global jogador_atual
    jogador_atual = ''
    return 1