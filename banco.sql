DROP TABLE IF EXISTS jogo;
CREATE TABLE jogo(
	id int NOT NULL AUTO_INCREMENT,
	ultima_data date NOT NULL,

	CONSTRAINT pk_id_jogo PRIMARY KEY (id)
);

DROP TABLE IF EXISTS jogada;
CREATE TABLE jogada (

	jogador_atual varchar(20) NOT NULL,
	rodada int NOT NULL,
	jogada int NOT NULL,
	fk_id_jogo int,												
	
	CONSTRAINT fk_jogada_jogo_id FOREIGN KEY (fk_id_jogo) REFERENCES jogo(id)
);

DROP TABLE IF EXISTS dados;
CREATE TABLE dados(
	fk_id_jogo int NOT NULL,
	id int NOT NULL,
	valor int,
	CONSTRAINT pk_dados PRIMARY KEY (id),
	CONSTRAINT fk_dados_jogo_id FOREIGN KEY (fk_id_jogo) REFERENCES jogo(id)
	);

DROP TABLE IF EXISTS tabela;
CREATE TABLE tabela(
	nome_jogador varchar(50) NOT NULL,
	fk_id_jogo int NOT NULL,
	jogada_1 int NULL,
	jogada_2 int NULL,
	jogada_3 int NULL,
	jogada_4 int NULL,
	jogada_5 int NULL,
	jogada_6 int NULL,
	trinca int NULL,	
	quadra int NULL,
	full_house int NULL,
	sequencia_a int NULL,
	sequencia_b int NULL,
	yam int NULL,

	CONSTRAINT pk_nome_id_tabela PRIMARY KEY (nome_jogador, fk_id_jogo),
	CONSTRAINT fk_tabela_jogo_id FOREIGN KEY (fk_id_jogo) REFERENCES jogo(id)
);

