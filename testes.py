import unittest

def teste_insere_jogador_sucesso(self):
    print("")
    retorno_esperado = insere_jogador("Teste")
    self.assertEqual(retorno_esperado,1)

def teste_insere_jogador_string_vazia(self):
    print("")
    retorno_esperado = insere_jogador("")
    self.assertEqual(retorno_esperado,0)

def teste_exclui_jogador_sucesso(self):
    print("")
    retorno_esperado = exclui_jogador("Teste")
    self.assertEqual(retorno_esperado, 0)

def teste_exclui_jogador_inexistente(self):
    print("")
    retorno_esperado = exclui_jogador("Deus")
    self.assertEqual(retorno_esperado, 1)

def teste_exclui_jogador_string_vazia(self):
    print("")
    retorno_esperado = exclui_jogador("")
    self.assertEqual(retorno_esperado, 2)

def teste_joga_sucesso(self):
    print("")
    lista_dados = [2,5]
    retorno_esperado = joga("Jogador",lista_dados)
    self.assertEqual(retorno_esperado, 0)

# def teste_joga_jogador_inexistente(self):
#     print("")
#     lista_dados = [1]
#     retorno_esperado = joga("Inexistente",lista_dados)
#     self.assertEqual(retorno_esperado, 1)

# def teste_joga_dado_inalcancavel():
#     print("")
#     lista_dados = [1,7]
#     retorno_esperado = joga("Jogador",lista_dados)

def teste_cria_tabela(self):
    print("")
    retorno_esperado = cria_tabela(self)
    self.assertEqual(retorno_esperado, 1)

def teste_cria_coluna_sucesso(self):
    print("")
    insere_jogador("Jõao")
    retorno_esperado = cria_coluna("João")
    exclui_jogador("João")
    self.assertEqual(retorno_esperado, 1)

def teste_cria_coluna_jogador_inexistente(self):
    print("")
    retorno_esperado = cria_coluna("Deus")
    self.assertEqual(retorno_esperado, 0)

# def teste_combinacoes_possiveis():

class Tabela ou Pimport unittest

def teste_insere_jogador_sucesso(self):
    print("")
    retorno_esperado = insere_jogador("Teste")
    self.assertEqual(retorno_esperado,1)

def teste_insere_jogador_string_vazia(self):
    print("")
    retorno_esperado = insere_jogador("")
    self.assertEqual(retorno_esperado,0)

def teste_exclui_jogador_sucesso(self):
    print("")
    retorno_esperado = exclui_jogador("Teste")
    self.assertEqual(retorno_esperado, 0)

def teste_exclui_jogador_inexistente(self):
    print("")
    retorno_esperado = exclui_jogador("Deus")
    self.assertEqual(retorno_esperado, 1)

def teste_exclui_jogador_string_vazia(self):
    print("")
    retorno_esperado = exclui_jogador("")
    self.assertEqual(retorno_esperado, 2)

def teste_joga_sucesso(self):
    print("")
    lista_dados = [2,5]
    retorno_esperado = joga("Jogador",lista_dados)
    self.assertEqual(retorno_esperado, 0)

# def teste_joga_jogador_inexistente(self):
#     print("")
#     lista_dados = [1]
#     retorno_esperado = joga("Inexistente",lista_dados)
#     self.assertEqual(retorno_esperado, 1)

# def teste_joga_dado_inalcancavel():
#     print("")
#     lista_dados = [1,7]
#     retorno_esperado = joga("Jogador",lista_dados)

def teste_cria_tabela(self):
    print("")
    retorno_esperado = cria_tabela(self)
    self.assertEqual(retorno_esperado, 1)

def teste_cria_coluna_sucesso(self):
    print("")
    insere_jogador("Jõao")
    retorno_esperado = cria_coluna("João")
    exclui_jogador("João")
    self.assertEqual(retorno_esperado, 1)

def teste_cria_coluna_jogador_inexistente(self):
    print("")
    retorno_esperado = cria_coluna("Deus")
    self.assertEqual(retorno_esperado, 0)

# def teste_combinacoes_possiveis():

class Tabela ou Pontua_tabela(unittest.TestCase):
    def teste_1(self): #Testa se a função retorna uma pontuação valida (>=0)
        retorno_esperado = pontua_tabela("João", [1,2,3,4], "quadra")
        self.assertGreaterEqual(retorno_esperado, 0)

    def teste_2(self): #Testa a função se o jogador é inexistente
        retorno_esperado = pontua_tabela("", [1,2], "dupla")
        self.assertEqual(retorno_esperado, -1)

    def teste_3(self): #Testa a função quando o dado está fora de alcance ou é inválido
        retorno_esperado = pontua_tabela("João", [7,8], "dupla")
        self.assertEqual(retorno_esperado, -2)

    def teste_3(self): #Testa a função quando a a combinação é inválida
        retorno_esperado = pontua_tabela("João", [1,2], "dupppla")
        self.assertEqual(retorno_esperado, -3)

def teste_cosulta_tabela(self):
    retorno_esperado = consulta_tabela("Deus")
    self.assertEqual(retorno_esperado, -1)

def teste_pontuacao_final(self):
    retorno_esperado = pontuacao_final("Deus")
    self.assertEqual(retorno_esperado, -1)

def teste_exclui_tabela():
    retorno_esperado = exclui_tabela()
    self.assertEqual(retorno_esperado, 1)

ontua_tabela(unittest.TestCase):
    def teste_1(self): #Testa se a função retorna uma pontuação valida (>=0)
        retorno_esperado = pontua_tabela("João", [1,2,3,4], "quadra")
        self.assertGreaterEqual(retorno_esperado, 0)

    def teste_2(self): #Testa a função se o jogador é inexistente
        retorno_esperado = pontua_tabela("", [1,2], "dupla")
        self.assertEqual(retorno_esperado, -1)

    def teste_3(self): #Testa a função quando o dado está fora de alcance ou é inválido
        retorno_esperado = pontua_tabela("João", [7,8], "dupla")
        self.assertEqual(retorno_esperado, -2)

    def teste_3(self): #Testa a função quando a a combinação é inválida
        retorno_esperado = pontua_tabela("João", [1,2], "dupppla")
        self.assertEqual(retorno_esperado, -3)

def teste_cosulta_tabela(self):
    retorno_esperado = consulta_tabela("Deus")
    self.assertEqual(retorno_esperado, -1)

def teste_pontuacao_final(self):
    retorno_esperado = pontuacao_final("Deus")
    self.assertEqual(retorno_esperado, -1)

def teste_exclui_tabela():
    retorno_esperado = exclui_tabela()
    self.assertEqual(retorno_esperado, 1)

