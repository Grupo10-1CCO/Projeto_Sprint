CREATE USER 'sampUser'@'localhost' IDENTIFIED BY 'samp';
GRANT ALL PRIVILEGES ON samp.* TO 'sampUser'@'localhost';

create database samp;
use samp;

drop database samp;

CREATE TABLE EMPRESA(
  cnpj char(18) primary key,
  nomeEmpresa varchar(60)
);

create table usuario(
  idUsuario int primary key auto_increment,
  senha varchar(45),
  nomeUsuario varchar(60),
  email varchar(60) unique,
  funcao char(1),
  fkEmpresa char(18),
  foreign key(fkEmpresa) references empresa(cnpj)
);

create table servidor(
  idServidor int primary key auto_increment,
  modelo varchar(45),
  fkEmpresa char(18),
  foreign key(fkEmpresa) references empresa(cnpj)
);

create table registro(
  idRegistro int primary key auto_increment,
  usoCpu int,
  usoMemoria double,
  usoDisco double,
  dataHoraReg datetime,
  fkServidor int,
  foreign key(fkServidor) references servidor(idServidor)
);

select * from empresa;
select * from usuario;

