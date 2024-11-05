import os
import shutil
import re
import pandas as pd
import win32com.client as win32
from datetime import datetime

# Diretórios
log_dir = r"C:\adicione o path onde estão os logs"
processed_log_dir = r"C:\adicione o path para o qual os logs analisados devem ser movidos"
error_log_dir = r"C:\adicione o path para o qual os logs com erro na leitura devem ser movidos"

# Configurações do e-mail para usar o app outlook
def send_email(subject, body):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    
    # Configurar a conta específica para enviar o email
    account = None
    for acc in outlook.Session.Accounts:
        if acc.SmtpAddress == "seu_email@gmail.com.br":
            account = acc
            break
            
    if account is None:
        print("Conta de email não encontrada.")
        return

    mail.Subject = subject
    mail.Body = body
    mail.To = "email_destinatario@gmail.com"
    mail.SendUsingAccount = account
    mail.Send()

# Verificar se a pasta de logs existe
if not os.path.exists(log_dir):
    send_email("RPA - Análise de Logs - Erro de Execução", "A pasta de logs não foi encontrada. Execução interrompida.")
    exit()

# Listar os arquivos de log que estão na pasta no início da execução
initial_log_files = [f for f in os.listdir(log_dir) if f.endswith('.log')]

# Verificar se há arquivos na pasta de logs
if not initial_log_files:
    send_email("RPA - Análise de Logs - Execução Interrompida", "Nenhum log encontrado na pasta. Execução interrompida.")
    exit()

# Criar pasta de logs analisados e logs com erro na análise, se não existir
if not os.path.exists(processed_log_dir):
    os.makedirs(processed_log_dir)

if not os.path.exists(error_log_dir):
    os.makedirs(error_log_dir)

# Lista vazia para armazenar os dados processados
data = []


# Todo esse bloco deve ser personalizado de acordo com as necessidades de analise do seu log
# Função para processar o arquivo de log
def process_log_file(log_path):
    with open(log_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            # Procurar hora e descrição do evento
            match = re.search(r'(\d{2}:\d{2}:\d{2}) (.*)', line)
            if match:
                time = match.group(1)
                message = match.group(2)

                # Classificação de severidade
                if "ERROR" in message:
                    severity = "ERROR"
                elif "WARN" in message:
                    severity = "WARN"
                elif "SUCCESS" in message:
                    severity = "SUCESSO"
                else:
                    severity = "INFO"

                # Adicionar os dados ao DataFrame
                data.append([time, severity, message])

# Processar os arquivos .log listados
for log_file in initial_log_files:
    log_path = os.path.join(log_dir, log_file)
    
    try:
        process_log_file(log_path)
        destination_path = os.path.join(processed_log_dir, log_file)
        counter = 1
        while os.path.exists(destination_path):
            base_name, extension = os.path.splitext(log_file)
            destination_path = os.path.join(processed_log_dir, f"{base_name}_{counter}{extension}")
            counter += 1

        # Mover o arquivo processado para a pasta de logs analisados
        shutil.move(log_path, destination_path)
    
    except UnicodeDecodeError:
        # Em caso de erro de decodificação, tentar abrir com uma codificação diferente
        try:
            with open(log_path, 'r', encoding='ISO-8859-1') as file:
                lines = file.readlines()
                for line in lines:
                    match = re.search(r'(\d{2}:\d{2}:\d{2}) (.*)', line)
                    if match:
                        time = match.group(1)
                        message = match.group(2)

                        # Classificação
                        if "ERROR" in message:
                            severity = "ERROR"
                        elif "WARN" in message:
                            severity = "WARN"
                        elif "SUCCESS" in message:
                            severity = "SUCESSO"
                        else:
                            severity = "INFO"

                        # Adicionar os dados ao DataFrame
                        data.append([time, severity, message])

            # Mover o arquivo para a pasta de logs analisados
            destination_path = os.path.join(processed_log_dir, log_file)
            counter = 1
            while os.path.exists(destination_path):
                base_name, extension = os.path.splitext(log_file)
                destination_path = os.path.join(processed_log_dir, f"{base_name}_{counter}{extension}")
                counter += 1
            shutil.move(log_path, destination_path)
        
        except Exception as e_inner:
            # Mover o arquivo para a pasta de logs com erro e notificar
            shutil.move(log_path, error_log_dir)
            send_email("RPA - Análise de Logs - Erro de Análise de Log", f"Erro ao ler o arquivo {log_file}. Ele foi movido para 'erroAnaliseLog'.\nDetalhes: {e_inner}")

    except Exception as e:
        # Mover o arquivo para a pasta de logs com erro e notificar
        shutil.move(log_path, error_log_dir)
        send_email("RPA - Análise de Logs - Erro de Análise de Log", f"Erro ao ler o arquivo {log_file}. Ele foi movido para 'erroAnaliseLog'.\nDetalhes: {e}")

# Salvar os dados em um arquivo Excel, caso existam registros processados
if data:
    # Organizar dados no DataFrame
    df = pd.DataFrame(data, columns=["Horário", "Severidade", "Descrição do Evento"]) 
    # Criar um nome de arquivo único com a data e hora atual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"logs_organizados_{timestamp}.xlsx"
    output_path = r"C:\path onde os xlsx devem ficar"
    full_output_path = f"{output_path}\\{filename}"
    # Salvar o arquivo Excel com o nome gerado
    df.to_excel(full_output_path, index=False) 

send_email("RPA - Análise de Logs - Execução Completa", "Os logs foram processados e movidos para a pasta 'logstratados'.")