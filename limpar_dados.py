import pandas as pd

# Ler arquivo criado
df = pd.read_csv("data_clean.csv")

print("Verificando valores vazios:")
print(df.isnull().sum())

# Remover valores vazios
df = df.dropna()

# Ajustar tipos
df["Data"] = pd.to_datetime(df["Data"])
df["Quantidade"] = df["Quantidade"].astype(int)
df["Preco"] = df["Preco"].astype(float)

print("\nDados prontos!")
print(df.info())

# Salvar novo arquivo
df.to_csv("vendas_limpo.csv", index=False)

print("Arquivo vendas_limpo.csv salvo com sucesso!")