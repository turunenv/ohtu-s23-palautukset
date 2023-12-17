from kivi_paperi_sakset import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")
    
class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly):
        self.tekoaly = tekoaly
    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto(ensimmaisen_siirto)
        print(f"Tietokone valitsi: {siirto}")

        return siirto

    