from datetime import date
import unittest

from src.processtrad import Informationsobjekt, Arkiv, Verksamhetsomrade, Processgrupp, Process, informationsobjekt_to_markdown

# TODO implement tests

class testInformationsobjekt(unittest.TestCase):
    def test_eq(self):
        objekt1 = Informationsobjekt(name="objekt", num=1, description="test")
        objekt2 = Informationsobjekt(name="objekt", num=1, description="test")
        self.assertEqual(objekt1, objekt2)

    def test_verksamhetsomrade_to_md(self):
        verksamhetsomrade = Verksamhetsomrade(name="Styrande", num=1)
        md = verksamhetsomrade.to_markdown()
        self.assertEqual(md, "# 1. Styrande\n" + date.today().strftime('%Y-%m-%d') + " -")

    def test_processgrupp_to_md(self):
        processgrupp = Processgrupp(name="Styrande", verksamhetsomrade=1, num=1)
        md = processgrupp.to_markdown()
        self.assertEqual(md, "## 1.1. Styrande\n" + date.today().strftime('%Y-%m-%d') + " -")

    def test_process_to_md(self):
        process = Process(name="Styrande", verksamhetsomrade=1, processgrupp=1, num=1) 
        md = process.to_markdown()
        self.assertEqual(md, "### 1.1.1. Styrande\n" + date.today().strftime('%Y-%m-%d') + " -")



