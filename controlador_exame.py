from datetime import datetime
from exame import Exame
from tela_exame import TelaExame
from exceptions import HorarioInvalidoException


class ControladorExame:
    def __init__(self, controlador_sistema):
        self.__exames = []
        self.__tela = TelaExame()
        self.__controlador_sistema = controlador_sistema

    @property
    def exames(self):
        return self.__exames

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()

            if opcao == '1':
                self.agendar_exame()

            elif opcao == '2':
                self.listar_exames()

            elif opcao == '3':
                self.alterar_exame()

            elif opcao == '4':
                self.cancelar_exame()

            elif opcao == '5':
                self.registrar_resultado()

            elif opcao == '0':
                break

            else:
                self.__tela.mostrar_mensagem(
                    "❌ Opção inválida!"
                )

    def agendar_exame(self):
        dados = self.__tela.pegar_dados_exame()

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

            novo_exame = Exame(
                paciente,
                profissional,
                clinica,
                dados["tipo_exame"],
                dados["data_agendamento"],
                dados["hora_agendamento"]
            )

            if dados["observacoes"]:
                novo_exame.observacoes = dados["observacoes"]

            self.__exames.append(novo_exame)
            self.__tela.mostrar_mensagem(
                "\n✅ Exame agendado com sucesso!"
            )

        except HorarioInvalidoException as e:
            self.__tela.mostrar_mensagem(f"\n❌ Erro: {e}")
        except Exception as e:
            self.__tela.mostrar_mensagem(f"\n❌ Erro inesperado: {e}")

    def listar_exames(self):
        if not self.__exames:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum exame registrado."
            )
            return

        print("\n" + "="*80)
        print("EXAMES REGISTRADOS")
        print("="*80)

        for i, exame in enumerate(self.__exames):
            print(f"{i} - {exame.exibir_dados()}")
            if exame.resultado:
                print(f"   Resultado: {exame.resultado}")
            if exame.observacoes:
                print(f"   Observações: {exame.observacoes}")

        print("="*80)

    def alterar_exame(self):
        if not self.__exames:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum exame para alterar."
            )
            return

        self.listar_exames()

        try:
            exame_id = int(self.__tela.selecionar_exame())

            if exame_id < 0 or exame_id >= len(self.__exames):
                self.__tela.mostrar_mensagem(
                    "❌ Exame não encontrado."
                )
                return

            dados = self.__tela.pegar_dados_remarcar_exame()

            if not dados:
                self.__tela.mostrar_mensagem(
                    "❌ Erro: Dados inválidos."
                )
                return

            exame = self.__exames[exame_id]
            exame.remarcar(
                dados["nova_data"],
                dados["nova_hora"]
            )

            self.__tela.mostrar_mensagem(
                "\n✅ Exame remarcado com sucesso!"
            )

        except (ValueError, HorarioInvalidoException) as e:
            self.__tela.mostrar_mensagem(f"\n❌ Erro: {e}")

    def cancelar_exame(self):
        if not self.__exames:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum exame para cancelar."
            )
            return

        self.listar_exames()

        try:
            exame_id = int(self.__tela.selecionar_exame())

            if exame_id < 0 or exame_id >= len(self.__exames):
                self.__tela.mostrar_mensagem(
                    "❌ Exame não encontrado."
                )
                return

            exame = self.__exames[exame_id]
            exame.cancelar()

            self.__tela.mostrar_mensagem(
                "\n✅ Exame cancelado com sucesso!"
            )

        except ValueError:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Digite um número válido."
            )

    def registrar_resultado(self):
        if not self.__exames:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum exame registrado."
            )
            return

        self.listar_exames()

        try:
            dados = self.__tela.pegar_resultado_exame()
            exame_id = int(dados["exame_id"])

            if exame_id < 0 or exame_id >= len(self.__exames):
                self.__tela.mostrar_mensagem(
                    "❌ Exame não encontrado."
                )
                return

            exame = self.__exames[exame_id]
            exame.realizar_exame(dados["resultado"])

            if dados["observacoes"]:
                exame.observacoes = dados["observacoes"]

            self.__tela.mostrar_mensagem(
                "\n✅ Resultado do exame registrado!"
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
