from exceptions import (
    MenorDeIdadeException,
    HorarioInvalidoException
)


class Atendimento:
    def __init__(self,
                 clinica,
                 paciente,
                 profissional,
                 data,
                 hora_inicio,
                 hora_fim,
                 tipo_atendimento,
                 valor):

        if not paciente.maior_de_idade():
            raise MenorDeIdadeException(
                "Paciente menor de idade."
            )

        if hora_inicio < clinica.horario_abertura:
            raise HorarioInvalidoException(
                "Atendimento antes da abertura da clínica."
            )

        if hora_fim > clinica.horario_fechamento:
            raise HorarioInvalidoException(
                "Atendimento após fechamento da clínica."
            )

        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__hora_inicio = hora_inicio
        self.__hora_fim = hora_fim
        self.__tipo_atendimento = tipo_atendimento
        self.__valor = valor

        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def valor(self):
        return self.__valor

    @property
    def data(self):
        return self.__data

    @property
    def pagamentos(self):
        return self.__pagamentos

    @property
    def paciente(self):
        return self.__paciente

    @property
    def profissional(self):
        return self.__profissional

    @property
    def clinica(self):
        return self.__clinica

    @property
    def procedimentos(self):
        return self.__procedimentos

    def adicionar_procedimento(self, procedimento):
        self.__procedimentos.append(procedimento)

    def adicionar_pagamento(self, pagamento):
        self.__pagamentos.append(pagamento)

    def calcular_total_pago(self):
        total = 0

        for pagamento in self.__pagamentos:
            total += pagamento.valor_pago

        return total

    def calcular_valor_restante(self):
        return self.__valor - self.calcular_total_pago()

    def exibir_dados(self):
        return (
            f"Atendimento de {self.__paciente.nome} "
            f"com {self.__profissional.nome}"
        )