import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Definindo o diretório onde os arquivos estão localizados
analises_dir = r"C:\usar o mesmo diretório no qual os xlsx foram salvos"

# Listando todos os arquivos .xlsx no diretório
xlsx_files = [f for f in os.listdir(analises_dir) if f.endswith('.xlsx')]

for xlsx_file in xlsx_files:
    # Definindo o caminho completo do arquivo .xlsx
    caminho_arquivo = os.path.join(analises_dir, xlsx_file)
    print(f"Lendo o arquivo: {caminho_arquivo}")

    # Carregando os dados do arquivo Excel
    df = pd.read_excel(caminho_arquivo)

    # Convertendo o horário para datetime para uma melhor visualização no gráfico
    df['Horário'] = pd.to_datetime(df['Horário'], format='%H:%M:%S')

    # Plotando o gráfico com linhas para cada tipo de severidade
    print(f"Plotando o arquivo: {caminho_arquivo}")
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=df, x='Horário', y=df.groupby('Horário').cumcount(), hue='Severidade', marker='o')

    # Adicionando título e legendas
    plt.title("Ocorrências de Logs ao Longo do Tempo")
    plt.xlabel("Horário")
    plt.ylabel("Quantidade de Eventos")
    plt.legend(title="Severidade")
    plt.xticks(rotation=45)

    # Definindo o caminho para salvar o gráfico .png correspondente
    png_file = f"{xlsx_file.replace('.xlsx', '.png')}"
    caminho_salvar = os.path.join(analises_dir, png_file)

    # Verificando se o arquivo PNG já existe
    if not os.path.exists(caminho_salvar):
        plt.tight_layout()
        plt.savefig(caminho_salvar)
        print(f"Gráfico salvo em: {caminho_salvar}")
    else:
        print(f"O gráfico já existe: {caminho_salvar}")

    # Limpando a figura atual para evitar sobreposição
    plt.clf()