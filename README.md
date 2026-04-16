# Organizador Automático de Arquivos

Script desenvolvido para automatizar a organização de pastas (por exemplo, a pasta "Downloads"), distribuindo os arquivos em subpastas de acordo com suas extensões. O objetivo é demonstrar a aplicação de lógica de programação para resolver tarefas operacionais repetitivas.

## Funcionalidades

- Leitura de todos os arquivos de um diretório especificado.
- Classificação baseada na extensão do arquivo.
- Movimentação dos arquivos para subpastas predefinidas (Documentos, Imagens, Planilhas, Vídeos, etc.).
- Criação automática das pastas de destino, caso não existam.

## Tecnologias

- Python 3 (módulos `os` e `shutil`)

## Configuração necessária

Antes de executar, é preciso ajustar a variável `pasta_alvo` no código para o caminho do diretório que se deseja organizar.

### Exemplo no Windows:
`pasta_alvo = r"C:\Users\SeuUsuario\Downloads"`

### Exemplo no Linux:
`pasta_alvo = "/home/seuUsuario/Downloads"`

## Como executar
python organizador.py

## Observações
Recomenda-se fechar programas que possam estar utilizando arquivos do diretório alvo antes da execução, para evitar erros de permissão.

## Autora

**Barbara Carvalho**  
[LinkedIn](https://linkedin.com/in/bcarv-eng)
