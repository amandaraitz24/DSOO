class TelaPrincipal:
    def tela_opcoes(self):
        print("\n" + "="*35)
        print("🏥 SISTEMA DE GESTÃO DE CLÍNICA")
        print("="*35)
        print("1 - Módulo de Pacientes")
        print("2 - Módulo de Atendimentos")
        print("3 - Módulo Financeiro (Pagamentos)")
        print("4 - Módulo de Profissionais")
        print("5 - Relatórios")
        print("6 - Módulo de Agendamentos")
        print("7 - Módulo de Exames")
        print("8 - Gestão de Clínicas")
        print("0 - Sair do Sistema")
        print("="*35)
        return input("Escolha uma opção: ")

    def mostrar_mensagem(self, msg):
        print(msg)