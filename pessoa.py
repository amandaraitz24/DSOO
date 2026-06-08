from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, celular: str, cpf: str):
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def celular(self):
        return self.__celular

    @property
    def cpf(self):
        return self.__cpf

    @abstractmethod
    def exibir_dados(self):
        pass