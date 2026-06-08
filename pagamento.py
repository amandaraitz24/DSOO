from abc import ABC, abstractmethod
from exceptions import PagamentoAtrasadoException


class Pagamento(ABC):
    def __init__(self, data, atendimento,
                 paciente, valor_pago):

        if data > atendimento.data:
            raise PagamentoAtrasadoException(
                "Pagamento realizado após a data do atendimento."
            )

        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago

    @property
    def valor_pago(self):
        return self.__valor_pago

    @property
    def data(self):
        return self.__data

    @property
    def paciente(self):
        return self.__paciente

    @abstractmethod
    def detalhes_pagamento(self):
        pass