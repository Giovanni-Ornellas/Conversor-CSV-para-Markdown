import csv
import os

# Caminho para o arquivo CSV
caminho_csv = "/home/asimov/Área de Trabalho/Github/Conversor-CSV-para-Markdown/Processo Seletivo MinervaBots.csv"

# Função para transformar os dados de uma linha em Markdown
def csv_para_markdown(linha, numero_linha):
    # Nome do arquivo .md para essa linha
    area  = linha[7]
    nome  = linha[1]
    nome_arquivo = f"{nome} - {area}.md"
    
    # Conteúdo do markdown
    markdown = f"## Dados da linha {numero_linha}\n\n"
    markdown += "| Coluna | Valor |\n"
    markdown += "|--------|-------|\n"
    
    for indice, valor in enumerate(linha):
        markdown += f"| Coluna {indice + 1} | {valor} |\n"
    
    # Salvar o markdown em um arquivo .md
    with open(nome_arquivo, 'w') as arquivo_md:
        arquivo_md.write(markdown)
    
    print(f"Arquivo {nome_arquivo} gerado com sucesso!")

# Verificar se o diretório existe, senão criar um
if not os.path.exists('markdowns'):
    os.makedirs('markdowns')

# Mudar o diretório de trabalho para a pasta 'markdowns'
os.chdir('markdowns')

# Abrindo o arquivo CSV e gerando um arquivo .md para cada linha
with open(caminho_csv, newline='') as csvfile:
    leitor_csv = csv.reader(csvfile)
    for numero_linha, linha in enumerate(leitor_csv, start=1):
        csv_para_markdown(linha, numero_linha)
