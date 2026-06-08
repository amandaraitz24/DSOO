class TelaPagamento:
    def tela_opcoes(self):
        print("\n--- 💰 MÓDULO FINANCEIRO (CRUD) ---")
        print("1 - Registrar Pagamento (Incluir)")
        print("2 - Listar Pagamentos")
        print("3 - Alterar Pagamento")
        print("4 - Excluir Pagamento")
        print("0 - Voltar")
        return input("Escolha a opção: ")

    def selecionar_atendimento(self, atendimentos, mostrar_saldo=True):
        print("\n--- SELECIONE O ATENDIMENTO ---")
        for i, a in enumerate(atendimentos):
            if mostrar_saldo:
                print(f"{i} - {a.exibir_dados()} | Saldo Devedor: R$ {a.calcular_valor_restante():.2f}")
            else:
                print(f"{i} - {a.exibir_dados()}")
        return input("Digite o número do atendimento (ou 'V' para voltar): ")

    def selecionar_pagamento(self, pagamentos):
        print("\n--- PAGAMENTOS DESTE ATENDIMENTO ---")
        for i, p in enumerate(pagamentos):
            print(f"{i} - {p.detalhes_pagamento()} | Valor: R$ {p.valor_pago:.2f}")
        return input("Digite o número do pagamento a selecionar: ")

    def pegar_dados_pagamento(self):
        try:
            valor = float(input("Valor do pagamento: R$ "))
            print("\nForma de Pagamento:")
            print("1 - PIX | 2 - Cartão de Crédito | 3 - Dinheiro")
            tipo = input("Escolha (1/2/3): ")
            
            dados = {"valor": valor, "tipo": tipo}
            if tipo == '1':
                dados["cpf_pagador"] = input("CPF do titular do PIX: ")
            elif tipo == '2':
                dados["numero_cartao"] = input("Número do Cartão: ")
                dados["bandeira"] = input("Bandeira (Ex: Visa, Mastercard): ")
            
            return dados
        except ValueError:
            return None

    def mostrar_mensagem(self, msg):
        print(msg)