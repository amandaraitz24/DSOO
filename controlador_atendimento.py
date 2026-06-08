from datetime import date, time
from atendimento import Atendimento
from procedimento import Procedimento
from exceptions import MenorDeIdadeException, HorarioInvalidoException


class TelaAtendimento:
    def tela_opcoes(self):
        print("\n" + "="*40)
        print("👨‍⚕️ MÓDULO DE ATENDIMENTOS")
        print("="*40)
        print("1 - Realizar Atendimento")
        print("2 - Listar Atendimentos")
        print("3 - Adicionar Procedimento a Atendimento")
        print("4 - Adicionar Pagamento a Atendimento")
        print("5 - Visualizar Detalhes do Atendimento")
        print("0 - Voltar ao Menu Principal")
        print("="*40)
        return input("Escolha uma opção: ")

    def pegar_dados_atendimento(self):
        print("\n--- Novo Atendimento ---")
        try:
            paciente_id = input("ID do Paciente: ")
            profissional_id = input("ID do Profissional: ")
            clinica_id = input("ID da Clínica: ")
            tipo_atendimento = input("Tipo de Atendimento: ")
            
            print("Data do Atendimento (DD/MM/YYYY): ", end="")
            data_input = input()
            dia, mes, ano = map(int, data_input.split('/'))
            data = date(ano, mes, dia)
            
            print("Hora Início (HH:MM): ", end="")
            hora_input = input()
            hora, minuto = map(int, hora_input.split(':'))
            hora_inicio = time(hora, minuto)
            
            print("Hora Fim (HH:MM): ", end="")
            hora_input = input()
            hora, minuto = map(int, hora_input.split(':'))
            hora_fim = time(hora, minuto)
            
            valor = float(input("Valor do Atendimento: R$ "))
            
            return {
                "paciente_id": paciente_id,
                "profissional_id": profissional_id,
                "clinica_id": clinica_id,
                "tipo_atendimento": tipo_atendimento,
                "data": data,
                "hora_inicio": hora_inicio,
                "hora_fim": hora_fim,
                "valor": valor
            }
        except (ValueError, IndexError):
            return None

    def pegar_dados_procedimento(self):
        print("\n--- Adicionar Procedimento ---")
        descricao = input("Descrição do Procedimento: ")
        try:
            custo = float(input("Custo do Procedimento: R$ "))
            profissional_id = input("ID do Profissional Responsável: ")
            
            return {
                "descricao": descricao,
                "custo": custo,
                "profissional_id": profissional_id
            }
        except ValueError:
            return None

    def selecionar_atendimento(self):
        atendimento_id = input("\nID do Atendimento: ")
        return atendimento_id

    def mostrar_mensagem(self, msg):
        print(msg)

    def listar_atendimentos(self, atendimentos):
        if not atendimentos:
            print("\n❌ Nenhum atendimento registrado.")
            return
        
        print("\n" + "="*80)
        print("ATENDIMENTOS REGISTRADOS")
        print("="*80)
        for i, atendimento in enumerate(atendimentos):
            print(f"{i} - {atendimento.exibir_dados()}")
        print("="*80)

    def exibir_detalhes_atendimento(self, atendimento):
        print("\n" + "="*80)
        print("DETALHES DO ATENDIMENTO")
        print("="*80)
        print(f"Paciente: {atendimento.paciente.nome}")
        print(f"Profissional: {atendimento.profissional.nome}")
        print(f"Clínica: {atendimento.clinica.nome}")
        print(f"Data: {atendimento.data.strftime('%d/%m/%Y')}")
        print(f"Valor Total: R$ {atendimento.valor:.2f}")
        print(f"Total Pago: R$ {atendimento.calcular_total_pago():.2f}")
        print(f"Valor Restante: R$ {atendimento.calcular_valor_restante():.2f}")
        
        if atendimento.procedimentos:
            print("\nProcedimentos:")
            for proc in atendimento.procedimentos:
                print(f"  - {proc.exibir_dados()}")
        
        if atendimento.pagamentos:
            print("\nPagamentos:")
            for pag in atendimento.pagamentos:
                print(f"  - {pag}")
        
        print("="*80)


