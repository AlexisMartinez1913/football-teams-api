from fastapi import APIRouter
from fastapi import Depends, Path, Query
from typing import List

from starlette.responses import JSONResponse
from config.database import Session
from models.team import Team as TeamModel
from fastapi.encoders import jsonable_encoder
from services.team import TeamService
from schemas.team import Team

team_router = APIRouter()


#obtener todos los equipos.
@team_router.get('/teams', tags=['teams'], response_model=List[Team], status_code=200)
def get_teams() -> JSONResponse:
    #conectar db
    db = Session()
    result = TeamService(db).get_teams()
    #jsonable_encoder: convierte los objetos de Python a un formato compatible con JSON.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@team_router.post('/teams', tags=['teams'], response_model=dict, status_code=201)
def create_team(team: Team) -> JSONResponse:
    db = Session()
    TeamService(db).create_team(team)
    return JSONResponse(status_code=201, content={"message": "The football team has been registered"})


@team_router.get('/teams/{id}', tags=['teams'], response_model=Team)
def get_team_by_id(id: int = Path(ge=1, le=2000)) -> JSONResponse:
    db = Session()
    result = TeamService(db).get_team_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "the football team not found"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@team_router.put('/teams/{id}', tags=['teams'], response_model=dict, status_code=200)
def update_team(id: int, team: Team) -> JSONResponse:
    db = Session()
    result = TeamService(db).get_team_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "the football team not found"})

    TeamService(db).update_team(id, team)
    result.name = team.name
    result.founded = team.founded
    result.country = team.country
    result.stadium = team.stadium
    result.coach = team.coach
    db.commit()

    return JSONResponse(status_code=200, content={"message": "The football team has been updated successfully"})


@team_router.delete('/teams/{id}', tags=['teams'], response_model=dict, status_code=200)
def delete_team(id: int) -> JSONResponse:
    db = Session()
    result: TeamModel = db.query(TeamModel).filter(TeamModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "the football team not found"})

    TeamService(db).delete_team(id)

    return JSONResponse(status_code=200, content={"message": "The football team has been deleted successfully!"})
