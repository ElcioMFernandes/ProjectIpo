CREATE DATABASE ProjetoIPO;

USE ProjetoIPO;

CREATE TABLE Veiculos (
	id_veiculo INT auto_increment primary key,
    placa VARCHAR(8) NOT NULL,
    marca VARCHAR(30) NOT NULL,
    modelo VARCHAR(30) NOT NULL,
    alocado boolean NOT NULL,
    cnh_requirida VARCHAR(1) NOT NULL,
    tipo_combustivel VARCHAR(8) NOT NULL,
    km FLOAT NOT NULL,
    quantidade_combustivel REAL NOT NULL,
    capacidade_tanque INT NOT NULL
);
