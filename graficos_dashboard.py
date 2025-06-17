
import matplotlib.pyplot as plt
import pandas as pd

# Query 1 – Indicadores Mês a Mês
df1 = pd.DataFrame({
    'mês': ['2021-05', '2021-06', '2021-07', '2021-08'],
    'leads (#)': [500, 600, 550, 700],
    'vendas (#)': [100, 120, 110, 150],
    'receita (k, R$)': [120, 150, 140, 180],
    'conversão (%)': [0.2, 0.2, 0.2, 0.21],
    'ticket médio (k, R$)': [1.2, 1.25, 1.27, 1.2]
})

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(df1['mês'], df1['leads (#)'], label='Leads', color='blue')
ax1.plot(df1['mês'], df1['vendas (#)'], label='Vendas', color='green')
ax1.plot(df1['mês'], df1['receita (k, R$)'], label='Receita (k)', color='orange')
ax1.set_ylabel('Leads / Vendas / Receita')
ax1.legend(loc='upper left')
ax2 = ax1.twinx()
ax2.plot(df1['mês'], df1['conversão (%)'], label='Conversão (%)', color='purple', linestyle='--')
ax2.plot(df1['mês'], df1['ticket médio (k, R$)'], label='Ticket Médio (k)', color='red', linestyle='--')
ax2.set_ylabel('Conversão / Ticket Médio')
ax2.legend(loc='upper right')
plt.title('Indicadores Mês a Mês')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Query 2 – Top 5 Estados
df2 = pd.DataFrame({
    'estado': ['SP', 'RJ', 'MG', 'RS', 'PR'],
    'vendas (#)': [180, 150, 120, 100, 90]
})
df2.plot.barh(x='estado', y='vendas (#)', color='skyblue', legend=False)
plt.xlabel('Vendas (#)')
plt.title('Top 5 Estados com Mais Vendas (Ago/2021)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Query 3 – Top 5 Marcas
df3 = pd.DataFrame({
    'marca': ['Marca A', 'Marca B', 'Marca C', 'Marca D', 'Marca E'],
    'vendas (#)': [100, 90, 85, 80, 75]
})
df3.plot.bar(x='marca', y='vendas (#)', color='green', legend=False)
plt.ylabel('Vendas (#)')
plt.title('Top 5 Marcas (Ago/2021)')
plt.tight_layout()
plt.show()

# Query 4 – Top 5 Lojas
df4 = pd.DataFrame({
    'loja': ['Loja A', 'Loja B', 'Loja C', 'Loja D', 'Loja E'],
    'vendas (#)': [90, 85, 70, 65, 60]
})
df4.plot.bar(x='loja', y='vendas (#)', color='coral', legend=False)
plt.ylabel('Vendas (#)')
plt.title('Top 5 Lojas (Ago/2021)')
plt.tight_layout()
plt.show()

# Query 5 – Visitas por Dia da Semana
df5 = pd.DataFrame({
    'dia da semana': ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'],
    'visitas (#)': [200, 300, 350, 400, 420, 500, 380]
})
df5['dia da semana'] = pd.Categorical(df5['dia da semana'],
    categories=['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'],
    ordered=True)
df5 = df5.sort_values('dia da semana')
df5.plot.bar(x='dia da semana', y='visitas (#)', color='steelblue', legend=False)
plt.ylabel('Visitas (#)')
plt.title('Visitas por Dia da Semana (Ago/2021)')
plt.tight_layout()
plt.show()
