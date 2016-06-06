from datetime import datetime
from .resource import Resource

class Player(Resource):
    """
    {
            "id": 16,
            "name": "Bastian Schweinsteiger",
            "position": "Central Midfield",
            "jerseyNumber": 31,
            "dateOfBirth": "1984-08-01",
            "nationality": "Germany",
            "contractUntil": "2018-06-30",
            "marketValue": "22,000,000 €"
        },
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.__id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.team = kwargs.get("team")
        self.position = kwargs.get("position")
        self.jersey_number = kwargs.get("jerseyNumber")
        self.date_of_birth = kwargs.get("dateOfBirth")
        self.nationality = kwargs.get("nationality")
        self.market_value = int(kwargs.get("marketValue", "0,0").replace(',','').replace(' €','')) or -1

        # TODO : datetime support
        self.contract_until = kwargs.get("contractUntil")




