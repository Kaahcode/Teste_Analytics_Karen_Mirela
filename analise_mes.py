import pandas as pd
import matplotlib.pyplot as plt

# Ler dados limpos
df = pd.read_csv("vendas_limpo.csv")

# Converter data
df["Data"] = pd.to_datetime(df["Data"])

# Criar mês
df["Mes"] = df["Data"].dt.month

# Criar total
df["Total"] = df["Quantidade"] * df["Preco"]

# Somar por mês
total_mes = df.groupby("Mes")["Total"].sum()

print("Vendas por mês:")
print(total_mes)

# Criar gráfico
plt.plot(total_mes.index, total_mes.values)

plt.title("Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Total em R$")

plt.tight_layout()
plt.savefig("grafico_mes.png")
plt.show()

print("Gráfico grafico_mes.png salvo!")