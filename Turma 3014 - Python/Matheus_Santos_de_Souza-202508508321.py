import pandas as pd

arquivo = ('tarefa_python.xlsx')

df = pd.read_excel(arquivo)

print(df)

df["Média"] = (df["Nota 1"] + df["Nota 2"])/2

print(df)

df["Situação"] = df["Média"].apply(lambda x: "Aprovado" if x >= 6 else "Reprovado")

print(df)