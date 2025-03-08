# Análise de Dados de Redes

Projeto desenvolvido na disciplina Redes de Computadores, com o objetivo de analisar os dados de fluxo de uma rede.

Recebe de entrada um arquivo CSV gerado pelo Wireshark e como saída um arquivo CSV com os atributos de cada fluxo de tráfego.

São gerados 9 atributos por fluxo, sendo divididos em 3 grupos. 

O primeiro é relacionado ao tamanho dos pacotes: tamanho médio dos pacotes do fluxo (bytes) - tamanho mínimo dos pacotes do fluxo - tamanho máximo dos pacotes do fluxo - soma do tamanho de todos os pacotes

O segundo é relacionado ao intervalo de tempo de geração de pacotes:  duração do fluxo (segundo) - média do intervalo de tempo de geração dos pacotes - intervalo mínimo de tempo de geração de pacotes - intervalo máximo de tempo de geração de pacotes

O terceiro é relacionado a taxa de geração de pacotes: taxa média de geração dos pacotes (bits por segundo)
