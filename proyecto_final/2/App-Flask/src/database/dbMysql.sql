DROP DATABASE IF EXISTS usuarios;
CREATE DATABASE usuarios CHARACTER SET utf8 COLLATE utf8_spanish2_ci;
USE usuarios;


CREATE TABLE IF NOT EXISTS usuario(
   ID INT(3) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
   nombre VARCHAR(20) NOT NULL,
   apellidos VARCHAR(30) NOT NULL,
   password VARCHAR(15) NOT NULL,
   telefono VARCHAR(15),
   edad INT(3),
   PRIMARY KEY(ID)
);