from datetime import date, datetime, time

from pydantic import BaseModel, ConfigDict


class UsuarioBase(BaseModel):
    nome_completo: str
    cpf: str
    vinculo_institucional: str
    perfil: str


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioSchema(UsuarioBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ProjetoBase(BaseModel):
    descricao: str
    finalidade: str
    id_responsavel: int
    quantidade_participantes: int
    documentacao_base: str


class ProjetoCreate(ProjetoBase):
    pass


class ProjetoSchema(ProjetoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ProjetoParticipanteBase(BaseModel):
    id_projeto: int
    id_usuario: int
    papel_no_projeto: str


class ProjetoParticipanteCreate(ProjetoParticipanteBase):
    pass


class ProjetoParticipanteSchema(ProjetoParticipanteBase):
    model_config = ConfigDict(from_attributes=True)


class EspacoBase(BaseModel):
    nome: str
    descricao: str
    capacidade: str
    bloco: str
    disponibilidade: bool


class EspacoCreate(EspacoBase):
    pass


class EspacoSchema(EspacoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SolicitacaoBase(BaseModel):
    tipo: str
    urgencia: bool
    status: str
    decisao_justificativa: str
    id_projeto: int
    id_solicitante: int
    id_espaco: int


class SolicitacaoCreate(SolicitacaoBase):
    pass


class SolicitacaoSchema(SolicitacaoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class RecursoBase(BaseModel):
    nome: str
    tipo: str
    autorizacao_necessaria: bool
    disponibilidade: bool
    id_espaco: int


class RecursoCreate(RecursoBase):
    pass


class RecursoSchema(RecursoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SolicitacaoHorarioBase(BaseModel):
    data_reserva: date
    hora_inicio: time
    ora_fim: time
    id_solicitacao: int


class SolicitacaoHorarioCreate(SolicitacaoHorarioBase):
    pass


class SolicitacaoHorarioSchema(SolicitacaoHorarioBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SolicitacaoRecursoBase(BaseModel):
    id_solicitacao: int
    id_recurso: int


class SolicitacaoRecursoCreate(SolicitacaoRecursoBase):
    pass


class SolicitacaoRecursoSchema(SolicitacaoRecursoBase):
    model_config = ConfigDict(from_attributes=True)


class AnexoBase(BaseModel):
    nome_arquivo: str
    url_caminho: str
    tipo_arquivo: str
    data_upload: datetime
    id_solicitacao: int


class AnexoCreate(AnexoBase):
    pass


class AnexoSchema(AnexoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class AgendaReservaBase(BaseModel):
    data_hora_inicio: datetime
    data_hora_fim: datetime
    situacao: str
    id_solicitacao: int
    id_espaco: int


class AgendaReservaCreate(AgendaReservaBase):
    pass


class AgendaReservaSchema(AgendaReservaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class AgendaReservaRecursoBase(BaseModel):
    id_agenda: int
    id_recurso: int


class AgendaReservaRecursoCreate(AgendaReservaRecursoBase):
    pass


class AgendaReservaRecursoSchema(AgendaReservaRecursoBase):
    model_config = ConfigDict(from_attributes=True)


class MonitorTurnoBase(BaseModel):
    periodo_atuacao_inicio: datetime
    periodo_atuacao_fim: datetime
    id_monitor: int


class MonitorTurnoCreate(MonitorTurnoBase):
    pass


class MonitorTurnoSchema(MonitorTurnoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
