from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from contrato.schemas import (
    AgendaReservaRecursoCreate,
    AgendaReservaRecursoSchema,
    AgendaReservaCreate,
    AgendaReservaSchema,
    AnexoCreate,
    AnexoSchema,
    EspacoCreate,
    EspacoSchema,
    ProjetoCreate,
    ProjetoParticipanteCreate,
    ProjetoParticipanteSchema,
    ProjetoSchema,
    RecursoCreate,
    RecursoSchema,
    SolicitacaoCreate,
    SolicitacaoHorarioCreate,
    SolicitacaoHorarioSchema,
    SolicitacaoRecursoCreate,
    SolicitacaoRecursoSchema,
    SolicitacaoSchema,
    MonitorTurnoCreate,
    MonitorTurnoSchema,
    UsuarioCreate,
    UsuarioSchema,
)
from models.database import get_db
from models.models import (
    AgendaReserva,
    AgendaReservaRecurso,
    Anexo,
    Espaco,
    MonitorTurno,
    Projeto,
    ProjetoParticipante,
    Recurso,
    Solicitacao,
    SolicitacaoHorario,
    SolicitacaoRecurso,
    Usuario,
)


router = APIRouter(
    prefix="/API/V1",
    tags=["Agendamento"],
)


@router.get("/usuarios", response_model=list[UsuarioSchema])
def get_usuarios(session: Session = Depends(get_db)):
    return session.query(Usuario).all()


@router.post(
    "/usuarios",
    response_model=UsuarioSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_usuario(dados: UsuarioCreate, session: Session = Depends(get_db)):
    usuario = Usuario(**dados.model_dump())
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


@router.get("/projetos", response_model=list[ProjetoSchema])
def get_projetos(session: Session = Depends(get_db)):
    return session.query(Projeto).all()


@router.post(
    "/projetos",
    response_model=ProjetoSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_projeto(dados: ProjetoCreate, session: Session = Depends(get_db)):
    projeto = Projeto(**dados.model_dump())
    session.add(projeto)
    session.commit()
    session.refresh(projeto)
    return projeto


@router.get(
    "/projeto-participantes",
    response_model=list[ProjetoParticipanteSchema],
)
def get_projeto_participantes(session: Session = Depends(get_db)):
    return session.query(ProjetoParticipante).all()


@router.post(
    "/projeto-participantes",
    response_model=ProjetoParticipanteSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_projeto_participante(
    dados: ProjetoParticipanteCreate,
    session: Session = Depends(get_db),
):
    participante = ProjetoParticipante(**dados.model_dump())
    session.add(participante)
    session.commit()
    session.refresh(participante)
    return participante


@router.get("/espacos", response_model=list[EspacoSchema])
def get_espacos(session: Session = Depends(get_db)):
    return session.query(Espaco).all()


@router.post(
    "/espacos",
    response_model=EspacoSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_espaco(dados: EspacoCreate, session: Session = Depends(get_db)):
    espaco = Espaco(**dados.model_dump())
    session.add(espaco)
    session.commit()
    session.refresh(espaco)
    return espaco


@router.get("/recursos", response_model=list[RecursoSchema])
def get_recursos(session: Session = Depends(get_db)):
    return session.query(Recurso).all()


@router.post(
    "/recursos",
    response_model=RecursoSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_recurso(dados: RecursoCreate, session: Session = Depends(get_db)):
    recurso = Recurso(**dados.model_dump())
    session.add(recurso)
    session.commit()
    session.refresh(recurso)
    return recurso


@router.get("/espacos/{espaco_id}", response_model=EspacoSchema)
def get_espaco(espaco_id: int, session: Session = Depends(get_db)):
    espaco = session.get(Espaco, espaco_id)
    if espaco is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Espaço não encontrado",
        )
    return espaco


@router.get("/solicitacoes", response_model=list[SolicitacaoSchema])
def get_solicitacoes(session: Session = Depends(get_db)):
    return session.query(Solicitacao).all()


@router.post(
    "/solicitacoes",
    response_model=SolicitacaoSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_solicitacao(
    dados: SolicitacaoCreate,
    session: Session = Depends(get_db),
):
    solicitacao = Solicitacao(**dados.model_dump())
    session.add(solicitacao)
    session.commit()
    session.refresh(solicitacao)
    return solicitacao


@router.get(
    "/solicitacao-horarios",
    response_model=list[SolicitacaoHorarioSchema],
)
def get_solicitacao_horarios(session: Session = Depends(get_db)):
    return session.query(SolicitacaoHorario).all()


@router.post(
    "/solicitacao-horarios",
    response_model=SolicitacaoHorarioSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_solicitacao_horario(
    dados: SolicitacaoHorarioCreate,
    session: Session = Depends(get_db),
):
    horario = SolicitacaoHorario(**dados.model_dump())
    session.add(horario)
    session.commit()
    session.refresh(horario)
    return horario


@router.get(
    "/solicitacao-recursos",
    response_model=list[SolicitacaoRecursoSchema],
)
def get_solicitacao_recursos(session: Session = Depends(get_db)):
    return session.query(SolicitacaoRecurso).all()


@router.post(
    "/solicitacao-recursos",
    response_model=SolicitacaoRecursoSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_solicitacao_recurso(
    dados: SolicitacaoRecursoCreate,
    session: Session = Depends(get_db),
):
    item = SolicitacaoRecurso(**dados.model_dump())
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("/anexos", response_model=list[AnexoSchema])
def get_anexos(session: Session = Depends(get_db)):
    return session.query(Anexo).all()


@router.post(
    "/anexos",
    response_model=AnexoSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_anexo(dados: AnexoCreate, session: Session = Depends(get_db)):
    anexo = Anexo(**dados.model_dump())
    session.add(anexo)
    session.commit()
    session.refresh(anexo)
    return anexo


@router.get("/agenda-reservas", response_model=list[AgendaReservaSchema])
def get_agenda_reservas(session: Session = Depends(get_db)):
    return session.query(AgendaReserva).all()


@router.post(
    "/agenda-reservas",
    response_model=AgendaReservaSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_agenda_reserva(
    dados: AgendaReservaCreate,
    session: Session = Depends(get_db),
):
    reserva = AgendaReserva(**dados.model_dump())
    session.add(reserva)
    session.commit()
    session.refresh(reserva)
    return reserva


@router.get(
    "/agenda-reserva-recursos",
    response_model=list[AgendaReservaRecursoSchema],
)
def get_agenda_reserva_recursos(session: Session = Depends(get_db)):
    return session.query(AgendaReservaRecurso).all()


@router.post(
    "/agenda-reserva-recursos",
    response_model=AgendaReservaRecursoSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_agenda_reserva_recurso(
    dados: AgendaReservaRecursoCreate,
    session: Session = Depends(get_db),
):
    item = AgendaReservaRecurso(**dados.model_dump())
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("/monitor-turnos", response_model=list[MonitorTurnoSchema])
def get_monitor_turnos(session: Session = Depends(get_db)):
    return session.query(MonitorTurno).all()


@router.post(
    "/monitor-turnos",
    response_model=MonitorTurnoSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_monitor_turno(
    dados: MonitorTurnoCreate,
    session: Session = Depends(get_db),
):
    turno = MonitorTurno(**dados.model_dump())
    session.add(turno)
    session.commit()
    session.refresh(turno)
    return turno
