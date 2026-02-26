import pandas as pd
import random
from datetime import datetime, timedelta

# Lista de produtos
produtos = ["Tênis", "Vestido", "Bolsa", "Creme", "Notebook"]

data_inicio = datetime(2023, 1, 1)
data_fim = datetime(2023, 12, 31)

dados = []

# Criar 50 vendas
for i in range(50):

    dias = (data_fim - data_inicio).days
    data = data_inicio + timedelta(days=random.randint(0, dias))

    produto = random.choice(produtos)
    quantidade = random.randint(1, 10)
    preco = round(random.uniform(20, 5000), 2)

    dados.append([data, produto, quantidade, preco])

# Criar tabela
df = pd.DataFrame(dados, columns=["Data", "Produto", "Quantidade", "Preco"])

print(df.head())

# Salvar arquivo
df.to_csv("data_clean.csv", index=False)

print("Arquivo data_clean.csv criado com sucesso!")