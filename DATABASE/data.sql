CREATE DATABASE IF NOT EXISTS `database`;

USE `database`;

CREATE TABLE colaborador(
    id_colaborador INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    veiculo int NOT NULL foreign key references veiculo(id_veiculo)
);

CREATE TABLE veiculo(
    id_veiculo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(30) NOT NULL,
    marca VARCHAR(30) NOT NULL,
    placa VARCHAR(8) NOT NULL UNIQUE,
    disponivel BOOLEAN NOT NULL,
    cnh_required VARCHAR(1) NOT NULL
);