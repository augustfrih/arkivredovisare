import os
import sqlite3
from globals import DATABASE_PATH, MARKDOWN_PATH
from src.processtrad import Process, Processgrupp, Verksamhetsomrade


def markdown_till_informationsobjekt(
        database_path: str = DATABASE_PATH, markdown_path: str = MARKDOWN_PATH
        ):
    # Get absolute paths for markdown and database
    database_path = os.path.abspath(database_path)
    markdown_path = os.path.abspath(markdown_path)

    # Put the markdown in a variable
    with open(markdown_path) as f:
        markdown = f.read()

    # TODO split the markdown into informationsobjekt

    verksamhetsomrade_list = []
    processgrupp_list = []
    process_list = []

    markdown_split = markdown.split("\n")

    for line in markdown_split:
        objekt = md_line_to_informationsobjekt(line)
        match objekt:
            case Verksamhetsomrade():
                verksamhetsomrade_list.append(objekt)
            case Processgrupp():
                processgrupp_list.append(objekt)
            case Process():
                process_list.append(objekt)
            case _:
                pass

    # create or connect to database
    con = sqlite3.connect(database_path)
    cur = con.cursor()

    create_processtrad_table_if_not_exists(cur)

    # TODO read the informationsobjekt to the tables
    add_to_table(cur, verksamhetsomrade_list, processgrupp_list, process_list)

    # Create this function

# def sql_till_markdownfil(database=DATABASE_PATH, dest_path="arkivredovisning.md"):
#     # Import all informationsobjekt from the database
#     con = sqlite3.connect(database)
#     cur = con.cursor()
#
#
#     # Create lists for the different levels of informationsobjekt and populate them
#     verksamhetsomraden, processgrupper, processer = [], [], []
#     for objekt in informationsobjekt:
#         if isinstance(objekt, Verksamhetsomrade):
#             verksamhetsomraden.append(objekt)
#         if isinstance(objekt, Processgrupp):
#             processgrupper.append(objekt)
#         if isinstance(objekt, Process):
#             processer.append(objekt)
#
#     verksamhetsomraden.sort(key=lambda s: s.num)
#     processgrupper.sort(key=lambda s: s.num)
#     processer.sort(key=lambda s: s.num)
#     # Create markdown from the lists of informationsobjekt
#     markdown = ""
#     for verkasmhetsomrade in verksamhetsomraden:
#         markdown += "# " verkasmhetsomrade.num + " " + verkasmhetsomrade.name + "\n"
#         for processgrupp in processgrupper:
#             if processgrupp.num.startswith(verksamhetsomrade.num):
#                 markdown += processgrupp.num + " " +
#
#
#
#     abs_path = os.path.abspath("./content/" + dest_path)
#     with open(abs_path, "w") as f:
#         _ = f.write(markdown)
#
# def informationsobjekt_till_header(informationsobjekt):
#     if type(informationsobjekt) ==


def md_line_to_informationsobjekt(line: str):
    hashes, num, text = line.split(" ", 2)
    if num.endswith("."):
        num = num[:-1]

    if hashes == "#":
        objekt = Verksamhetsomrade(text, int(num), end=None)
    elif hashes == "##":
        verksamhetsomrade, num = num.split(".")
        objekt = Processgrupp(text, int(verksamhetsomrade), int(num))
    elif hashes == "###":
        verksamhetsomrade, processgrupp, num = num.split(".")
        objekt = Process(name=text, verksamhetsomrade=int(verksamhetsomrade), processgrupp=int(processgrupp), num=int(num))
    else:
        print(f"{line} was not added to the db")
        return
    return objekt

def create_processtrad_table_if_not_exists(cur):

    # create the verkshametsomrade table
    create_verksamhetsomrade_command = """
    CREATE TABLE IF NOT EXISTS verksamhetsomrade (
            num INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200),
            arkiv VARCHAR(100),
            start VARCHAR(100) NOT NULL,
            end VARCHAR(100)
            )
    """

    # create the processgrupp table
    create_processgrupp_command = """
    CREATE TABLE IF NOT EXISTS processgrupp (
            num INT PRIMARY KEY,
            verksamhetsomrade INT NOT NULL,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200),
            arkiv VARCHAR(100),
            start VARCHAR(100) NOT NULL,
            end VARCHAR(100)
            )
    """

    # fill the veekshametsomrade table
    create_process_command = """
    CREATE TABLE IF NOT EXISTS process (
            num INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200),
            forvaring VARCHAR(100),
            arkiv VARCHAR(100),
            start VARCHAR(100) NOT NULL,
            end VARCHAR(100)
            )
    """

    _ = cur.execute(create_verksamhetsomrade_command)
    _ = cur.execute(create_processgrupp_command)
    _ = cur.execute(create_process_command)

def add_to_table(cursor, verksamhetsomrade_list, processgrupp_list, process_list):
    pass
