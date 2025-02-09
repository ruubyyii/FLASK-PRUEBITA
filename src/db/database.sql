DROP DATABASE IF EXISTS pruebita_tienda;
CREATE DATABASE pruebita_tienda;
USE pruebita_tienda;

CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(155),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE productos(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    precio FLOAT UNSIGNED,
    categoria VARCHAR(50)
);

CREATE TABLE users_productos(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    id_user INT UNSIGNED,
    id_producto INT UNSIGNED,

    FOREIGN KEY (id_user) REFERENCES users(id),
    FOREIGN KEY (id_producto) REFERENCES productos(id)
);