import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# --- ETAPA 1: LEITURA DOS DADOS ---
# Certifique-se que o arquivo 'base_dados_ia.xlsx' está na mesma pasta que este código!
df = pd.read_excel('base_dados_ia.xlsx')
print("--- Base de Dados Carregada ---")
print(df.head())
print(df.info())

# --- ETAPA 2: PREPARAÇÃO DOS DADOS ---
# Tratando inconsistências (removendo espaços vazios) e mapeando o resultado
df['resultado'] = df['resultado'].str.strip()
df['resultado_num'] = df['resultado'].map({'Aprovado': 1, 'Reprovado': 0})

# Separando X e y
X = df[['nota1', 'nota2', 'frequencia', 'horas_estudo']]
y = df['resultado_num']

# --- ETAPA 3: CRIAÇÃO DO MODELO ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# --- ETAPA 4: AVALIAÇÃO ---
previsoes = modelo.predict(X_test)
acuracia = accuracy_score(y_test, previsoes)
print(f"\n✅ Acurácia do Modelo: {acuracia:.2%}")
print("\nRelatório de Desempenho:")
print(classification_report(y_test, previsoes))

# --- ETAPA 5: PROBABILIDADES ---
# Pegando as probabilidades de aprovação (coluna 1) para o grupo de teste
probabilidades = modelo.predict_proba(X_test)[:, 1]

print("\n--- ETAPA 5: ANÁLISE DE PROBABILIDADES (Exemplos) ---")
for i in range(5): # Mostra os 5 primeiros do teste
    print(f"Aluno {i+1}: Chance de Aprovação: {probabilidades[i]:.2f} -> {'Alta chance' if probabilidades[i] > 0.7 else 'Risco'}")