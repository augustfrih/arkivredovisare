import os
import sqlite3
from globals import DATABASE_PATH, MARKDOWN_PATH
from src.processtrad import Process, Processgrupp, Verksamhetsomrade

def markdown_till_informationsobjekt(database_path: str = DATABASE_PATH, markdown_path: str = MARKDOWN_PATH):
    # Get absolute paths for markdown and database
    database_path = os.path.abspath(database_path)
    markdown_path = os.path.abspath(markdown_path)

    # Put the markdown in a variable
    with open(markdown_path) as f:
        markdown = f.read()
        
    #TODO split the markdown into informationsobjekt

    #TODO create database file if not exists

    #TODO if database file exists, check that it is well formed

    #TODO read the informationsobjekt to the tables

    # Create this function
    pass

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
