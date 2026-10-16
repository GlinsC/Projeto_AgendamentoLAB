from datetime import datetime
from typing import Optional



from pydantic import BaseModel, ConfigDict, Field


class AgendamentoBase(BaseModel):
    data_agendamento: datetime
    horario_inicio: datetime
    horario_fim: datetime
    finalidade: str = Field(max_length=100)
    descricao: Optional[str] = None
    quantidade_participantes: int
    status: bool = True
    motivo_recusa: Optional[str] = None
    laboratorio_id: int = None


class AgendamentoCreate(AgendamentoBase):
    pass


class AgendamentoUpdate(BaseModel):
    data_agendamento: Optional[datetime] = None
    horario_inicio: Optional[datetime] = None
    horario_fim: Optional[datetime] = None
    finalidade: Optional[str] = Field(default=None, max_length=100)
    descricao: Optional[str] = None
    quantidade_participantes: Optional[int] = None
    status: Optional[bool] = None
    motivo_recusa: Optional[str] = None
    laboratorio_id: int = None


class AgendamentoSchema(AgendamentoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class LaboratorioBase(BaseModel):
    nome_laboratorio: str = Field(max_length=100)
    descricao: Optional[str] = None
    bloco: str = Field(max_length=50)
    sala: str = Field(max_length=50)
    capacidade: int
    status: bool = True
    tipo_uso: str = Field(max_length=50)
    equipamentos: Optional[str] = None
    cor_card: Optional[str] = Field(default=None, max_length=20)


class LaboratorioCreate(LaboratorioBase):
    pass


class LaboratorioUpdate(BaseModel):
    nome_laboratorio: Optional[str] = Field(default=None, max_length=100)
    descricao: Optional[str] = None
    bloco: Optional[str] = Field(default=None, max_length=50)
    sala: Optional[str] = Field(default=None, max_length=50)
    capacidade: Optional[int] = None
    status: Optional[bool] = None
    tipo_uso: Optional[str] = Field(default=None, max_length=50)
    equipamentos: Optional[str] = None
    cor_card: Optional[str] = Field(default=None, max_length=20)


class LaboratorioSchema(LaboratorioBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class AnexosAgendamentoBase(BaseModel):
    nome_arquivo: str = Field(max_length=100)
    caminho_storage: str = Field(max_length=200)
    agendamento_id: int


class AnexosAgendamentoCreate(AnexosAgendamentoBase):
    pass


class AnexosAgendamentoUpdate(BaseModel):
    nome_arquivo: Optional[str] = Field(default=None, max_length=100)
    caminho_storage: Optional[str] = Field(default=None, max_length=200)
    agendamento_id: Optional[int] = None


class AnexosAgendamentoSchema(AnexosAgendamentoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
