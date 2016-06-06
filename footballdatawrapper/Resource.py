

class Resource:
    def __init__(self, uri=None, api=None):
        self.__uri = uri
        self.__api = api

    def get(self):
        return self.__api.__get_resource(self)

    @property
    def uri(self):
        return self.__uri

    def __len__(self):
        return 0



