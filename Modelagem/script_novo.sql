CREATE DATABASE projetoSamp;
USE projetoSamp;



CREATE TABLE empresa (
    idEmpresa INT PRIMARY KEY AUTO_INCREMENT,
    nomeEmpresa VARCHAR(100),
    emailEmpresa VARCHAR(100),
    cnpj CHAR(14)
) AUTO_INCREMENT = 1;


CREATE TABLE usuario (
    idUsuario INT PRIMARY KEY AUTO_INCREMENT,
    fkEmpresa INT,
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(100),
    cargo VARCHAR(100),
    FOREIGN KEY (fkEmpresa) REFERENCES empresa(idEmpresa)
) AUTO_INCREMENT = 1;

CREATE TABLE memoria (
    idMemoria INT PRIMARY KEY AUTO_INCREMENT,
    qtdMemoria DOUBLE
) AUTO_INCREMENT = 1;




CREATE TABLE registroMemoria (
    idRegistroMemoria INT PRIMARY KEY AUTO_INCREMENT,
    fkMemoria INT,
    usoMemoria INT,
    momento DATETIME,
    FOREIGN KEY (fkMemoria) REFERENCES memoria(idMemoria)
) AUTO_INCREMENT = 1;

CREATE TABLE processador (
    idProcessador INT PRIMARY KEY AUTO_INCREMENT,
    modelo VARCHAR(45),
    qtdNucleosFisicos INT,
    qtdNucleosLogicos INT,
    frequenciaMaxima DOUBLE
) AUTO_INCREMENT = 1;

CREATE TABLE registroProcessador (
    idRegistroProcessador INT PRIMARY KEY AUTO_INCREMENT,
    fkProcessador INT,
    usoProcessador INT,
    frequenciaAtual DOUBLE,
    momento DATETIME,
    FOREIGN KEY (fkProcessador) REFERENCES processador(idProcessador)
) AUTO_INCREMENT = 1;

CREATE TABLE disco (
    idDisco INT PRIMARY KEY AUTO_INCREMENT,
    capacidade DOUBLE
) AUTO_INCREMENT = 1;

CREATE TABLE registroDisco (
    idRegistroDisco INT PRIMARY KEY AUTO_INCREMENT,
    fkDisco  INT,
    usoDisco INT,
    momento DATETIME,
    FOREIGN KEY (fkDisco) REFERENCES disco(idDisco)
) AUTO_INCREMENT = 1;

CREATE TABLE maquina (
    idMaquina CHAR(12) PRIMARY KEY,
    fkEmpresa INT,
    nome VARCHAR(45),
    fkMemoria INT,
    fkProcessador INT,
    fkDisco INT,
    FOREIGN KEY (fkEmpresa) REFERENCES empresa(idEmpresa),
    FOREIGN KEY (fkMemoria) REFERENCES memoria(idMemoria),
    FOREIGN KEY (fkProcessador) REFERENCES processador(idProcessador),
    FOREIGN KEY (fkDisco) REFERENCES disco(idDisco)
) AUTO_INCREMENT = 1;

insert into empresa values(null, 'C6', 'c6@email.com.br','22222222222222');
select * from empresa;
select * from usuario;
