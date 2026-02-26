import pandas as pd
import matplotlib.pyplot as plt

# Ler dados limpos
df = pd.read_csv("vendas_limpo.csv")

# Criar coluna total
df["Total"] = df["Quantidade"] * df["Preco"]

# Somar por produto
total_produto = df.groupby("Produto")["Total"].sum()

print("Total de vendas por produto:")
print(total_produto)

# Criar gráfico
total_produto.plot(kind="bar")

plt.title("Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Total em R$")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("grafico_produto.png")
plt.show()

print("Gráfico grafico_produto.png salvo!")