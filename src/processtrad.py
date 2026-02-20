from datetime import date
import uuid


class Informationsobjekt:
    def __init__(self, name: str, num: int, description: str | None = None, start: date | None = None, end = None): 
        self.name = name
        self.num = num
        # self.id = uuid
        self.end = end
        self.description = description
        if not start:
            self.start = date.today()
        else:
            self.start = start

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
    def __init__(self, name: str, num: int, description: str | None = None, start: date | None = None, end: date | None = None):
        super().__init__(name, num, description, start, end)

class Verksamhetsomrade(Informationsobjekt):
    def __init__(self, name: str, num: int, description: str | None = None, arkiv: str | None = None, start: date | None = None, end: date | None = None):
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
    def __init__(self, name: str, verksamhetsomrade: int, num: int, description: str | None = None, start: date | None = None, end: date | None = None):
        super().__init__(name, num, description, start, end)
        self.verksamhetsomrade = verksamhetsomrade

class Process(Informationsobjekt):
    def __init__(self, name: str, verksamhetsomrade: int, processgrupp: int, num: int, forvaring: str, description: str | None = None, start: date | None = None, end: date | None = None):
        super().__init__(name, num, description, start, end)
        self.processgrupp = processgrupp
        self.verksamhetsomrade = verksamhetsomrade


def informationsobjekt_to_markdown(informationsobjekt):
    match informationsobjekt:
        case Verksamhetsomrade():
            md = "# " + str(informationsobjekt.num) + ". "
        case Processgrupp():
            md = "## " + str(informationsobjekt.verksamhetsomrade) + "." + str(informationsobjekt.num) + ". "
        case Process():
            md = "### " + str(informationsobjekt.verksamhetsomrade) + "." + str(informationsobjekt.processgrupp) + "." + str(informationsobjekt.num) + ". "
        case _:
            raise Exception("Inte ett giltigt informationsbojekt för att skapa markdown")

    md += informationsobjekt.name

    if informationsobjekt.start or informationsobjekt.end:
        md += "\n"
    if informationsobjekt.start:
        md += informationsobjekt.start.strftime('%Y-%m-%d') + " "
    if informationsobjekt.start or informationsobjekt.end:
        md += "-"
    if informationsobjekt.end:
        md += " " + informationsobjekt.end.strftime('%Y%m%d')
            
    return md 

