import json
import requests
from io import StringIO

from .player import Player
from .fixture import Fixture
from .team import Team


class FootballDataAPI:

    ROOT_URL = "http://api.football-data.org/v1/{:s}"

    def __init__(self, api_key):
        self.__headers = {
            'X-Auth-Token': api_key,
            'X-Response-Control': "full"
        }
        self.__requests_available = 2 ** 32 - 1

    def __get_response(self, query):
        query = query if ROOT_URL in query else ROOT_URL.format(query)
        response = requests.get(query, headers=self.__headers)
        response.raise_for_status()
        self.__requests_available = response.headers.get("X-Requests-Available", self.__requests_available)
        return json.load(StringIO(response.content.decode('utf-8')))

    def get_one_fixture(self, fixture_id):
        response = self.__get_response("/v1/fixtures/{id}".format(fixture_id))
        return Fixture(response.get("fixture", {}))

    def get_one_team(self, id):
        response = self.__get_response("v1/teams/{id}".format(id))
        return Team(response)

    def get_players(self, id):
        response = self.__get_response("v1/teams/{id}/players".format(id))
        players = list()
        for player in response.get("players",[]):
            players.append(Player(player))

        if len(players) == response.get("count", 0):
            return players
        else:
            raise ValueError

    def __get_resource(self, resource):
        return self.__get_response(resource.uri)