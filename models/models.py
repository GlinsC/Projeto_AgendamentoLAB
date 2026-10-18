from datetime import date, datetime, time

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome_completo: Mapped[str] = mapped_column(String, nullable=False)
    cpf: Mapped[str] = mapped_column(String, nullable=False)
    vinculo_institucional: Mapped[str] = mapped_column(String, nullable=False)
    perfil: Mapped[str] = mapped_column(String, nullable=False)

    projetos_responsavel: Mapped[list["Projeto"]] = relationship(
        back_populates="responsavel"
    )
    participacoes: Mapped[list["ProjetoParticipante"]] = relationship(
        back_populates="usuario"
    )
    solicitacoes: Mapped[list["Solicitacao"]] = relationship(
        back_populates="solicitante"
    )
    turnos_monitor: Mapped[list["MonitorTurno"]] = relationship(
        back_populates="monitor"
    )


class Projeto(Base):
    __tablename__ = "projeto"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    descricao: Mapped[str] = mapped_column(String, nullable=False)
    finalidade: Mapped[str] = mapped_column(String, nullable=False)
    id_responsavel: Mapped[int] = mapped_column(
        ForeignKey("usuario.id"), nullable=False
    )
    quantidade_participantes: Mapped[int] = mapped_column(Integer, nullable=False)
    documentacao_base: Mapped[str] = mapped_column(String, nullable=False)

    responsavel: Mapped["Usuario"] = relationship(back_populates="projetos_responsavel")
    participantes: Mapped[list["ProjetoParticipante"]] = relationship(
        back_populates="projeto"
    )
    solicitacoes: Mapped[list["Solicitacao"]] = relationship(
        back_populates="projeto"
    )


class ProjetoParticipante(Base):
    __tablename__ = "projeto_participante"

    id_projeto: Mapped[int] = mapped_column(
        ForeignKey("projeto.id"), primary_key=True
    )
    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuario.id"), primary_key=True
    )
    papel_no_projeto: Mapped[str] = mapped_column(String, nullable=False)

    projeto: Mapped["Projeto"] = relationship(back_populates="participantes")
    usuario: Mapped["Usuario"] = relationship(back_populates="participacoes")


class Espaco(Base):
    __tablename__ = "espaco"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    descricao: Mapped[str] = mapped_column(String, nullable=False)
    capacidade: Mapped[str] = mapped_column(String, nullable=False)
    bloco: Mapped[str] = mapped_column(String, nullable=False)
    disponibilidade: Mapped[bool] = mapped_column(Boolean, nullable=False)

    recursos: Mapped[list["Recurso"]] = relationship(back_populates="espaco")
    solicitacoes: Mapped[list["Solicitacao"]] = relationship(
        back_populates="espaco"
    )
    reservas: Mapped[list["AgendaReserva"]] = relationship(back_populates="espaco")


class Recurso(Base):
    __tablename__ = "recurso"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    tipo: Mapped[str] = mapped_column(String, nullable=False)
    autorizacao_necessaria: Mapped[bool] = mapped_column(Boolean, nullable=False)
    disponibilidade: Mapped[bool] = mapped_column(Boolean, nullable=False)
    id_espaco: Mapped[int] = mapped_column(ForeignKey("espaco.id"), nullable=False)

    espaco: Mapped["Espaco"] = relationship(back_populates="recursos")
    solicitacoes: Mapped[list["SolicitacaoRecurso"]] = relationship(
        back_populates="recurso"
    )
    reservas: Mapped[list["AgendaReservaRecurso"]] = relationship(
        back_populates="recurso"
    )


