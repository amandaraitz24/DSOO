class TelaPaciente:

    def tela_opcoes(self):

        print("\n--- 👥 MÓDULO DE PACIENTES ---")
        print("1 - Cadastrar Novo Paciente")
        print("2 - Listar Pacientes")
        print("3 - Alterar Paciente")
        print("4 - Excluir Paciente")
        print("0 - Voltar")

        return input("Escolha a opção: ")

    def pegar_dados_paciente(self):

        print("\n--- DADOS DO NOVO PACIENTE ---")

        nome = input("Nome Completo: ")
        cpf = input("CPF (apenas números): ")
        celular = input("Celular: ")

        print("Data de Nascimento:")

        try:

            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))

            return {
                "nome": nome,
                "cpf": cpf,
                "celular": celular,
                "dia": dia,
                "mes": mes,
                "ano": ano
            }

        except ValueError:
            return None

    def pegar_dados_alteracao_paciente(self, paciente):
        """
        Mostra os dados atuais do paciente e pede novos valores.
        Campos vazios mantêm os valores atuais.
        Retorna dict com chaves possivelmente vazias ou None se cancelado.
        """
        print("\n--- ALTERAR PACIENTE ---")
        print(f"Paciente atual: {paciente.exibir_dados()}")
        print(f"Idade atual: {paciente.calcular_idade()} anos")

        novo_nome = input(f"Novo nome [{paciente.nome}]: ")
        novo_cpf = input(f"Novo CPF [{paciente.cpf}]: ")
        novo_celular = input(f"Novo celular [{paciente.celular}]: ")

        print("\nSe desejar alterar data de nascimento, preencha os campos abaixo. Caso contrário, pressione Enter para manter a data atual.")
        try:
            dia_input = input("Dia (DD): ")
            if dia_input.strip() == "":
                dia = None
            else:
                dia = int(dia_input)

            mes_input = input("Mês (MM): ")
            if mes_input.strip() == "":
                mes = None
            else:
                mes = int(mes_input)

            ano_input = input("Ano (YYYY): ")
            if ano_input.strip() == "":
                ano = None
            else:
                ano = int(ano_input)

        except ValueError:
            return None

        return {
            "nome": novo_nome,
            "cpf": novo_cpf,
            "celular": novo_celular,
            "dia": dia,
            "mes": mes,
            "ano": ano
        }

    def mostrar_mensagem(self, msg):
        print(msg)