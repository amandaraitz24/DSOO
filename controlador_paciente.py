from datetime import date
from paciente import Paciente
from tela_paciente import TelaPaciente


class ControladorPaciente:

    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__tela = TelaPaciente()
        self.__controlador_sistema = controlador_sistema

    @property
    def pacientes(self):
        return self.__pacientes

    def abre_tela(self):

        while True:

            opcao = self.__tela.tela_opcoes()

            if opcao == '1':
                self.incluir_paciente()

            elif opcao == '2':
                self.listar_pacientes()

            elif opcao == '3':
                self.alterar_paciente()

            elif opcao == '4':
                self.excluir_paciente()

            elif opcao == '0':
                break

            else:
                self.__tela.mostrar_mensagem(
                    "❌ Opção inválida!"
                )

    def incluir_paciente(self):

        dados = self.__tela.pegar_dados_paciente()

        if not dados:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Digite apenas números na data."
            )
            return

        try:

            data_nasc = date(
                dados["ano"],
                dados["mes"],
                dados["dia"]
            )

            novo_paciente = Paciente(
                dados["nome"],
                dados["celular"],
                dados["cpf"],
                data_nasc
            )

            self.__pacientes.append(
                novo_paciente
            )

            self.__tela.mostrar_mensagem(
                "\n✅ Paciente cadastrado!"
            )

        except ValueError:

            self.__tela.mostrar_mensagem(
                "❌ Data inválida."
            )

    def listar_pacientes(self):

        if not self.__pacientes:

            self.__tela.mostrar_mensagem(
                "Não há pacientes registrados."
            )

            return

        print("\n--- PACIENTES CADASTRADOS ---")

        for i, paciente in enumerate(
                self.__pacientes):

            self.__tela.mostrar_mensagem(
                f"{i} - "
                f"{paciente.exibir_dados()} "
                f"| Idade: "
                f"{paciente.calcular_idade()} anos"
            )

    def excluir_paciente(self):

        if not self.__pacientes:

            self.__tela.mostrar_mensagem(
                "Não há pacientes cadastrados."
            )

            return

        self.listar_pacientes()

        try:

            indice = int(
                input(
                    "Índice do paciente: "
                )
            )

            del self.__pacientes[indice]

            self.__tela.mostrar_mensagem(
                "✅ Paciente removido."
            )

        except:

            self.__tela.mostrar_mensagem(
                "❌ Índice inválido."
            )

    def alterar_paciente(self):

        if not self.__pacientes:

            self.__tela.mostrar_mensagem(
                "Não há pacientes cadastrados."
            )

            return

        self.listar_pacientes()

        try:

            indice = int(
                input(
                    "Índice do paciente: "
                )
            )

            paciente = self.__pacientes[indice]

            # Usar tela para obter dados de alteração (mostra atuais e aceita vazio)
            dados = self.__tela.pegar_dados_alteracao_paciente(paciente)

            if dados is None:
                self.__tela.mostrar_mensagem(
                    "❌ Erro: Dados inválidos para alteração."
                )
                return

            # Atualizar apenas os campos preenchidos pelo usuário
            if dados.get("nome"):
                paciente._Pessoa__nome = dados["nome"]

            if dados.get("cpf"):
                paciente._Pessoa__cpf = dados["cpf"]

            if dados.get("celular"):
                paciente._Pessoa__celular = dados["celular"]

            # Se a data foi informada completamente, atualiza
            if dados.get("dia") and dados.get("mes") and dados.get("ano"):
                try:
                    nova_data = date(dados["ano"], dados["mes"], dados["dia"])
                    paciente._Paciente__data_nascimento = nova_data
                except ValueError:
                    self.__tela.mostrar_mensagem(
                        "❌ Data inválida. Data não foi alterada."
                    )

            self.__tela.mostrar_mensagem(
                "✅ Paciente alterado com sucesso."
            )

        except:

            self.__tela.mostrar_mensagem(
                "❌ Erro na alteração."
            )