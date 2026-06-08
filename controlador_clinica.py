from datetime import time
from clinica import Clinica
from tela_clinica import TelaClinica


class ControladorClinica:
    def __init__(self, controlador_sistema):
        self.__clinicas = []
        self.__tela = TelaClinica()
        self.__controlador_sistema = controlador_sistema

    @property
    def clinicas(self):
        return self.__clinicas

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()

            if opcao == '1':
                self.registrar_clinica()

            elif opcao == '2':
                self.listar_clinicas()

            elif opcao == '3':
                self.alterar_clinica()

            elif opcao == '4':
                self.remover_clinica()

            elif opcao == '5':
                self.exibir_detalhes_clinica()

            elif opcao == '0':
                break

            else:
                self.__tela.mostrar_mensagem(
                    "❌ Opção inválida!"
                )

    def registrar_clinica(self):
        dados = self.__tela.pegar_dados_clinica()

        if not dados:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Dados inválidos."
            )
            return

        try:
            nova_clinica = ClinicaEstendida(
                dados["nome"],
                dados["endereco"],
                dados["descricao"],
                dados["horario_abertura"],
                dados["horario_fechamento"]
            )
            
            nova_clinica.telefone = dados["telefone"]
            nova_clinica.email = dados["email"]
            nova_clinica.especialidades = dados["especialidades"]

            self.__clinicas.append(nova_clinica)

            self.__tela.mostrar_mensagem(
                "\n✅ Clínica registrada com sucesso!"
            )

        except Exception as e:
            self.__tela.mostrar_mensagem(f"\n❌ Erro: {e}")

    def listar_clinicas(self):
        if not self.__clinicas:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhuma clínica registrada."
            )
            return

        print("\n" + "="*80)
        print("CLÍNICAS REGISTRADAS")
        print("="*80)

        for i, clinica in enumerate(self.__clinicas):
            print(f"{i} - {clinica.exibir_dados()}")

        print("="*80)

    def alterar_clinica(self):
        if not self.__clinicas:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhuma clínica para alterar."
            )
            return

        self.listar_clinicas()

        try:
            clinica_id = int(self.__tela.selecionar_clinica())

            if clinica_id < 0 or clinica_id >= len(self.__clinicas):
                self.__tela.mostrar_mensagem(
                    "❌ Clínica não encontrada."
                )
                return

            dados = self.__tela.pegar_dados_alteracao_clinica()

            if not dados:
                self.__tela.mostrar_mensagem(
                    "❌ Erro: Dados inválidos."
                )
                return

            clinica = self.__clinicas[clinica_id]

            if dados["nome"]:
                clinica.nome = dados["nome"]
            if dados["endereco"]:
                clinica.endereco = dados["endereco"]
            if dados["telefone"]:
                clinica.telefone = dados["telefone"]
            if dados["email"]:
                clinica.email = dados["email"]
            if dados["horario_abertura"]:
                clinica.horario_abertura = dados["horario_abertura"]
            if dados["horario_fechamento"]:
                clinica.horario_fechamento = dados["horario_fechamento"]

            self.__tela.mostrar_mensagem(
                "\n✅ Clínica alterada com sucesso!"
            )

        except ValueError:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Digite um número válido."
            )

    def remover_clinica(self):
        if not self.__clinicas:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhuma clínica para remover."
            )
            return

        self.listar_clinicas()

        try:
            clinica_id = int(self.__tela.selecionar_clinica())

            if clinica_id < 0 or clinica_id >= len(self.__clinicas):
                self.__tela.mostrar_mensagem(
                    "❌ Clínica não encontrada."
                )
                return

            clinica_removida = self.__clinicas.pop(clinica_id)

            self.__tela.mostrar_mensagem(
                f"\n✅ Clínica '{clinica_removida.nome}' removida com sucesso!"
            )

        except ValueError:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Digite um número válido."
            )

    def exibir_detalhes_clinica(self):
        if not self.__clinicas:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhuma clínica registrada."
            )
            return

        self.listar_clinicas()

        try:
            clinica_id = int(self.__tela.selecionar_clinica())

            if clinica_id < 0 or clinica_id >= len(self.__clinicas):
                self.__tela.mostrar_mensagem(
                    "❌ Clínica não encontrada."
                )
                return

            clinica = self.__clinicas[clinica_id]
            self.__tela.exibir_detalhes_clinica(clinica)

        except ValueError:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Digite um número válido."
            )


class ClinicaEstendida(Clinica):
    """Extensão da classe Clinica com campos adicionais"""
    
    def __init__(self, nome, endereco, descricao, horario_abertura, horario_fechamento):
        super().__init__(nome, endereco, descricao, horario_abertura, horario_fechamento)
        self._ClinicaEstendida__telefone = ""
        self._ClinicaEstendida__email = ""
        self._ClinicaEstendida__especialidades = []

    @property
    def telefone(self):
        return self._ClinicaEstendida__telefone

    @telefone.setter
    def telefone(self, telefone):
        self._ClinicaEstendida__telefone = telefone

    @property
    def email(self):
        return self._ClinicaEstendida__email

    @email.setter
    def email(self, email):
        self._ClinicaEstendida__email = email

    @property
    def especialidades(self):
        return self._ClinicaEstendida__especialidades

    @especialidades.setter
    def especialidades(self, especialidades):
        self._ClinicaEstendida__especialidades = especialidades
