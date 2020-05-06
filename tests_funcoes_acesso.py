import unittest
from dado import *
from jogada import *
from jogador import *
from tabela import *

if __name__ == "__main__":
    unittest.main()

class Jogador(unittest.TestCase):

    def test_insere_jogador_sucesso(self):
        
        retorno_esperado = insere_jogador("Teste")
        exclui_jogador("Teste")
        self.assertEqual(retorno_esperado,1)

    def test_insere_jogador_string_vazia(self):
        
        retorno_esperado = insere_jogador("")
        self.assertEqual(retorno_esperado,0)

    def test_exclui_jogador_sucesso(self):
        insere_jogador("Teste")
        retorno_esperado = exclui_jogador("Teste")
        self.assertEqual(retorno_esperado, 0)

    def test_exclui_jogador_inexistente(self):
        retorno_esperado = exclui_jogador("Deus")
        self.assertEqual(retorno_esperado, 1)

class Jogada(unittest.TestCase):

    def teste_proximo_jogador(self):
        jogador_atual = get_jogador_atual()
        retorno_esperado = proximo_jogador(["Jogador1","Jogador2"])
        reseta_jogador_atual()
        self.assertNotEqual(retorno_esperado, jogador_atual)

    def teste_incrementa_jogada(self):
        jogada = get_jogada()
        retorno_esperado = incrementa_jogada()
        reseta_jogada()
        self.assertNotEqual(retorno_esperado, jogada)

    def teste_incrementa_rodada(self):
        rodada = get_rodada()
        retorno_esperado = incrementa_rodada()
        reseta_rodada()
        self.assertNotEqual(retorno_esperado, rodada)

    def teste_reseta_jogada(self):
        incrementa_jogada()
        retorno_esperado = reseta_jogada()
        self.assertEqual(retorno_esperado, 1)

    def teste_reseta_rodada(self):
        incrementa_rodada()
        retorno_esperado = reseta_rodada()
        self.assertEqual(retorno_esperado, 1)

    def teste_reseta_jogador_atual(self):
        proximo_jogador(["Jonas","Bonas"])
        retorno_esperado = reseta_jogador_atual()
        self.assertEqual(retorno_esperado, 1)

class Dado(unittest.TestCase):

    def test_combinacoes_possiveis_1(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(1,retorno_esperado)
        
    def test_combinacoes_possiveis_2(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(2,retorno_esperado)

    def test_combinacoes_possiveis_3(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(3,retorno_esperado)

    def test_combinacoes_possiveis_4(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(4,retorno_esperado)
        
    def test_combinacoes_possiveis_5(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(5,retorno_esperado)

    def test_combinacoes_possiveis_6(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,6])
        self.assertIn(6,retorno_esperado)

    def test_combinacoes_possiveis_trinca(self):
        retorno_esperado = combinacoes_possiveis([1,1,1,4,6])
        self.assertIn(7,retorno_esperado)

    def test_combinacoes_possiveis_quadra(self):
        retorno_esperado = combinacoes_possiveis([1,1,1,1,6])
        self.assertIn(8,retorno_esperado)

    def test_combinacoes_possiveis_full_house(self):
        retorno_esperado = combinacoes_possiveis([1,1,1,2,2])
        self.assertIn(9,retorno_esperado)

    def test_combinacoes_possiveis_seq_a(self):
        retorno_esperado = combinacoes_possiveis([2,3,4,5,6])
        self.assertIn(10,retorno_esperado)

    def test_combinacoes_possiveis_seq_b(self):
        retorno_esperado = combinacoes_possiveis([1,2,3,4,5])
        self.assertIn(11,retorno_esperado)

    def test_combinacoes_possiveis_yam(self):
        retorno_esperado = combinacoes_possiveis([1,1,1,1,1])
        self.assertIn(12,retorno_esperado)

class Tabela(unittest.TestCase):

    def test_cria_coluna_sucesso(self):
        insere_jogador("João")
        retorno_esperado = cria_coluna("João")
        exclui_colunas()
        exclui_jogador("João")
        self.assertEqual(retorno_esperado, 1)

    def test_cria_coluna_jogador_inexistente(self):
        retorno_esperado = cria_coluna("Deus")
        self.assertEqual(retorno_esperado, 0)

    def test_pontua_tabela_sucesso(self):
        insere_jogador("João")
        cria_coluna("João")
        retorno_esperado = pontua_tabela(0, [1,4,4,4,4], 8)
        exclui_jogador("João")
        exclui_colunas()
        self.assertGreaterEqual(retorno_esperado, 0)

    def test_pontua_tabela_jogador_inexistente(self):
        retorno_esperado = pontua_tabela(2, [1,2,3,4,5], 7)
        self.assertEqual(retorno_esperado, -1)

    def test_pontua_tabela_dado_erro(self):
        insere_jogador("João")
        cria_coluna("João")
        retorno_esperado = pontua_tabela(0, [7,8], 7)
        exclui_jogador("João")
        exclui_colunas()
        self.assertEqual(retorno_esperado, -2)

    def test_pontua_tabela_combinacao_invalida(self):
        retorno_esperado = pontua_tabela(0, [1,2,3,4,5], 13)
        self.assertEqual(retorno_esperado, -3)

    def test_consulta_tabela_sucesso(self):
        insere_jogador("João")
        cria_coluna("João")
        retorno_esperado = consulta_tabela(0)
        exclui_jogador("João")
        exclui_colunas()
        self.assertIsInstance(retorno_esperado, list)

    def test_consulta_tabela_inexistente(self):
        retorno_esperado = consulta_tabela(1)
        self.assertEqual(retorno_esperado, -1)

    def test_pontuacao_final_sucesso(self):
        insere_jogador("João")
        cria_coluna("João")
        retorno_esperado = pontuacao_final(0)
        exclui_jogador("João")
        exclui_colunas()
        self.assertNotEqual(retorno_esperado, -1)

    def test_pontuacao_final_inexistente(self):
        insere_jogador("João")
        cria_coluna("João")
        retorno_esperado = pontuacao_final(1)
        exclui_jogador("João")
        exclui_colunas()
        self.assertEqual(retorno_esperado, -1)

    # def test_combinacoes_possiveis(self):


