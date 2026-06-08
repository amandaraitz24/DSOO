from datetime import date, time


class TelaExame:
    def tela_opcoes(self):
        print("\n" + "="*40)
        print("🧬 MÓDULO DE EXAMES")
        print("="*40)
        print("1 - Agendar Exame")
        print("2 - Listar Exames")
        print("3 - Alterar Exame")
        print("4 - Cancelar Exame")
        print("5 - Registrar Resultado do Exame")
        print("0 - Voltar ao Menu Principal")
        print("="*40)
        return input("Escolha uma opção: ")

    def pegar_dados_exame(self):
        print("\n--- Novo Exame ---")
        try:
            paciente_id = input("ID do Paciente: ")
            profissional_id = input("ID do Profissional Responsável: ")
            clinica_id = input("ID da Clínica: ")
            tipo_exame = input("Tipo de Exame (Sangue/Raio-X/Ultrassom/etc): ")
            
            print("\nData do Exame (DD/MM/YYYY): ", end="")
            data_input = input()
            dia, mes, ano = map(int, data_input.split('/'))
            data_agendamento = date(ano, mes, dia)
            
            print("Hora do Exame (HH:MM): ", end="")
            hora_input = input()
            hora, minuto = map(int, hora_input.split(':'))
            hora_agendamento = time(hora, minuto)
            
            observacoes = input("Observações (opcional): ")
            
            return {
                "paciente_id": paciente_id,
                "profissional_id": profissional_id,
                "clinica_id": clinica_id,
                "tipo_exame": tipo_exame,
                "data_agendamento": data_agendamento,
                "hora_agendamento": hora_agendamento,
                "observacoes": observacoes
            }
        except (ValueError, IndexError):
            return None

    def pegar_resultado_exame(self):
        print("\n--- Registrar Resultado ---")
        exame_id = input("ID do Exame: ")
        resultado = input("Resultado do Exame: ")
        observacoes = input("Observações (opcional): ")
        
        return {
            "exame_id": exame_id,
            "resultado": resultado,
            "observacoes": observacoes
        }

    def pegar_dados_remarcar_exame(self):
        print("\n--- Remarcar Exame ---")
        try:
            exame_id = input("ID do Exame: ")
            
            print("Nova Data (DD/MM/YYYY): ", end="")
            data_input = input()
            dia, mes, ano = map(int, data_input.split('/'))
            nova_data = date(ano, mes, dia)
            
            print("Novo Horário (HH:MM): ", end="")
            hora_input = input()
            hora, minuto = map(int, hora_input.split(':'))
            nova_hora = time(hora, minuto)
            
            return {
                "exame_id": exame_id,
                "nova_data": nova_data,
                "nova_hora": nova_hora
            }
        except (ValueError, IndexError):
            return None

    def selecionar_exame(self):
        exame_id = input("\nID do Exame: ")
        return exame_id

    def mostrar_mensagem(self, msg):
        print(msg)

    def listar_exames(self, exames):
        if not exames:
            print("\n❌ Nenhum exame registrado.")
            return
        
        print("\n" + "="*80)
        print("EXAMES REGISTRADOS")
        print("="*80)
        for i, exame in enumerate(exames):
            print(f"{i} - {exame.exibir_dados()}")
        print("="*80)
