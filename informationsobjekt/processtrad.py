from datetime import date
import uuid


class informationsobjekt:
    def __init__(self, name: str, num: str, uuid: str, description: str, start: date = date.today(), end = None):
        self.name = name
        self.num = num
        self.id = uuid
        self.start = start
        self.end = end
        self.description = description

class verksamhetsomrade(informationsobjekt):
    def __init__(self, name: str, num: str, uuid: str, description: str, start = date.today(), end = None):
        super().__init__(name, num, uuid, description, start, end)
    
class processgrupp(informationsobjekt):
    def __init__(self, name: str, num: str, uuid: str, description: str, start = date.today(), end = None, verksamhetsomrade):
        super().__init__(name, num, uuid, description, start, end)
        self.verksamhetsomrade = verksamhetsomrade



