from models.team import Team as TeamModel
from schemas.team import Team

#lógica para manipular los datos del equipo de fútbol.
class TeamService:

    def __init__(self, db):
        self.db = db

    def get_teams(self):
        result = self.db.query(TeamModel).all()
        return result

    def get_team_by_id(self, id: int):
        result = self.db.query(TeamModel).filter(TeamModel.id == id).first()
        return result

    def create_team(self, team: Team):
        new_team = TeamModel(**team.model_dump())
        self.db.add(new_team)
        self.db.commit()
        return

    def update_team(self, id: int, data: Team):
        team = self.db.query(TeamModel).filter(TeamModel.id == id).first()
        team.name = data.name
        team.founded = data.founded
        team.country = data.country
        team.stadium = data.stadium
        team.coach = data.coach

        self.db.commit()
        return

    def delete_team(self, id: int):
        self.db.query(TeamModel).filter(TeamModel.id == id).delete()
        self.db.commit()
        return 
