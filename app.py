from fastapi import FastAPI
from router.routers import router as agendamento_router


app = FastAPI(
    title="Agendamento API",
    description="API para gerenciamento de agendamentos",
    version="1.0.0",
)

@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API de Agendamento!"}

app.include_router(agendamento_router)