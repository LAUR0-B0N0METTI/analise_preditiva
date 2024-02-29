# Importar bibliotecas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt


# Carregar o DataFrame do arquivo Excel
df = pd.read_excel('C:\\Users\\nanni\\OneDrive\\Documentos\\Projetos Python\\Analise de Dados\\3 - Analise Preditiva\\base de dados\\Dados_excel.xlsx')


# Adicionar as colunas 'Ano', 'Mês', 'Dia'
df['Data'] = pd.to_datetime(df['Data'])
df['Ano'] = df['Data'].dt.year
df['Mês'] = df['Data'].dt.month
df['Dia'] = df['Data'].dt.day

# Selecionar as features para modelagem preditiva
features_preditivas = ['Ano', 'Mês', 'Dia', 'Loja', 'Tamanho']

# Criar variáveis dummy
X = pd.get_dummies(df[features_preditivas])
y = df['Quantidade']


# Preparar os dados para modelagem preditiva
features_preditivas = ['Ano', 'Mês', 'Dia', 'Loja', 'Tamanho']
X = pd.get_dummies(df[features_preditivas])
y = df['Quantidade']

# Dividir em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(X_train, y_train)

# Prever os resultados no conjunto de teste
y_pred = regressor.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')


