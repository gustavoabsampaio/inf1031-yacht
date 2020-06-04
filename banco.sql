DROP TABLE IF EXISTS jogada;
CREATE TABLE jogada (

	jogador_atual varchar(20) NOT NULL,
	rodada int NOT NULL,
	jogada int NOT NULL,
	fk_id_jogo int,														
	
	CONSTRAINT jogo_id_fk FOREIGN KEY (fk_id_jogo) REFERENCES jogo(id)
);

DROP TABLE IF EXISTS dados;
CREATE TABLE dados(
	id_jogo int NOT NULL,
	id int NOT NULL,
	valor int,
	CONSTRAINT pk_dados PRIMARY KEY (id),
	CONSTRAINT id_jogo_fk FOREIGN KEY (id_jogo) REFERENCES jogo(id)
	);

DROP TABLE IF EXISTS tabela;
CREATE TABLE tabela(
	nome_jogador varchar(50) NOt NULL,
	id_jogo int NOT NULL,
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

	CONSTRAINT tabela_pk PRIMARY KEY (nome_jogador, id_jogo),
	CONSTRAINT id_jogo_fk FOREIGN KEY (id_jogo) REFERENCES jogo(id)
);

DROP TABLE IF EXISTS jogo;
CREATE TABLE jogo(
	id int NOT NULL AUTO_INCREMENT,
	ultima_data date NOT NULL,

	CONSTRAINT pk_id PRIMARY KEY (id)
);