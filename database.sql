create database db_ipo;

use db_ipo;

create table colab (
    id_colab INT PRIMARY KEY auto_increment,
    nome_colab VARCHAR(30) NOT NULL,
    sobrenome_colab VARCHAR(30) NOT NULL, 
    setor_colab VARCHAR(30) NOT NULL,
    permissao_colab INT NOT NULL
);