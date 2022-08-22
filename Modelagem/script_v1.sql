CREATE DATABASE SAMP;

USE SAMP;

CREATE TABLE tbEmpresa
    (
    idEmpresa int primary key auto_increment,
    nome varchar(100),
    email varchar(100),
    cnpj char(14)
    )
;


CREATE TABLE tbUsuario
    (
    idUsuario int primary key auto_increment,
    fkEmpresa int,
    nome varchar(100),
    email varchar(100),
    senha varchar(100),
    cargo varchar(100),
    foreign key(fkEmpresa) references tbEmpresa(idEmpresa) 
    )
;

CREATE TABLE tbMaquina
    (
    idMaquina int primary auto_increment,
    fkEmpresa int,
    nome varchar(100),
    so varchar(100),
    modelo_cpu varchar(100),
    qtd_nucleos_f varchar(100),
    qtd_nucleos_l varchar(100),
    freq_cpu_max varchar(100),
    freq_cpu_min varchar(100),
    temp_cpu_max varchar(100),
    memoria_ram varchar(100),
    local_disco varchar(100),
    capac_disco varchar(100),
    foreign key(fkEmpresa) references tbEmpresa(idEmpresa) 
    )
;

CREATE TABLE tbRegistro
    (
    idRegistro int primary key auto_increment,
    fkMaquina int,
    uso_cpu varchar(100),
    temp_cpu varchar(100),
    freq_cpu varchar(100),
    uso_memoria varchar(100),
    uso_disco varchar(100),
    data_hora_regis datetime,
    foreign key(fkMaquina) references tbMaquina(idMaquina)
    )
;