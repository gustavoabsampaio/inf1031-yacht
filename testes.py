import unittest
from dado import *
from jogada import *
from jogador import *
from tabela import *

if __name__ == "__main__":
    unittest.main()

class Jogador(unittest.TestCase):

    def teste_insere_jogador_sucesso(self):
        
        retorno_esperado = insere_jogador("Teste")
        self.assertEqual(retorno_esperado,1)

    def teste_insere_jogador_string_vazia(self):
        
        retorno_esperado = insere_jogador("")
        self.assertEqual(retorno_esperado,0)

    def teste_exclui_jogador_sucesso(self):
        retorno_esperado = exclui_jogador("Teste")
        self.assertEqual(retorno_esperado, 0)

    def teste_exclui_jogador_inexistente(self):
        retorno_esperado = exclui_jogador("Deus")
        self.assertEqual(retorno_esperado, 1)


class Jogada(unittest.TestCase):

    def teste_proximo_jogador(self):
        retorno_esperado = proximo_jogador(["Jogador1","Jogador2"])
        self.assertEqual(retorno_esperado, 1)

    def teste_incrementa_jogada(self):
        retorno_esperado = incrementa_jogada()
        self.assertEqual(retorno_esperado, 1)

    def teste_incrementa_rodada(self):
        retorno_esperado = incrementa_jogada()
        self.assertEqual(retorno_esperado, 1)

    def teste_reseta_jogada(self):
        retorno_esperado = reseta_jogada()
        self.assertEqual(retorno_esperado, 1)

    def teste_reseta_rodada(self):
        retorno_esperado = reseta_rodada()
        self.assertEqual(retorno_esperado, 1)

    def teste_reseta_jogador_atual(self):
        retorno_esperado = reseta_jogador_atual()
        self.assertEqual(retorno_esperado, 1)

    



class Dado(unittest.TestCase):

    def teste_combinacoes_possiveis_1(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(1,retorno_esperado)
        
    def teste_combinacoes_possiveis_2(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(2,retorno_esperado)

    def teste_combinacoes_possiveis_3(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(3,retorno_esperado)

    def teste_combinacoes_possiveis_4(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(4,retorno_esperado)
        
    def teste_combinacoes_possiveis_5(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(5,retorno_esperado)

    def teste_combinacoes_possiveis_6(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,6])
        self.assertIn(6,retorno_esperado)

    def teste_combinacoes_possiveis_trinca(self):
        retorno_esperado = combinacoes_possiveis([1,1,1,4,6])
        self.assertIn(7,retorno_esperado)

    def teste_combinacoes_possiveis_quadra(self):
        retorno_esperado = combinacoes_possiveis([1,1,1,1,6])
        self.assertIn(8,retorno_esperado)

    def teste_combinacoes_possiveis_full_house(self):
        retorno_esperado = combinacoes_possiveis([1,1,1,2,2])
        self.assertIn(9,retorno_esperado)

    def teste_combinacoes_possiveis_seq_a(self):
        retorno_esperado = combinacoes_possiveis([2,3,4,5,6])
        self.assertIn(10,retorno_esperado)

    def teste_combinacoes_possiveis_seq_b(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(11,retorno_esperado)

    def teste_combinacoes_possiveis_yam(self):
        retorno_esperado = combinacoes_possiveis([1,1,1,1,1])
        self.assertIn(12,retorno_esperado)

    def teste_combinacoes_possiveis_nenhuma(self):
        retorno_esperado = combinacoes_possiveis([0,0,0,0,0])
        self.assertIn(9,retorno_esperado)

class Tabela(unittest.TestCase):

    def teste_cria_tabela(self):
        retorno_esperado = cria_tabela()
        self.assertEqual(retorno_esperado, 1)

    def teste_cria_coluna_sucesso(self):
        insere_jogador("Jõao")
        retorno_esperado = cria_coluna("João")
        exclui_jogador("João")
        self.assertEqual(retorno_esperado, 1)

    def teste_cria_coluna_jogador_inexistente(self):
        retorno_esperado = cria_coluna("Deus")
        self.assertEqual(retorno_esperado, 0)

    def teste_pontua_tabela_sucesso(self): 
        retorno_esperado = pontua_tabela("João", [1,2,3,4], "quadra")
        self.assertGreaterEqual(retorno_esperado, 0)

    def teste_pontua_tabela_jogador_inexistente(self):
        retorno_esperado = pontua_tabela("", [1,2], "trinca")
        self.assertEqual(retorno_esperado, -1)

    def teste_pontua_tabela_dado_erro(self):
        retorno_esperado = pontua_tabela("João", [7,8], "trinca")
        self.assertEqual(retorno_esperado, -2)

    def teste_pontua_tabela_combinacao_invalida(self):
        retorno_esperado = pontua_tabela("João", [1,2], "dupppla")
        self.assertEqual(retorno_esperado, -3)

    def teste_consulta_tabela(self):
        retorno_esperado = consulta_tabela("Deus")
        self.assertEqual(retorno_esperado, -1)

    def teste_pontuacao_final(self):
        retorno_esperado = pontuacao_final("Deus")
        self.assertEqual(retorno_esperado, -1)

    def teste_exclui_tabela(self):
        retorno_esperado = exclui_tabela()
        self.assertEqual(retorno_esperado, 1)

    # def teste_combinacoes_possiveis(self):


