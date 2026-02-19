from datetime import date
import uuid


class Informationsobjekt:
    def __init__(self, name: str, num: str, description: str | None = None, start: date | None = None, end = None): 
        self.name = name
        self.num = num
        # self.id = uuid
        self.start = start
        self.end = end
        self.description = description

    def to_markdown(self):
        return informationsobjekt_to_markdown(self)

    def __eq__(self, other):
        if (
                self.name == other.name
                and self.num == other.num
                # and self.id == other.id
                and self.start == other.start
                and self.end == other.end
                and self.description == other.description
                ):
            return True
        return False

class Arkiv(Informationsobjekt):
    def __init__(self, name: str, num: str, description: str | None = None, start = date.today(), end: date | None = None):
        super().__init__(name, num, description, start, end)

class Verksamhetsomrade(Informationsobjekt):
    def __init__(self, name: str, num: str, description: str | None = None, arkiv: str | None = None, start: date | None = None, end: date | None = None):
        super().__init__(name, num, description, start, end)
        self.arkiv = arkiv

    def __eq__(self, other):
        if (
                self.name == other.name
                and self.num == other.num
                # and self.id == other.id
                and self.start == other.start
                and self.end == other.end
                and self.description == other.description
                ):
            return True
        return False
    
class Processgrupp(Informationsobjekt):
    def __init__(self, name: str, num: str, verksamhetsomrade: str, description: str | None = None, start: date = date.today(), end: date | None = None):
        super().__init__(name, num, description, start, end)
        self.verksamhetsomrade = verksamhetsomrade

class Process(Informationsobjekt):
    def __init__(self, name: str, num: str, processgrupp: str, forvaring: str, description: str | None = None, start: date = date.today(), end: date | None = None):
        super().__init__(name, num, description, start, end)
        self.processgrupp = processgrupp


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
        md += informationsobjekt.start.strftime('%Y-%m-%d') + " "
    if informationsobjekt.start or informationsobjekt.end:
        md += "-"
    if informationsobjekt.end:
        md += " " + informationsobjekt.end.strftime('%Y%m%d')
            
    return md 

