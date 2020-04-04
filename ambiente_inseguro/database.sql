CREATE DATABASE ambienteInseguro;
use ambienteInseguro;

CREATE TABLE user (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    ncartao VARCHAR(30) NOT NULL
)

INSERT INTO user (id,nome, email, ncartao) VALUES (null,'Suzy Horto','suzy.horto@gmail.com','5332567898761234');
INSERT INTO user (id,nome, email, ncartao) VALUES (null,'Hugo Almeida','hugo.almeida@gmail.com','4332567298766789');
INSERT INTO user (id,nome, email, ncartao) VALUES (null,'Vitor Santos','vitor.amer@gmail.com','4332167898763456');