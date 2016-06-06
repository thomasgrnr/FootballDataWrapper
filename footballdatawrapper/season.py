from .resource import Resource
from .team import Team
from .fixture import Fixture

class Season(Resource):
    """
    {
        "id": 394,
        "caption": "1. Bundesliga 2015/16",
        "league": "BL1",
        "year": "2015",
        "numberOfTeams": 18,
        "numberOfGames": 306,
        "lastUpdated": "2015-10-25T19:06:29Z"
    }
    """

    SEASON = "/soccerseasons"
    TEAMS = "/teams"
    FIXTURES = "/fixtures"
    LEAGUE_TABLE = "/leagueTable"

    def __init__(self, *args, **kwargs):
        super().__init__(*args)

        self.__id = kwargs.get("id")
        self.__uri = self.__uri or self.__api.ROOT_URL + self.SEASON + self.__id.__str__()
        self.caption = kwargs.get("caption")
        self.league = kwargs.get("league")
        self.year = kwargs.get("year")
        self.number_of_teams = kwargs.get("numberOfTeams")
        self.number_of_games = kwargs.get("numberOfGames")
        self.last_updated = kwargs.get("lastUpdated")

        self.__teams = Resource(self.__uri + self.TEAMS, self.__api)
        self.__fixtures = Resource(self.__uri + self.FIXTURES, self.__api)
        self.__league_table = Resource(self.__uri + self.LEAGUE_TABLE, self.__api)

    @property
    def teams(self):
        if len(self.__teams):
            return self.__teams

        teams = list()
        for team in self.__teams.get()["teams"]:
            team["league"] = self.league
            teams.append(Team(**team))
        if len(teams) != self.__teams.get()["count"]:
            raise ValueError
        self.__teams = teams

        return self.__teams


    @property
    def fixtures(self):
        if len(self.__fixtures):
            return self.__fixtures

        fixtures = list()
        for fixture in self.__fixtures.get()["fixtures"]:
            fixtures.append(Fixture(**fixture))
        if len(fixtures) != self.__fixtures.get()["count"]:
            raise ValueError
        self.__fixtures = fixtures

        return self.__fixtures