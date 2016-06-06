from .resource import Resource
from .player import Player
from .fixture import Fixture


class Team(Resource):
    """
    "_links": {
      "self": { "href": "http://api.football-data.org/v1/teams/66" },
      "fixtures": { "href": "http://api.football-data.org/v1/teams/66/fixtures" },
      "players": { "href": "http://api.football-data.org/v1/teams/66/players" }
    },
    "name": "Manchester United FC",
    "shortName": "ManU",
    "squadMarketValue": "377,250,000 €",
    "crestUrl": "http://upload.wikimedia.org/wikipedia/de/d/da/Manchester_United_FC.svg"
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args)

        self.__uri = self.__uri or kwargs.get("_links", {}).get("self", {}).get("href")
        self.__fixtures = Resource(kwargs.get("_links", {}).get("fixtures", {}).get("href"), self.__api)
        self.__players = Resource(kwargs.get("_links", {}).get("players", {}).get("href"), self.__api)

        self.__id = self.__uri().split("/")[-1].__int__()
        self.name = kwargs.get("name","")
        self.league = kwargs.get("league", "")
        self.short_name = kwargs.get("shortName", "")
        self.squad_market_value = int(kwargs.get("squadMarketValue", "0,0").replace(',','').replace(' €','')) or -1
        self.crest_url = kwargs.get("crestUrl","")


    @property
    def players(self):
        if len(self.__players):
            return self.__players

        players = list()
        for player in self.__players.get()["players"]:
            player["team"] = self
            players.append(Player(**player))
        if len(players) != self.__players.get()["count"]:
            raise ValueError
        self.__players = players

        return self.__players

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

