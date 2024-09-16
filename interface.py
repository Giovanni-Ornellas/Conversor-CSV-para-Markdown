import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Função para carregar arquivos markdown e exibir o conteúdo
def carregar_markdowns():
    caminho_pasta = filedialog.askdirectory()
    if not caminho_pasta:
        return  # Cancelado pelo usuário

    # Limpa a lista de arquivos
    lista_arquivos.delete(0, tk.END)

    # Carrega os arquivos .md do diretório selecionado
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith(".md"):
            lista_arquivos.insert(tk.END, arquivo)

# Função para exibir o conteúdo do markdown selecionado
def exibir_conteudo():
    arquivo_selecionado = lista_arquivos.get(tk.ACTIVE)
    if not arquivo_selecionado:
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado!")
        return

    caminho_arquivo = os.path.join("/home/asimov/Área de Trabalho/Github/Conversor-CSV-para-Markdown/Processo Seletivo MinervaBots.csv"
, "Processo Seletivo MinervaBots")

    # Lê o conteúdo do arquivo markdown
    with open("/home/asimov/Área de Trabalho/Github/Conversor-CSV-para-Markdown/Processo Seletivo MinervaBots.csv"
, 'r') as arquivo_md:
        conteudo = arquivo_md.read()

    # Exibe o conteúdo no widget de texto
    campo_conteudo.config(state=tk.NORMAL)
    campo_conteudo.delete(1.0, tk.END)
    campo_conteudo.insert(tk.END, conteudo)
    campo_conteudo.config(state=tk.DISABLED)

# Janela principal
janela = tk.Tk()
janela.title("Visualizador de Markdown")

# Layout da interface
frame_esquerdo = ttk.Frame(janela)
frame_esquerdo.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

frame_direito = ttk.Frame(janela)
frame_direito.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Botão para carregar arquivos Markdown
botao_carregar = ttk.Button(frame_esquerdo, text="Carregar Markdown", command=carregar_markdowns)
botao_carregar.pack(pady=10)

# Lista de arquivos .md
lista_arquivos = tk.Listbox(frame_esquerdo, height=20, width=30)
lista_arquivos.pack(pady=10)

# Botão para exibir o conteúdo do arquivo selecionado
botao_exibir = ttk.Button(frame_esquerdo, text="Exibir Conteúdo", command=exibir_conteudo)
botao_exibir.pack(pady=10)

# Campo de texto para exibir o conteúdo do markdown
campo_conteudo = tk.Text(frame_direito, wrap=tk.WORD, state=tk.DISABLED)
campo_conteudo.pack(fill=tk.BOTH, expand=True)

# Executar a janela principal
janela.mainloop()
