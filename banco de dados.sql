create database deployPA;
use deployPA;

create table usuarios(
id int primary key auto_increment,
nome varchar(100),
email varchar(200) unique not null,
senha varchar(300) not null,
tipo varchar(50) not null
);

insert into usuarios (nome,email,senha,tipo) values 
('Maria','maria@email.com','1234','cliente'),
('Carlos','carlos@email.com','1234','cliente'),
('Ana','ana@email.com','1234','admin'),
('Paulo','paulo@email.com','1234','admin');

select * from usuarios;