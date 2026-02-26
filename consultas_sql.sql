CREATE DATABASE projeto_vendas;
USE projeto_vendas;

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    produto VARCHAR(50),
    categoria VARCHAR(50),
    quantidade INT,
    preco DECIMAL(10,2)
);

INSERT INTO vendas (data, produto, categoria, quantidade, preco)
VALUES 
('2024-06-10', 'Tênis', 'Calçados', 5, 200.00),
('2024-06-15', 'Notebook', 'Eletrônicos', 2, 3500.00),
('2024-06-20', 'Bolsa', 'Vestuário', 3, 500.00);

SELECT 
    produto,
    categoria,
    SUM(quantidade * preco) AS total_vendas
FROM vendas
GROUP BY produto, categoria
ORDER BY total_vendas DESC;