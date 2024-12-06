-- Crear base de datos
CREATE DATABASE IF NOT EXISTS heladeria2;
USE heladeria2;

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

-- Crear tabla de bases
CREATE TABLE IF NOT EXISTS bases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    precio FLOAT NOT NULL
);

-- Crear tabla de ingredientes
CREATE TABLE IF NOT EXISTS ingredientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    precio FLOAT NOT NULL,
    es_sano BOOLEAN NOT NULL DEFAULT 0
);

-- Crear tabla de complementos
CREATE TABLE IF NOT EXISTS complementos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    precio FLOAT NOT NULL
);

-- Crear tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    precio FLOAT NOT NULL,
    base_id INT NOT NULL,
    usuario_id INT NOT NULL,
    calorias INT DEFAULT 0,
    rentabilidad FLOAT DEFAULT 0.0,
    costo_produccion FLOAT DEFAULT 0.0,
    stock INT DEFAULT 0,
    stock_maximo INT DEFAULT 100 NOT NULL,
    FOREIGN KEY (base_id) REFERENCES bases(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insertar datos iniciales en bases
INSERT INTO bases (nombre, precio) VALUES
('Base de Vainilla', 5.0),
('Base de Chocolate', 6.0),
('Base de Fresa', 5.5),
('Base de Limón', 5.8),
('Base de Coco', 6.0);

-- Insertar datos iniciales en ingredientes
INSERT INTO ingredientes (nombre, precio, es_sano) VALUES
('Fresa', 1.0, 1),
('Banano', 1.5, 1);

-- Insertar datos iniciales en complementos
INSERT INTO complementos (nombre, precio) VALUES
('Chispas de Chocolate', 0.5),
('Sirope de Fresa', 0.75);

-- Insertar datos iniciales en usuarios
INSERT INTO usuarios (username, password_hash) VALUES
('admin', '$2b$12$defaultpasswordhashvalue');

-- Insertar datos iniciales en productos
INSERT INTO productos (nombre, precio, base_id, usuario_id, calorias, rentabilidad, costo_produccion, stock) VALUES
('Helado de Vainilla', 7.50, 1, 1, 150, 0.2, 5.0, 10),
('Helado de Chocolate', 8.00, 2, 1, 200, 0.3, 6.0, 5);

-- Consultar datos
SELECT * FROM usuarios;
SELECT * FROM bases;
SELECT * FROM ingredientes;
SELECT * FROM complementos;
SELECT * FROM productos;
