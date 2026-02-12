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

    def to_markdown(self):
        return informationsobjekt_to_markdown(self)


class Arkiv(Informationsobjekt):
    def __init__(self, name: str, num: str, uuid: str, description: str, start = date.today(), end = None):
        super().__init__(name, num, uuid, description, start, end)

class Verksamhetsomrade(Informationsobjekt):
    def __init__(self, name: str, num: str, uuid: str, description: str, arkiv: str,  start = date.today(), end = None):
        super().__init__(name, num, uuid, description, start, end)
        self.arkiv = arkiv

    
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


def informationsobjekt_to_markdown(informationsobjekt):
    match informationsobjekt:
        case Verksamhetsomrade():
            md = "# "
        case Processgrupp():
            md = "## "
        case Process():
            md = "### "
        case _:
            raise Exception("Inte ett giltigt informationsbojekt för att skapa markdown")


    md += informationsobjekt.num + " " + informationsobjekt.name

    if informationsobjekt.start or informationsobjekt.end:
        md += "\n"
    if informationsobjekt.start:
        md += " " + informationsobjekt.start.strftime('%Y%m%d') + " "
    if informationsobjekt.start or informationsobjekt.end:
        md += "-"
    if informationsobjekt.end:
        md += " " + informationsobjekt.end.strftime('%Y%m%d')
            
    return md 

