from datetime import datetime
from agendamento import Agendamento
from tela_agendamento import TelaAgendamento
from exceptions import HorarioInvalidoException


class ControladorAgendamento:
    def __init__(self, controlador_sistema):
        self.__agendamentos = []
        self.__tela = TelaAgendamento()
        self.__controlador_sistema = controlador_sistema

    @property
    def agendamentos(self):
        return self.__agendamentos

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()

            if opcao == '1':
                self.agendar()

            elif opcao == '2':
                self.listar_agendamentos()

            elif opcao == '3':
                self.alterar_agendamento()

            elif opcao == '4':
                self.cancelar_agendamento()

            elif opcao == '5':
                self.confirmar_agendamento()

            elif opcao == '0':
                break

            else:
                self.__tela.mostrar_mensagem(
                    "❌ Opção inválida!"
                )

    def agendar(self):
        dados = self.__tela.pegar_dados_agendamento()

        if not dados:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Dados inválidos."
            )
            return

        try:
            # Obter referências dos objetos
            paciente = self.__obter_paciente(dados["paciente_id"])
            profissional = self.__obter_profissional(dados["profissional_id"])
            clinica = self.__obter_clinica(dados["clinica_id"])

            if not paciente or not profissional or not clinica:
                self.__tela.mostrar_mensagem(
                    "❌ Erro: Paciente, Profissional ou Clínica não encontrado."
                )
                return

            novo_agendamento = Agendamento(
                paciente,
                profissional,
                clinica,
                dados["data_agendamento"],
                dados["hora_agendamento"],
                dados["tipo_atendimento"]
            )

            if dados["observacoes"]:
                novo_agendamento.observacoes = dados["observacoes"]

            self.__agendamentos.append(novo_agendamento)
            self.__tela.mostrar_mensagem(
                "\n✅ Agendamento realizado com sucesso!"
            )

        except HorarioInvalidoException as e:
            self.__tela.mostrar_mensagem(f"\n❌ Erro: {e}")
        except Exception as e:
            self.__tela.mostrar_mensagem(f"\n❌ Erro inesperado: {e}")

    def listar_agendamentos(self):
        if not self.__agendamentos:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum agendamento registrado."
            )
            return

        print("\n" + "="*80)
        print("AGENDAMENTOS REGISTRADOS")
        print("="*80)

        for i, agendamento in enumerate(self.__agendamentos):
            print(f"{i} - {agendamento.exibir_dados()}")
            if agendamento.observacoes:
                print(f"   Observações: {agendamento.observacoes}")

        print("="*80)

    def alterar_agendamento(self):
        if not self.__agendamentos:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum agendamento para alterar."
            )
            return

        self.listar_agendamentos()

        try:
            agendamento_id = int(self.__tela.selecionar_agendamento())

            if agendamento_id < 0 or agendamento_id >= len(self.__agendamentos):
                self.__tela.mostrar_mensagem(
                    "❌ Agendamento não encontrado."
                )
                return

            dados = self.__tela.pegar_dados_remarcar()

            if not dados:
                self.__tela.mostrar_mensagem(
                    "❌ Erro: Dados inválidos."
                )
                return

            agendamento = self.__agendamentos[agendamento_id]
            agendamento.remarcar(
                dados["nova_data"],
                dados["nova_hora"]
            )

            self.__tela.mostrar_mensagem(
                "\n✅ Agendamento remarcado com sucesso!"
            )

        except (ValueError, HorarioInvalidoException) as e:
            self.__tela.mostrar_mensagem(f"\n❌ Erro: {e}")

    def cancelar_agendamento(self):
        if not self.__agendamentos:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum agendamento para cancelar."
            )
            return

        self.listar_agendamentos()

        try:
            agendamento_id = int(self.__tela.selecionar_agendamento())

            if agendamento_id < 0 or agendamento_id >= len(self.__agendamentos):
                self.__tela.mostrar_mensagem(
                    "❌ Agendamento não encontrado."
                )
                return

            agendamento = self.__agendamentos[agendamento_id]
            agendamento.cancelar()

            self.__tela.mostrar_mensagem(
                "\n✅ Agendamento cancelado com sucesso!"
            )

        except ValueError:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Digite um número válido."
            )

    def confirmar_agendamento(self):
        if not self.__agendamentos:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum agendamento para confirmar."
            )
            return

        self.listar_agendamentos()

        try:
            agendamento_id = int(self.__tela.selecionar_agendamento())

            if agendamento_id < 0 or agendamento_id >= len(self.__agendamentos):
                self.__tela.mostrar_mensagem(
                    "❌ Agendamento não encontrado."
                )
                return

            agendamento = self.__agendamentos[agendamento_id]
            agendamento.confirmar()

            self.__tela.mostrar_mensagem(
                "\n✅ Agendamento confirmado!"
            )

        except ValueError:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Digite um número válido."
            )

    def __obter_paciente(self, paciente_id):
        try:
            idx = int(paciente_id)
            pacientes = self.__controlador_sistema.controlador_paciente.pacientes
            if 0 <= idx < len(pacientes):
                return pacientes[idx]
        except (ValueError, IndexError):
            pass
        return None

    def __obter_profissional(self, profissional_id):
        try:
            idx = int(profissional_id)
            profissionais = self.__controlador_sistema.controlador_profissional.profissionais
            if 0 <= idx < len(profissionais):
                return profissionais[idx]
        except (ValueError, IndexError):
            pass
        return None

    def __obter_clinica(self, clinica_id):
        try:
            idx = int(clinica_id)
            clinicas = self.__controlador_sistema.controlador_clinica.clinicas if hasattr(
                self.__controlador_sistema, 'controlador_clinica') else []
            if clinicas and 0 <= idx < len(clinicas):
                return clinicas[idx]
        except (ValueError, IndexError):
            pass
        # Retornar clínica padrão
        return self.__controlador_sistema.clinica_padrao
