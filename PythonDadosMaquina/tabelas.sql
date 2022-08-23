CREATE USER 'dataUser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'urubu100';
GRANT ALL PRIVILEGES ON dadosMaquina.* TO 'dataUser'@'localhost';

create database dadosMaquina;
use dadosMaquina;

drop database dadosMaquina;

create table Usuario(
	idUsuario int primary key auto_increment,
    nome varchar(45),
    usuario varchar(45) unique,
    senha varchar(45)
)auto_increment = 1001;

create table maquina(
  serialNumber char(12) primary key,
  fkUsuario int,
  sistema varchar(45), 
  processador varchar(100), 
  qtdNucleos int, 
  qtdThreads int, 
  freqMaxCpu varchar(45), 
  freqMinCpu varchar(45),
  ramTotal varchar(45),
  discoPrincipal varchar(45),
  capacidadeDiscoPrincipal varchar(45),
  foreign key(fkUsuario) references Usuario(idUsuario)
);

create table dados(
	idDados int primary key auto_increment,
    fkMaquina char(12),
    usoMemoria int,
    usoCpu int,
    tempCpu double,
    frequenciaCpu double,
    usoDisco int,
    dataHoraRegistro datetime,
    foreign key(fkmaquina) references maquina(serialNumber)
)auto_increment = 101;

select * from maquina;
select * from Usuario;
select * from dados;

insert into dados(dataHoraRegistro) values('2022-08-22 01:51:48.131296');

SELECT idUsuario FROM usuario where nome = 'trt' and senha = MD5('123');

INSERT INTO maquina(sistema, processador, ramTotal) values ('{sistema}','{processador}', '{memoriaTotal}');

INSERT INTO usuario VALUES (NULL, '{nome}', '{user}', MD5('2234'));




SELECT idUsuario, nome, idMaquina FROM usuario
JOIN maquina ON fkUsuario = idUsuario where usuario = 'lari' and senha = MD5('123');

INSERT INTO maquina VALUES (NULL, 1002, '{sistema}', '{processador}', 1, 2, '{freqCpu}', '{freqMinCpu}', '{memoriaTotal}', '/dev', '{capacidadeDiscoPrincipal}');

INSERT INTO maquina VALUES (NULL, 1002, 'Linux', 'Intel(R) Core(TM) i3-8145U CPU @ 2.10GHz', 4, 2, '3.9Ghz', '4.0Ghz', ' 11.57GB', '/dev/nvme0n1p1', '0.0')



