from datetime import datetime
from exceptions import HorarioInvalidoException


class Agendamento:
    def __init__(self, paciente, profissional, clinica, 
                 data_agendamento, hora_agendamento, tipo_atendimento):
        
        if hora_agendamento < clinica.horario_abertura:
            raise HorarioInvalidoException(
                "Agendamento antes da abertura da clínica."
            )
        
        if hora_agendamento > clinica.horario_fechamento:
            raise HorarioInvalidoException(
                "Agendamento após fechamento da clínica."
            )
        
        self.__paciente = paciente
        self.__profissional = profissional
        self.__clinica = clinica
        self.__data_agendamento = data_agendamento
        self.__hora_agendamento = hora_agendamento
        self.__tipo_atendimento = tipo_atendimento
        self.__status = "Agendado"
        self.__data_criacao = datetime.now()
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
    def data_agendamento(self):
        return self.__data_agendamento

    @property
    def hora_agendamento(self):
        return self.__hora_agendamento

    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    @property
    def status(self):
        return self.__status

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

    def marcar_como_realizado(self):
        self.__status = "Realizado"

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
            f"Agendamento: {self.__paciente.nome} com "
            f"{self.__profissional.nome} | "
            f"Data: {self.__data_agendamento.strftime('%d/%m/%Y')} às "
            f"{self.__hora_agendamento.strftime('%H:%M')} | "
            f"Status: {self.__status}"
        )
