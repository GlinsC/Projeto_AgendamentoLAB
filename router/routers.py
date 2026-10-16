from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Agendamento.contrato.schemas import AgendamentoBase, AgendamentoSchema, AgendamentoCreate, AgendamentoUpdate, LaboratorioSchema, LaboratorioCreate, LaboratorioUpdate, AnexosAgendamentoSchema, AnexosAgendamentoCreate, AnexosAgendamentoUpdate
from Agendamento.models.database import get_db
from Agendamento.models.models import Agendamento as AgendamentoModel, laboratorio as LaboratorioModel, AnexosAgendamento



router = APIRouter(
    prefix="/API/V1",
    tags=["Agendamento"],
)

###Rotas para Agendamento

@router.get("/agendamentos", response_model=list[AgendamentoSchema])
async def get_agendamentos(session: Session = Depends(get_db)):
    # Lógica para obter todos os agendamentos
    agendamentos = session.query(AgendamentoModel).all()
    return agendamentos

@router.post("/agendamentos", response_model=AgendamentoSchema, status_code=status.HTTP_201_CREATED)
async def create_agendamento(agendamento: AgendamentoBase, session: Session = Depends(get_db)):
    # Lógica para criar um novo agendamento
    agendamento = AgendamentoModel(**agendamento.model_dump())
    session.add(agendamento)
    session.commit()
    session.refresh(agendamento)
    return agendamento


##Rotas para Laboratorio

@router.post("/laboratorios", response_model=LaboratorioSchema, status_code=status.HTTP_201_CREATED)
async def create_laboratorio(dados_laboratorio: LaboratorioCreate, session: Session = Depends(get_db)):
    # Lógica para criar um novo laboratório
    laboratorio = LaboratorioModel(**dados_laboratorio.model_dump())
    session.add(laboratorio)
    session.commit()
    session.refresh(laboratorio)
    return laboratorio

@router.get("/laboratorios", response_model=list[LaboratorioSchema])
async def get_laboratorios(session: Session = Depends(get_db)):
    # Lógica para obter todos os laboratórios
    laboratorios = session.query(LaboratorioModel).all()
    return laboratorios

@router.get("/laboratorios/{laboratorio_id}", response_model=LaboratorioSchema)
async def get_laboratorio(laboratorio_id: int, session: Session = Depends(get_db)):
    # Lógica para obter um laboratório específico pelo ID
    laboratorio = session.query(LaboratorioModel).filter(LaboratorioModel.id == laboratorio_id).first()
    if not laboratorio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laboratório não encontrado")
    return laboratorio
