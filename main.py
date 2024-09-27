from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.team import team_router

app = FastAPI()
app.title = "Football teams API"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(team_router)

# llamado de conexion db
Base.metadata.create_all(bind=engine)
