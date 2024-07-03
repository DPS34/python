import os

# Função para formatar uma sequência individual
def formatar_sequencia(sequencia):
    partes = [
        sequencia[0:2],    # 24
        sequencia[2:4],    # 06
        sequencia[4:6],    # 27
        sequencia[6:8],    # 17
        sequencia[8:10],   # 49
        sequencia[10:12],  # 15
        sequencia[12],     # V
        sequencia[13:20],  # 0000096
        sequencia[20:27],  # 0000096
        sequencia[27:34],  # 0000002
        sequencia[34:41],  # 0000002
        sequencia[41:48],  # 0000000
        sequencia[48:55],  # 0000000
        sequencia[55:62],  # 0000062
        sequencia[62:69],  # 0000034
        sequencia[69:76],  # 0000000
        sequencia[76:83],  # 0000000
    ]
    return ','.join(partes)

# Diretório onde os arquivos estão localizados
diretorio = '/Users/danilo.silva/sq'

# Listar todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# Iterar sobre os arquivos no diretório
for arquivo in arquivos:
    if arquivo.endswith('.txt'):  # Considerar apenas arquivos .txt
        caminho_arquivo = os.path.join(diretorio, arquivo)
        caminho_saida = os.path.join(diretorio, f"format.log")
        
        # Abrir o arquivo de entrada para leitura e o arquivo de saída para escrita
        with open(caminho_arquivo, 'r') as f_in, open(caminho_saida, 'w') as f_out:
            # Iterar sobre cada linha no arquivo de entrada
            for linha in f_in:
                # Remover espaços em branco e quebras de linha
                linha = linha.strip()
                
                # Verificar se a linha não está vazia
                if linha:
                    # Formatar a sequência e escrever no arquivo de saída
                    sequencia_formatada = formatar_sequencia(linha)
                    f_out.write(sequencia_formatada + '\n')
                    print(f'Sequência formatada: {sequencia_formatada}')
        
        print(f'As sequências foram formatadas e salvas em {caminho_saida}.')