class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self.__atendimentos = []
        self.__tela = TelaAtendimento()
        self.__controlador_sistema = controlador_sistema

    @property
    def atendimentos(self):
        return self.__atendimentos

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()

            if opcao == '1':
                self.realizar_atendimento()

            elif opcao == '2':
                self.listar_atendimentos()

            elif opcao == '3':
                self.adicionar_procedimento()

            elif opcao == '4':
                self.adicionar_pagamento()

            elif opcao == '5':
                self.visualizar_detalhes()

            elif opcao == '0':
                break

            else:
                self.__tela.mostrar_mensagem(
                    "❌ Opção inválida!"
                )

    def realizar_atendimento(self):
        dados = self.__tela.pegar_dados_atendimento()

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
            tipo_atendimento = self.__obter_tipo_atendimento(dados["tipo_atendimento"])

            if not paciente or not profissional or not clinica:
                self.__tela.mostrar_mensagem(
                    "❌ Erro: Paciente, Profissional ou Clínica não encontrado."
                )
                return

            novo_atendimento = Atendimento(
                clinica,
                paciente,
                profissional,
                dados["data"],
                dados["hora_inicio"],
                dados["hora_fim"],
                tipo_atendimento,
                dados["valor"]
            )

            self.__atendimentos.append(novo_atendimento)
            self.__tela.mostrar_mensagem(
                "\n✅ Atendimento registrado com sucesso!"
            )

        except MenorDeIdadeException as e:
            self.__tela.mostrar_mensagem(f"\n❌ Erro: {e}")
        except HorarioInvalidoException as e:
            self.__tela.mostrar_mensagem(f"\n❌ Erro: {e}")
        except Exception as e:
            self.__tela.mostrar_mensagem(f"\n❌ Erro inesperado: {e}")

    def listar_atendimentos(self):
        if not self.__atendimentos:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum atendimento registrado."
            )
            return

        print("\n" + "="*80)
        print("ATENDIMENTOS REGISTRADOS")
        print("="*80)

        for i, atendimento in enumerate(self.__atendimentos):
            print(f"{i} - {atendimento.exibir_dados()}")
            print(f"   Data: {atendimento.data.strftime('%d/%m/%Y')} | "
                  f"Valor: R$ {atendimento.valor:.2f} | "
                  f"Pago: R$ {atendimento.calcular_total_pago():.2f}")

        print("="*80)

    def adicionar_procedimento(self):
        if not self.__atendimentos:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum atendimento registrado."
            )
            return

        self.listar_atendimentos()

        try:
            atendimento_id = int(self.__tela.selecionar_atendimento())

            if atendimento_id < 0 or atendimento_id >= len(self.__atendimentos):
                self.__tela.mostrar_mensagem(
                    "❌ Atendimento não encontrado."
                )
                return

            dados = self.__tela.pegar_dados_procedimento()

            if not dados:
                self.__tela.mostrar_mensagem(
                    "❌ Erro: Dados inválidos."
                )
                return

            profissional = self.__obter_profissional(dados["profissional_id"])

            if not profissional:
                profissional = self.__controlador_sistema.profissional_padrao

            procedimento = Procedimento(
                dados["descricao"],
                dados["custo"],
                profissional
            )

            atendimento = self.__atendimentos[atendimento_id]
            atendimento.adicionar_procedimento(procedimento)

            self.__tela.mostrar_mensagem(
                "\n✅ Procedimento adicionado ao atendimento!"
            )

        except ValueError:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Digite um número válido."
            )

    def adicionar_pagamento(self):
        if not self.__atendimentos:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum atendimento registrado."
            )
            return

        self.listar_atendimentos()

        try:
            atendimento_id = int(self.__tela.selecionar_atendimento())

            if atendimento_id < 0 or atendimento_id >= len(self.__atendimentos):
                self.__tela.mostrar_mensagem(
                    "❌ Atendimento não encontrado."
                )
                return

            atendimento = self.__atendimentos[atendimento_id]

            # Delegar para o controlador de pagamento
            self.__controlador_sistema.controlador_pagamento.adicionar_pagamento_atendimento(
                atendimento
            )

        except ValueError:
            self.__tela.mostrar_mensagem(
                "❌ Erro: Digite um número válido."
            )

    def visualizar_detalhes(self):
        if not self.__atendimentos:
            self.__tela.mostrar_mensagem(
                "\n❌ Nenhum atendimento registrado."
            )
            return

        self.listar_atendimentos()

        try:
            atendimento_id = int(self.__tela.selecionar_atendimento())

            if atendimento_id < 0 or atendimento_id >= len(self.__atendimentos):
                self.__tela.mostrar_mensagem(
                    "❌ Atendimento não encontrado."
                )
                return

            atendimento = self.__atendimentos[atendimento_id]
            self.__tela.exibir_detalhes_atendimento(atendimento)

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

    def __obter_tipo_atendimento(self, tipo_id):
        try:
            idx = int(tipo_id)
            # Aqui você pode buscar tipos de atendimento se tiver uma lista
            return self.__controlador_sistema.tipo_padrao
        except (ValueError, IndexError):
            pass
        return self.__controlador_sistema.tipo_padrao
