from sqlalchemy import  ForeignKey, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    data_agendamento = Column(DateTime, nullable=False)
    horario_inicio = Column(DateTime, nullable=False)
    horario_fim = Column(DateTime, nullable=False)
    finalidade = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=True)
    quantidade_participantes = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    motivo_recusa = Column(Text, nullable=True)

    laboratorio_id: Mapped[int] = mapped_column(
        ForeignKey("laboratorio.id")
    )


class laboratorio(Base):
    __tablename__ = "laboratorio"

    id = Column(Integer, primary_key=True, index=True)
    nome_laboratorio = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=True)
    bloco = Column(String(50), nullable=False)
    sala = Column(String(50), nullable=False)
    capacidade = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    tipo_uso = Column(String(50), nullable=False)
    equipamentos = Column(Text, nullable=True)
    cor_card = Column(String(20), nullable=True)

class AnexosAgendamento(Base):
    __tablename__ = "anexos_agendamento"

    id = Column(Integer, primary_key=True, index=True)
    nome_arquivo = Column(String(100), nullable=False)
    caminho_storage = Column(String(200), nullable=False)

    agendamento_id: Mapped[int] = mapped_column(
        ForeignKey("agendamentos.id")
    )
