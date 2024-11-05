# Log Analyzer Automating

Este documento orienta como automatizar a execução dos scripts.

1. **Usando NotePad crie um arquivo .bat com o seguinte conteúdo**:
   ```bash
   @echo off
   C:\path\to\python.exe C:\path\to\analisandologs_codeforgit.py
   ```
   - Substitua C:\path\to\python.exe pelo caminho do seu .exe Python
   - Substitua C:\path\to\analisandologs_codeforgit.py pelo caminho onde salvou o script.
   - Salve o arquivo com a extensão .bat

2. **Crie tarefa no agendador do Windows**:
   - Pressione `Win + R`, digite `taskschd.msc`, pressione `Enter`
   - Configure a tarefa no afendador conforme suas necessidades
   - Na aba Ações, em Novo, selecione "Iniciar um programa" e coloque o script .bat que você criou

### Observações:
- Esse agendador serve para servidores dedicados à automação durante sua execução.
- Se você não pode parar de usar determinado servidor e ao mesmo tempo precisa que o script execute, indico usar o Heroku.
- Repetir esse passo a passo para criar o .bat do script plotlogs_codeforgit.py
