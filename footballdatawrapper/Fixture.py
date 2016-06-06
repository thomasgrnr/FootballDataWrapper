class Fixture:
    """
            "id": 149461,
            "soccerseasonId": 406,
            "date": "2014-07-08T20:00:00Z",
            "matchday": 6,
            "homeTeamName": "Brazil",
            "homeTeamId": 764,
            "awayTeamName": "Germany",
            "awayTeamId": 759,
            "result":
            {
                "goalsHomeTeam": 1,
                "goalsAwayTeam": 7
            }
    """
    def __init__(self, *args, **kwargs):
        self.__id = kwargs.get("id", -1)
        self.__home_team = kwargs.get("homeTeamId", -1)
        self.__away_team = kwargs.get("awayTeamId", -1)
        self.__matchday = kwargs.get("matchday", -1)
        self.__soccer_season = kwargs.get("soccerseasonId", -1)
        self.__result = kwargs.get("result", -1)


    @property
    def result(self):
        return self.__result

    @property
    def home_team(self):
        return self.__home_team
