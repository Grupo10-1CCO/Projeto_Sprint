CREATE DATABASE dadosMaquina;
USE dadosMaquina;

DROP DATABASE dadosMaquina;

CREATE TABLE empresa (
    idEmpresa INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    cnpj CHAR(14)
) AUTO_INCREMENT = 101;

CREATE TABLE usuario (
    idUsuario INT PRIMARY KEY AUTO_INCREMENT,
    fkEmpresa INT,
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(100),
    cargo VARCHAR(100),
    FOREIGN KEY (fkEmpresa) REFERENCES empresa(idEmpresa)
) AUTO_INCREMENT = 1001;

CREATE TABLE maquina (
    idMaquina CHAR(12) PRIMARY KEY,
    fkEmpresa INT,
    nome VARCHAR(45),
    FOREIGN KEY (fkEmpresa) REFERENCES empresa(idEmpresa)
) AUTO_INCREMENT = 1;

CREATE TABLE memoria (
    idMemoria INT PRIMARY KEY AUTO_INCREMENT,
    fkMaquina CHAR(12),
    qtdMemoria VARCHAR(45),
    frequenciaMemoria VARCHAR(45),
    FOREIGN KEY (fkMaquina) REFERENCES maquina(idMaquina)
) AUTO_INCREMENT = 101;

CREATE TABLE registroMemoria (
    idRegistroMemoria INT PRIMARY KEY AUTO_INCREMENT,
    fkMemoria INT,
    usoMemoria INT,
    momento DATETIME,
    FOREIGN KEY (fkMemoria) REFERENCES memoria(idMemoria)
) AUTO_INCREMENT = 1;

CREATE TABLE processador (
    idProcessador INT PRIMARY KEY AUTO_INCREMENT,
    fkMaquina CHAR(12),
    modelo VARCHAR(45),
    qtdNucleosFisicos INT,
    qtdNucleosLogicos INT,
    frequenciaMaxima DOUBLE,
    FOREIGN KEY (fkMaquina) REFERENCES maquina(idMaquina)
) AUTO_INCREMENT = 101;

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
    fkMaquina CHAR(12),
    capacidade VARCHAR(45),
    FOREIGN KEY (fkMaquina) REFERENCES maquina(idMaquina)
) AUTO_INCREMENT = 101;

CREATE TABLE registroDisco (
    idRegistroDisco INT PRIMARY KEY AUTO_INCREMENT,
    fkDisco  INT,
    usoDisco INT,
    momento DATETIME,
    FOREIGN KEY (fkDisco) REFERENCES disco(idDisco)
) AUTO_INCREMENT = 1;

SELECT * FROM empresa;
SELECT * FROM usuario;
SELECT * FROM maquina;
SELECT * FROM memoria;
SELECT * FROM registroMemoria;
SELECT * FROM processador;
SELECT * FROM registroProcessador;
SELECT * FROM disco;
SELECT * FROM registroDisco;
