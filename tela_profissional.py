class TelaProfissional:

    def tela_opcoes(self):
        print("\n--- 👨‍⚕️ MÓDULO DE PROFISSIONAIS ---")
        print("1 - Cadastrar Profissional")
        print("2 - Listar Profissionais")
        print("3 - Alterar Profissional")
        print("4 - Excluir Profissional")
        print("0 - Voltar")

        return input("Escolha uma opção: ")

    def pegar_dados_profissional(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        celular = input("Celular: ")
        especialidade = input("Especialidade: ")
        registro = input("Registro profissional: ")

        return {
            "nome": nome,
            "cpf": cpf,
            "celular": celular,
            "especialidade": especialidade,
            "registro": registro
        }

    def mostrar_mensagem(self, msg):
        print(msg)