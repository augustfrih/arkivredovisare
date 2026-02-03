from datetime import date
import uuid


class Informationsobjekt:
    def __init__(self, name: str, num: str, uuid: str, description: str, start: date = date.today(), end = None):
        self.name = name
        self.num = num
        self.id = uuid
        self.start = start
        self.end = end
        self.description = description

class Verksamhetsomrade(Informationsobjekt):
    def __init__(self, name: str, num: str, uuid: str, description: str, start = date.today(), end = None):
        super().__init__(name, num, uuid, description, start, end)
    
class Processgrupp(Informationsobjekt):
    def __init__(self, name: str, num: str, uuid: str, description: str, verksamhetsomrade: str, beskrivning: str, start: date = date.today(), end: date | None = None):
        super().__init__(name, num, uuid, description, start, end)
        self.verksamhetsomrade = verksamhetsomrade
        self.beskrivning = beskrivning

class Process(Informationsobjekt):
    def __init__(self, name: str, num: str, uuid: str, description: str, processgrupp: str, beskrivning: str, forvaring: str, start: date = date.today(), end: date | None = None):
        super().__init__(name, num, uuid, description, start, end)
        self.processgrupp = processgrupp
        self.beskrivning = beskrivning


