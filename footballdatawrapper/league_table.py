from .resource import Resource

class LeagueTable(Resource):
    """
    "matchday": 10,
    "standing":
        [
            {
                "rank": 1,
                "team": "ManCity",
                "teamId": 65,
                "playedGames": 10,
                "crestURI": "http://upload.wikimedia.org/wikipedia/de/f/fd/ManCity.svg",
                "points": 22,
                "goals": 24,
                "goalsAgainst": 8,
                "goalDifference": 16
            },
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args)

        self.matchday = kwargs.get("matchday")
        self.standings = []

