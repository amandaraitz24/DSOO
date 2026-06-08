from datetime import datetime
from exceptions import HorarioInvalidoException


class Exame:
    def __init__(self, paciente, profissional, clinica,
                 tipo_exame, data_agendamento, hora_agendamento):
        
        if hora_agendamento < clinica.horario_abertura:
            raise HorarioInvalidoException(
                "Exame antes da abertura da clínica."
            )
        
        if hora_agendamento > clinica.horario_fechamento:
            raise HorarioInvalidoException(
                "Exame após fechamento da clínica."
            )
        
        self.__paciente = paciente
        self.__profissional = profissional
        self.__clinica = clinica
        self.__tipo_exame = tipo_exame
        self.__data_agendamento = data_agendamento
        self.__hora_agendamento = hora_agendamento
        self.__status = "Agendado"
        self.__data_criacao = datetime.now()
        self.__data_realizacao = None
        self.__resultado = ""
        self.__observacoes = ""

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
    def tipo_exame(self):
        return self.__tipo_exame

    @property
    def data_agendamento(self):
        return self.__data_agendamento

    @property
    def hora_agendamento(self):
        return self.__hora_agendamento

    @property
    def status(self):
        return self.__status

    @property
    def resultado(self):
        return self.__resultado

    @resultado.setter
    def resultado(self, resultado):
        self.__resultado = resultado

    @property
    def observacoes(self):
        return self.__observacoes

    @observacoes.setter
    def observacoes(self, observacoes):
        self.__observacoes = observacoes

    def confirmar(self):
        self.__status = "Confirmado"

    def cancelar(self):
        self.__status = "Cancelado"

    def realizar_exame(self, resultado):
        self.__status = "Realizado"
        self.__data_realizacao = datetime.now()
        self.__resultado = resultado

    def remarcar(self, nova_data, nova_hora):
        if nova_hora < self.__clinica.horario_abertura:
            raise HorarioInvalidoException(
                "Novo horário antes da abertura da clínica."
            )
        
        if nova_hora > self.__clinica.horario_fechamento:
            raise HorarioInvalidoException(
                "Novo horário após fechamento da clínica."
            )
        
        self.__data_agendamento = nova_data
        self.__hora_agendamento = nova_hora
        self.__status = "Remarcado"

    def exibir_dados(self):
        return (
            f"Exame: {self.__tipo_exame} | "
            f"Paciente: {self.__paciente.nome} | "
            f"Data: {self.__data_agendamento.strftime('%d/%m/%Y')} às "
            f"{self.__hora_agendamento.strftime('%H:%M')} | "
            f"Status: {self.__status}"
        )
