import unittest
from src.markdown import md_line_to_informationsobjekt
from src.processtrad import Process, Processgrupp, Verksamhetsomrade

class testMd_line_to_informationsobjekt(unittest.TestCase):
    def test_verksamhetsomrade_md_to_informationsobjekt(self):
        verksamhetsomrade_md = "# 1. Styrande"
        self.assertEqual(
                md_line_to_informationsobjekt(verksamhetsomrade_md),
                Verksamhetsomrade("Styrande", num=1)
                )
    
    def test_processgrupp_md_to_informationsobjekt(self):
        verksamhetsomrade_md = "## 1.1. Styrelsearenden"
        self.assertEqual(
                md_line_to_informationsobjekt(verksamhetsomrade_md),
                Processgrupp("Styrelsearenden", num=1, verksamhetsomrade=1)
                )

    def test_process_md_to_informationsobjekt(self):
        process_md = "### 1.1.1. Styrelseprotokoll"
        self.assertEqual(
                md_line_to_informationsobjekt(process_md),
                Process(name="Styrelseprotokoll", verksamhetsomrade=1, processgrupp=1, num=1)
                )
