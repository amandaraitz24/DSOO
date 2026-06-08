from datetime import time


class TelaClinica:
    def tela_opcoes(self):
        print("\n" + "="*40)
        print("🏥 MÓDULO DE CLÍNICAS")
        print("="*40)
        print("1 - Registrar Nova Clínica")
        print("2 - Listar Clínicas")
        print("3 - Alterar Dados da Clínica")
        print("4 - Remover Clínica")
        print("5 - Exibir Detalhes da Clínica")
        print("0 - Voltar ao Menu Principal")
        print("="*40)
        return input("Escolha uma opção: ")

    def pegar_dados_clinica(self):
        print("\n--- Nova Clínica ---")
        try:
            nome = input("Nome da Clínica: ")
            endereco = input("Endereço: ")
            descricao = input("Descrição: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            
            print("\nHorário de Abertura (HH:MM): ", end="")
            hora_input = input()
            hora, minuto = map(int, hora_input.split(':'))
            horario_abertura = time(hora, minuto)
            
            print("Horário de Fechamento (HH:MM): ", end="")
            hora_input = input()
            hora, minuto = map(int, hora_input.split(':'))
            horario_fechamento = time(hora, minuto)
            
            especialidades = input("Especialidades (separadas por vírgula): ")
            
            return {
                "nome": nome,
                "endereco": endereco,
                "descricao": descricao,
                "telefone": telefone,
                "email": email,
                "horario_abertura": horario_abertura,
                "horario_fechamento": horario_fechamento,
                "especialidades": [e.strip() for e in especialidades.split(',')]
            }
        except (ValueError, IndexError):
            return None

    def pegar_dados_alteracao_clinica(self):
        print("\n--- Alterar Clínica ---")
        clinica_id = input("ID da Clínica: ")
        
        print("\nDados a Alterar (deixe em branco para não alterar):")
        nome = input("Nome da Clínica: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        horario_abertura = input("Horário de Abertura (HH:MM): ")
        horario_fechamento = input("Horário de Fechamento (HH:MM): ")
        
        if horario_abertura:
            hora, minuto = map(int, horario_abertura.split(':'))
            horario_abertura = time(hora, minuto)
        else:
            horario_abertura = None

        if horario_fechamento:
            hora, minuto = map(int, horario_fechamento.split(':'))
            horario_fechamento = time(hora, minuto)
        else:
            horario_fechamento = None
        
        dados = {
            "clinica_id": clinica_id,
            "nome": nome,
            "endereco": endereco,
            "telefone": telefone,
            "email": email,
            "horario_abertura": horario_abertura,
            "horario_fechamento": horario_fechamento
        }
        
        return dados

    def selecionar_clinica(self):
        clinica_id = input("\nID da Clínica: ")
        return clinica_id

    def mostrar_mensagem(self, msg):
        print(msg)

    def listar_clinicas(self, clinicas):
        if not clinicas:
            print("\n❌ Nenhuma clínica registrada.")
            return
        
        print("\n" + "="*80)
        print("CLÍNICAS REGISTRADAS")
        print("="*80)
        for i, clinica in enumerate(clinicas):
            print(f"{i} - {clinica.exibir_dados()}")
        print("="*80)

    def exibir_detalhes_clinica(self, clinica):
        print("\n" + "="*80)
        print("DETALHES DA CLÍNICA")
        print("="*80)
        print(f"Nome: {clinica.nome}")
        print(f"Endereço: {clinica.endereco}")
        print(f"Descrição: {clinica.descricao}")
        print(f"Telefone: {clinica.telefone if hasattr(clinica, 'telefone') else 'N/A'}")
        print(f"Email: {clinica.email if hasattr(clinica, 'email') else 'N/A'}")
        print(f"Horário de Funcionamento: {clinica.horario_abertura.strftime('%H:%M')} - {clinica.horario_fechamento.strftime('%H:%M')}")
        if hasattr(clinica, 'especialidades'):
            print(f"Especialidades: {', '.join(clinica.especialidades)}")
        print("="*80)
