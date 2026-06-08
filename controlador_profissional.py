from profissional import Profissional
from tela_profissional import TelaProfissional


class ControladorProfissional:

    def __init__(self, controlador_sistema):
        self.__profissionais = []
        self.__tela = TelaProfissional()
        self.__controlador_sistema = controlador_sistema

    @property
    def profissionais(self):
        return self.__profissionais

    def abre_tela(self):

        while True:

            opcao = self.__tela.tela_opcoes()

            if opcao == "1":
                self.incluir_profissional()

            elif opcao == "2":
                self.listar_profissionais()

            elif opcao == "3":
                self.alterar_profissional()

            elif opcao == "4":
                self.excluir_profissional()

            elif opcao == "0":
                break

            else:
                self.__tela.mostrar_mensagem(
                    "Opção inválida."
                )

    def incluir_profissional(self):

        dados = self.__tela.pegar_dados_profissional()

        profissional = Profissional(
            dados["nome"],
            dados["celular"],
            dados["cpf"],
            dados["especialidade"],
            dados["registro"]
        )

        self.__profissionais.append(
            profissional
        )

        self.__tela.mostrar_mensagem(
            "Profissional cadastrado."
        )

    def listar_profissionais(self):

        if not self.__profissionais:
            print("Nenhum profissional.")
            return

        for i, profissional in enumerate(
                self.__profissionais):

            print(
                f"{i} - "
                f"{profissional.exibir_dados()}"
            )

    def excluir_profissional(self):

        self.listar_profissionais()

        try:

            indice = int(
                input(
                    "Índice do profissional: "
                )
            )

            del self.__profissionais[indice]

            print(
                "Profissional removido."
            )

        except:

            print("Índice inválido.")

    def alterar_profissional(self):

        if not self.__profissionais:
            print("Nenhum profissional cadastrado.")
            return

        self.listar_profissionais()

        try:

            indice = int(
                input(
                    "Índice do profissional: "
                )
            )

            profissional = self.__profissionais[indice]

            novo_nome = input("Novo nome: ")
            nova_especialidade = input(
                "Nova especialidade: "
            )

            profissional._Pessoa__nome = novo_nome
            profissional._Profissional__especialidade = (
                nova_especialidade
            )

            print("Profissional alterado.")

        except:

            print("Erro na alteração.")