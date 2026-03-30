import pandas as pd

df = pd.read_excel('tarefas_python.xlsx')

print("--- Base de Dados Original ---")
print(df)
print("-" * 30)

df['media'] = (df['Nota1'] + df['Nota2']) / 2

def verificar_situacao(media):
    if media >= 6:
        return 'Aprovado'
    else:
        return 'Reprovado'

df['situacao'] = df['media'].apply(verificar_situacao)

print("\n--- Resultado Final ---")
print(df)
