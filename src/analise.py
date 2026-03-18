import pandas as pd

# carregar dados
df = pd.read_csv('../data/jogadores.csv')

# visão geral
print("\n=== DADOS ===")
print(df.head())

# estatísticas
print("\n=== ESTATÍSTICAS ===")
print(df.describe())

# jogadores com maior carga
print("\n=== MAIOR CARGA ===")
print(df.sort_values(by='carga_treino', ascending=False))

# correlação
print("\n=== CORRELAÇÃO ===")
print(df.corr(numeric_only=True))

# risco de lesão
risco = df[df['carga_treino'] > 85]

print("\n=== RISCO DE LESÃO ===")
print(risco)