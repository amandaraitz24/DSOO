from datetime import date, time


class TelaAgendamento:
    def tela_opcoes(self):
        print("\n" + "="*40)
        print("📅 MÓDULO DE AGENDAMENTOS")
        print("="*40)
        print("1 - Agendar Consulta/Exame")
        print("2 - Listar Agendamentos")
        print("3 - Alterar Agendamento")
        print("4 - Cancelar Agendamento")
        print("5 - Confirmar Agendamento")
        print("0 - Voltar ao Menu Principal")
        print("="*40)
        return input("Escolha uma opção: ")

    def pegar_dados_agendamento(self):
        print("\n--- Novo Agendamento ---")
        try:
            paciente_id = input("ID do Paciente: ")
            profissional_id = input("ID do Profissional: ")
            clinica_id = input("ID da Clínica: ")
            tipo_atendimento = input("Tipo de Atendimento (Consulta/Exame): ")
            
            print("\nData do Agendamento (DD/MM/YYYY): ", end="")
            data_input = input()
            dia, mes, ano = map(int, data_input.split('/'))
            data_agendamento = date(ano, mes, dia)
            
            print("Hora do Agendamento (HH:MM): ", end="")
            hora_input = input()
            hora, minuto = map(int, hora_input.split(':'))
            hora_agendamento = time(hora, minuto)
            
            observacoes = input("Observações (opcional): ")
            
            return {
                "paciente_id": paciente_id,
                "profissional_id": profissional_id,
                "clinica_id": clinica_id,
                "tipo_atendimento": tipo_atendimento,
                "data_agendamento": data_agendamento,
                "hora_agendamento": hora_agendamento,
                "observacoes": observacoes
            }
        except (ValueError, IndexError):
            return None

    def pegar_dados_remarcar(self):
        print("\n--- Remarcar Agendamento ---")
        try:
            agendamento_id = input("ID do Agendamento: ")
            
            print("Nova Data (DD/MM/YYYY): ", end="")
            data_input = input()
            dia, mes, ano = map(int, data_input.split('/'))
            nova_data = date(ano, mes, dia)
            
            print("Novo Horário (HH:MM): ", end="")
            hora_input = input()
            hora, minuto = map(int, hora_input.split(':'))
            nova_hora = time(hora, minuto)
            
            return {
                "agendamento_id": agendamento_id,
                "nova_data": nova_data,
                "nova_hora": nova_hora
            }
        except (ValueError, IndexError):
            return None

    def selecionar_agendamento(self):
        agendamento_id = input("\nID do Agendamento: ")
        return agendamento_id

    def mostrar_mensagem(self, msg):
        print(msg)

    def listar_agendamentos(self, agendamentos):
        if not agendamentos:
            print("\n❌ Nenhum agendamento registrado.")
            return
        
        print("\n" + "="*80)
        print("AGENDAMENTOS REGISTRADOS")
        print("="*80)
        for i, agendamento in enumerate(agendamentos):
            print(f"{i} - {agendamento.exibir_dados()}")
        print("="*80)
