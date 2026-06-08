from datetime import date
from tela_pagamento import TelaPagamento
from pagamento_pix import PagamentoPix
from pagamento_cartao import PagamentoCartao
# Descomente a linha abaixo se o arquivo pagamento_dinheiro estiver na pasta
# from pagamento_dinheiro import PagamentoDinheiro
from exceptions import PagamentoAtrasadoException

class ControladorPagamento:
    def __init__(self, controlador_sistema):
        self.__tela = TelaPagamento()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao == '1':
                self.incluir_pagamento()
            elif opcao == '2':
                self.listar_pagamentos()
            elif opcao == '3':
                self.alterar_pagamento()
            elif opcao == '4':
                self.excluir_pagamento()
            elif opcao == '0':
                break
            else:
                self.__tela.mostrar_mensagem("❌ Opção inválida!")

    def incluir_pagamento(self):
        # Acessa a lista de atendimentos pelo controlador principal
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if not atendimentos:
            self.__tela.mostrar_mensagem("⚠️ Nenhum atendimento agendado no sistema.")
            return

        id_str = self.__tela.selecionar_atendimento(atendimentos, mostrar_saldo=True)
        if id_str.upper() == 'V': return

        try:
            atendimento = atendimentos[int(id_str)]
            if atendimento.calcular_valor_restante() <= 0:
                self.__tela.mostrar_mensagem("✅ O saldo deste atendimento já está quitado.")
                return

            dados = self.__tela.pegar_dados_pagamento()
            if not dados:
                self.__tela.mostrar_mensagem("❌ Erro nos dados digitados.")
                return
            
            pagamento = self._criar_objeto_pagamento(dados, atendimento)
            if pagamento:
                atendimento.adicionar_pagamento(pagamento)
                self.__tela.mostrar_mensagem("✅ Pagamento registrado com sucesso!")
        except (ValueError, IndexError):
            self.__tela.mostrar_mensagem("❌ Atendimento inválido.")
        except PagamentoAtrasadoException as e:
            self.__tela.mostrar_mensagem(f"⛔ REGRA DE NEGÓCIO: {e}")

    def adicionar_pagamento_atendimento(self, atendimento):
        """Registrar um pagamento para o atendimento já selecionado pela camada chamadora."""
        try:
            if atendimento.calcular_valor_restante() <= 0:
                self.__tela.mostrar_mensagem("✅ O saldo deste atendimento já está quitado.")
                return

            dados = self.__tela.pegar_dados_pagamento()
            if not dados:
                self.__tela.mostrar_mensagem("❌ Erro nos dados digitados.")
                return

            pagamento = self._criar_objeto_pagamento(dados, atendimento)
            if pagamento:
                atendimento.adicionar_pagamento(pagamento)
                self.__tela.mostrar_mensagem("✅ Pagamento registrado com sucesso!")

        except PagamentoAtrasadoException as e:
            self.__tela.mostrar_mensagem(f"⛔ REGRA DE NEGÓCIO: {e}")
        except Exception:
            self.__tela.mostrar_mensagem("❌ Erro ao registrar pagamento.")

    def listar_pagamentos(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if not atendimentos:
            self.__tela.mostrar_mensagem("⚠️ Nenhum atendimento no sistema.")
            return

        for a in atendimentos:
            if a.pagamentos:
                self.__tela.mostrar_mensagem(f"\n--- Pagamentos de: {a.exibir_dados()} ---")
                for p in a.pagamentos:
                    self.__tela.mostrar_mensagem(f"- {p.detalhes_pagamento()} | Valor: R$ {p.valor_pago:.2f}")

    def alterar_pagamento(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if not atendimentos: return

        id_str = self.__tela.selecionar_atendimento(atendimentos, mostrar_saldo=False)
        if id_str.upper() == 'V': return

        try:
            atendimento = atendimentos[int(id_str)]
            if not atendimento.pagamentos:
                self.__tela.mostrar_mensagem("⚠️ Este atendimento ainda não possui pagamentos.")
                return

            id_pag = int(self.__tela.selecionar_pagamento(atendimento.pagamentos))
            
            self.__tela.mostrar_mensagem("\n[ Insira os NOVOS dados para este pagamento ]")
            dados = self.__tela.pegar_dados_pagamento()
            if not dados: return

            novo_pagamento = self._criar_objeto_pagamento(dados, atendimento)
            if novo_pagamento:
                atendimento.pagamentos[id_pag] = novo_pagamento
                self.__tela.mostrar_mensagem("✅ Pagamento alterado com sucesso!")

        except (ValueError, IndexError):
            self.__tela.mostrar_mensagem("❌ Seleção inválida.")
        except PagamentoAtrasadoException as e:
            self.__tela.mostrar_mensagem(f"⛔ REGRA DE NEGÓCIO: {e}")

    def excluir_pagamento(self):
        atendimentos = self.__controlador_sistema.controlador_atendimento.atendimentos
        if not atendimentos: return

        id_str = self.__tela.selecionar_atendimento(atendimentos, mostrar_saldo=False)
        if id_str.upper() == 'V': return

        try:
            atendimento = atendimentos[int(id_str)]
            if not atendimento.pagamentos:
                self.__tela.mostrar_mensagem("⚠️ Este atendimento não tem pagamentos para excluir.")
                return

            id_pag = int(self.__tela.selecionar_pagamento(atendimento.pagamentos))
            pagamento_removido = atendimento.pagamentos.pop(id_pag)
            self.__tela.mostrar_mensagem(f"✅ Pagamento de R$ {pagamento_removido.valor_pago:.2f} foi excluído!")
        except (ValueError, IndexError):
            self.__tela.mostrar_mensagem("❌ Seleção inválida.")

    def _criar_objeto_pagamento(self, dados, atendimento):
        hoje = date.today()
        if dados["tipo"] == '1':
            return PagamentoPix(hoje, atendimento, atendimento.paciente, dados["valor"], dados["cpf_pagador"])
        elif dados["tipo"] == '2':
            return PagamentoCartao(hoje, atendimento, atendimento.paciente, dados["valor"], dados["numero_cartao"], dados["bandeira"])
        elif dados["tipo"] == '3':
            # return PagamentoDinheiro(hoje, atendimento, atendimento.paciente, dados["valor"])
            pass
        self.__tela.mostrar_mensagem("❌ Tipo de pagamento inválido.")
        return None