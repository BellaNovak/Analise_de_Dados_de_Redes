import pandas as pd

def process_traffic_csv(input_file, output_file):
    # Carregar o arquivo CSV
    df = pd.read_csv(input_file)
    
    # Renomear apenas as colunas necessárias
    df.rename(columns={'Source': 'IP_Origem', 
                       'Destination': 'IP_Destino', 
                       'Protocol': 'Protocolo', 
                       'Length': 'Tamanho_Pacote', 
                       'Time': 'Tempo_Geracao'}, inplace=True)
    
    # Manter apenas as colunas relevantes
    df = df[['IP_Origem', 'IP_Destino', 'Protocolo', 'Tamanho_Pacote', 'Tempo_Geracao']]
    
    # Filtrar apenas protocolos ICMP e TCP
    df = df[df['Protocolo'].isin(['ICMP', 'TCP'])]
    
    # Criar uma chave de fluxo baseada no protocolo
    def define_fluxo(row):
        if row['Protocolo'].lower() == 'icmp':
            return (row['IP_Origem'], row['IP_Destino'], row['Protocolo'], row['Tamanho_Pacote'])
        else:
            return (row['IP_Origem'], row['IP_Destino'], row['Protocolo'])
    
    df['Fluxo'] = df.apply(define_fluxo, axis=1)
    
    # Agrupar os dados por fluxo
    grouped = df.groupby('Fluxo')
    
    # Criar estrutura para armazenar os resultados
    resultados = []
    
    for fluxo, dados in grouped:
        tamanho_medio = dados['Tamanho_Pacote'].mean()
        tamanho_min = dados['Tamanho_Pacote'].min()
        tamanho_max = dados['Tamanho_Pacote'].max()
        soma_tamanho = dados['Tamanho_Pacote'].sum()
        
        duracao_fluxo = dados['Tempo_Geracao'].max() - dados['Tempo_Geracao'].min()
        intervalos_tempo = dados['Tempo_Geracao'].diff().dropna()
        
        intervalo_medio = intervalos_tempo.mean() if not intervalos_tempo.empty else 0
        intervalo_min = intervalos_tempo.min() if not intervalos_tempo.empty else 0
        intervalo_max = intervalos_tempo.max() if not intervalos_tempo.empty else 0
        
        taxa_geracao = (soma_tamanho * 8 / duracao_fluxo) if duracao_fluxo > 0 else 0
        
        resultados.append([
            fluxo, duracao_fluxo, soma_tamanho, tamanho_max, tamanho_min, 
            tamanho_medio, intervalo_medio, intervalo_min, intervalo_max, taxa_geracao
        ])
    
    # Criar DataFrame de saída
    df_saida = pd.DataFrame(resultados, columns=[
        'Fluxo', 'Duracao_Fluxo', 'Soma_Tamanho', 'Tamanho_Maximo', 'Tamanho_Minimo',
        'Tamanho_Medio', 'Intervalo_Medio', 'Intervalo_Minimo', 'Intervalo_Maximo', 'Taxa_Geracao'
    ])
    
    # Salvar como CSV
    df_saida.to_csv(output_file, index=False)
    print(f"Arquivo de saída salvo em: {output_file}")

# Exemplo de uso:
process_traffic_csv('entrada.csv', 'saida.csv')