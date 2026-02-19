import unittest
from markdown import md_line_to_informationsobjekt
from processtrad import Verksamhetsomrade

class testMd_line_to_informationsobjekt(unittest.TestCase):
    def test_verksamhetsomrade_md_to_informationsobjekt(self):
        verksamhetsomrade_md = "# 1. Verksamhetsomrade"
        self.assertEqual(
                md_line_to_informationsobjekt(verksamhetsomrade_md),
                Verksamhetsomrade("Styrande", "1")
                )
