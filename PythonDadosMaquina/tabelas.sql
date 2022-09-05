CREATE USER 'sampUser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'samp';
GRANT ALL PRIVILEGES ON dadosMaquina.* TO 'sampUser'@'localhost';

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

----------------------------






