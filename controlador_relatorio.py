from collections import Counter


class ControladorRelatorio:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def menu_relatorios(self):

        while True:

            print("\n===== RELATÓRIOS =====")
            print("1 - Clínica com maior número de atendimentos")
            print("2 - Atendimento mais caro e mais barato")
            print("3 - Procedimento mais realizado")
            print("4 - Procedimento mais caro e mais barato")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.relatorio_clinica()

            elif opcao == "2":
                self.relatorio_atendimentos()

            elif opcao == "3":
                self.relatorio_procedimento_popular()

            elif opcao == "4":
                self.relatorio_procedimento_custos()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

    def relatorio_clinica(self):

        atendimentos = (
            self.__controlador_sistema
            .controlador_atendimento
            .atendimentos
        )

        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        contador = {}

        for atendimento in atendimentos:

            nome = atendimento.clinica.nome

            if nome not in contador:
                contador[nome] = 0

            contador[nome] += 1

        maior = max(
            contador,
            key=contador.get
        )

        print("\n=== CLÍNICA COM MAIS ATENDIMENTOS ===")
        print(
            f"{maior} "
            f"({contador[maior]} atendimentos)"
        )

    def relatorio_atendimentos(self):

        atendimentos = (
            self.__controlador_sistema
            .controlador_atendimento
            .atendimentos
        )

        if not atendimentos:
            print("Nenhum atendimento cadastrado.")
            return

        mais_caro = max(
            atendimentos,
            key=lambda a: a.valor
        )

        mais_barato = min(
            atendimentos,
            key=lambda a: a.valor
        )

        print("\n=== RELATÓRIO DE ATENDIMENTOS ===")

        print(
            f"Mais caro: "
            f"R$ {mais_caro.valor:.2f}"
        )

        print(
            f"Mais barato: "
            f"R$ {mais_barato.valor:.2f}"
        )

    def relatorio_procedimento_popular(self):

        atendimentos = (
            self.__controlador_sistema
            .controlador_atendimento
            .atendimentos
        )

        procedimentos = []

        for atendimento in atendimentos:

            for procedimento in atendimento.procedimentos:

                procedimentos.append(
                    procedimento.descricao
                )

        if not procedimentos:
            print("Nenhum procedimento cadastrado.")
            return

        contador = Counter(
            procedimentos
        )

        nome, quantidade = (
            contador.most_common(1)[0]
        )

        print(
            "\n=== PROCEDIMENTO MAIS REALIZADO ==="
        )

        print(
            f"{nome} "
            f"({quantidade} vezes)"
        )

    def relatorio_procedimento_custos(self):

        atendimentos = (
            self.__controlador_sistema
            .controlador_atendimento
            .atendimentos
        )

        lista = []

        for atendimento in atendimentos:

            for procedimento in atendimento.procedimentos:

                lista.append(
                    procedimento
                )

        if not lista:
            print("Nenhum procedimento cadastrado.")
            return

        mais_caro = max(
            lista,
            key=lambda p: p.custo
        )

        mais_barato = min(
            lista,
            key=lambda p: p.custo
        )

        print(
            "\n=== PROCEDIMENTOS ==="
        )

        print(
            f"Mais caro: "
            f"{mais_caro.descricao} "
            f"(R$ {mais_caro.custo:.2f})"
        )

        print(
            f"Mais barato: "
            f"{mais_barato.descricao} "
            f"(R$ {mais_barato.custo:.2f})"
        )
