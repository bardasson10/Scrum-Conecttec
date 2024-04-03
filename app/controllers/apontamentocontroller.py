from flask import render_template
from app.api.tickets import make_api_request
from app import app
from datetime import datetime, timedelta
import pytz

@app.route('/apontamentos/<int:ticketNumber>')
def apontamentos(ticketNumber):
    try:
        # Constrói a URL da API com o número do ticket
        url = f'https://api.tiflux.com/api/v1/tickets/{ticketNumber}/appointments?limit=20'

        # Realiza a chamada à API usando a função make_api_request
        data = make_api_request(url)

        if data:
            # Definindo o fuso horário de Brasília
            brtz = pytz.timezone('America/Sao_Paulo')

            # Converter as datas dos apontamentos para o fuso horário de Brasília e remover o deslocamento de fuso horário
            for apontamento in data:
                apontamento['beginning'] = datetime.strptime(apontamento['beginning'], "%Y-%m-%dT%H:%M:%S.%fZ")
                apontamento['ending'] = datetime.strptime(apontamento['ending'], "%Y-%m-%dT%H:%M:%S.%fZ")
                
                # Calcular a diferença entre o início e o fim
                diferenca = apontamento['ending'] - apontamento['beginning']
                
                #Formatar data
                apontamento['beginning'] = datetime.strftime(apontamento['beginning'], "%d/%m/%Y %H:%M")
                apontamento['ending'] = datetime.strftime(apontamento['ending'],"%H:%M")
               
                

                # Armazenar a diferença como a duração do apontamento
                apontamento['duracao'] = diferenca

            # Ordena os apontamentos por datas de início e fim
            data.sort(key=lambda x: (x.get('beginning', ''), x.get('ending', '')))

            # Numerando os tickets em sequência
            for i, apontamento in enumerate(data):
                apontamento['ticket_number'] = i + 1

            # Renderiza a página de visualização com os dados da API ordenados
            return render_template('apontamentos.html', data=data)
        else:
            # Lida com erros de chamada à API
            return render_template('apontamentos.html', error="Erro na chamada à API")
    except Exception as e:
        # Lida com exceções
        return render_template('apontamentos.html', error=str(e))