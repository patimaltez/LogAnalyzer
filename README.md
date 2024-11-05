# LogAnalyzer

## Descrição
**LogAnalyzer** é um projeto Python para automação de análise de logs.

## Funcionalidades
- Processamento de arquivos de log em massa.
- Classificação de eventos por níveis de severidade (`ERROR`, `WARN`, `SUCESSO`, `INFO`).
- Armazenamento dos dados em um arquivo Excel.
- Geração automática de gráficos de linha em formato PNG.
- Envio de e-mails de notificação informando o status da execução e erros.

## Estrutura de Arquivos
- `analisandologs_codeforgit.py`: Script principal que processa os logs e gera o arquivo Excel.
- `plotlogs_codeforgit.py`: Script para gerar gráficos a partir do arquivo Excel.
- `logs`: Pasta de entrada onde os logs devem ser armazenados.
- `logs/analises`: Sugestão de nome de pasta onde os arquivos Excel e gráficos gerados serão salvos.
- `logs/logstratados`: Sugestão de nome de pasta para logs processados.
- `logs/erroAnaliseLog`: Sugestão de nome de pasta para logs que tiveram erros na análise.

## Pré-requisitos
- Python 3.7+
- Bibliotecas: `pandas`, `matplotlib`, `seaborn`, `pywin32`
- App Outlook: instalado e com conta de email configurada para enviar e receber

Para instalar as dependências, execute:
`pip install pandas matplotlib seaborn pywin32`

## Observações
- Atenção à extensão dos seus arquivos de log, necessário adaptar o código para o seu cenário.
- Código em inglês, porém comentários e mensagens em português.
- Para automatizar esse projeto, siga as instruções do arquivo AUTOMATING.md
- Esse projeto foi testado no ambiente Windows com o Microsoft Outlook configurado.
- 

## Como Usar
- Coloque os arquivos de log na pasta logs;
- Configure no Outlook o email a ser utilizado no script;
- Execute o script analisandologs_codeforgit.py:
- execute o script plotlogs_codeforgit.py;

Os logs serão processados e o resultado será salvo em um arquivo Excel na pasta logs/analises.
Os logs processados serão movidos para a pasta logs/logstratados, e logs com erro serão movidos para logs/erroAnaliseLog.
Um e-mail será enviado ao final da execução.
O script plotlogs_codeforgit.py abrirá o arquivo Excel criado e salvará o gráfico PNG na pasta logs/analises.

## Licença
Este projeto está sob a licença GNU Affero General Public License v3.0. Veja o arquivo LICENSE para mais detalhes.
