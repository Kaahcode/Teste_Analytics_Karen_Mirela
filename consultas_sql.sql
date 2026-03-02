USE consultas_sql;

DROP TABLE IF EXISTS vendas;

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    produto VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

INSERT INTO vendas (data, produto, categoria, quantidade, preco) VALUES
('2023-02-10', 'Bolsa', 'Acessórios', 120, 330.45),
('2023-03-15', 'Creme', 'Cosméticos', 800, 326.60),
('2023-04-20', 'Notebook', 'Eletrônicos', 40, 4335.45),
('2023-06-05', 'Tênis', 'Calçados', 350, 618.18),
('2023-08-18', 'Vestido', 'Vestuário', 200, 304.99);

SELECT * FROM vendas;

SELECT 
    produto,
    SUM(quantidade * preco) AS total_vendido
FROM vendas
WHERE data BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY produto
ORDER BY total_vendido DESC;