class Solicitacao(Base):
    __tablename__ = "solicitacao"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    tipo: Mapped[str] = mapped_column(String, nullable=False)
    urgencia: Mapped[bool] = mapped_column(Boolean, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    decisao_justificativa: Mapped[str] = mapped_column(String, nullable=False)
    id_projeto: Mapped[int] = mapped_column(ForeignKey("projeto.id"), nullable=False)
    id_solicitante: Mapped[int] = mapped_column(
        ForeignKey("usuario.id"), nullable=False
    )
    id_espaco: Mapped[int] = mapped_column(ForeignKey("espaco.id"), nullable=False)

    projeto: Mapped["Projeto"] = relationship(back_populates="solicitacoes")
    solicitante: Mapped["Usuario"] = relationship(back_populates="solicitacoes")
    espaco: Mapped["Espaco"] = relationship(back_populates="solicitacoes")
    horarios: Mapped[list["SolicitacaoHorario"]] = relationship(
        back_populates="solicitacao"
    )
    recursos: Mapped[list["SolicitacaoRecurso"]] = relationship(
        back_populates="solicitacao"
    )
    anexos: Mapped[list["Anexo"]] = relationship(back_populates="solicitacao")
    reservas: Mapped[list["AgendaReserva"]] = relationship(
        back_populates="solicitacao"
    )


class SolicitacaoHorario(Base):
    __tablename__ = "solicitacao_horario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    data_reserva: Mapped[date] = mapped_column(Date, nullable=False)
    hora_inicio: Mapped[time] = mapped_column(Time, nullable=False)
    ora_fim: Mapped[time] = mapped_column(Time, nullable=False)
    id_solicitacao: Mapped[int] = mapped_column(
        ForeignKey("solicitacao.id"), nullable=False
    )

    solicitacao: Mapped["Solicitacao"] = relationship(back_populates="horarios")


class SolicitacaoRecurso(Base):
    __tablename__ = "solicitacao_recurso"

    id_solicitacao: Mapped[int] = mapped_column(
        ForeignKey("solicitacao.id"), primary_key=True
    )
    id_recurso: Mapped[int] = mapped_column(
        ForeignKey("recurso.id"), primary_key=True
    )

    solicitacao: Mapped["Solicitacao"] = relationship(back_populates="recursos")
    recurso: Mapped["Recurso"] = relationship(back_populates="solicitacoes")


class Anexo(Base):
    __tablename__ = "anexo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome_arquivo: Mapped[str] = mapped_column(String, nullable=False)
    url_caminho: Mapped[str] = mapped_column(String, nullable=False)
    tipo_arquivo: Mapped[str] = mapped_column(String, nullable=False)
    data_upload: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    id_solicitacao: Mapped[int] = mapped_column(
        ForeignKey("solicitacao.id"), nullable=False
    )

    solicitacao: Mapped["Solicitacao"] = relationship(back_populates="anexos")


class AgendaReserva(Base):
    __tablename__ = "agenda_reserva"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    data_hora_inicio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    data_hora_fim: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    situacao: Mapped[str] = mapped_column(String, nullable=False)
    id_solicitacao: Mapped[int] = mapped_column(
        ForeignKey("solicitacao.id"), nullable=False
    )
    id_espaco: Mapped[int] = mapped_column(ForeignKey("espaco.id"), nullable=False)

    solicitacao: Mapped["Solicitacao"] = relationship(back_populates="reservas")
    espaco: Mapped["Espaco"] = relationship(back_populates="reservas")
    recursos: Mapped[list["AgendaReservaRecurso"]] = relationship(
        back_populates="agenda"
    )


class AgendaReservaRecurso(Base):
    __tablename__ = "agenda_reserva_recurso"

    id_agenda: Mapped[int] = mapped_column(
        ForeignKey("agenda_reserva.id"), primary_key=True
    )
    id_recurso: Mapped[int] = mapped_column(
        ForeignKey("recurso.id"), primary_key=True
    )

    agenda: Mapped["AgendaReserva"] = relationship(back_populates="recursos")
    recurso: Mapped["Recurso"] = relationship(back_populates="reservas")


class MonitorTurno(Base):
    __tablename__ = "monitor_turno"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    periodo_atuacao_inicio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    periodo_atuacao_fim: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    id_monitor: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)

    monitor: Mapped["Usuario"] = relationship(back_populates="turnos_monitor")
