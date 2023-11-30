from komennot import Summa, Erotus, Nollaus, Kumoa, Tuntematon
from komento_enum import KomentoEnum

class KomentoTehdas:
    def __init__(self, lue_syote, sovellus):
        self.lue_syote = lue_syote
        self.sovellus = sovellus
      
        self.komennot = {
            KomentoEnum.SUMMA: Summa(self.lue_syote, self.sovellus),
            KomentoEnum.EROTUS: Erotus(self.lue_syote, self.sovellus),
            KomentoEnum.NOLLAUS: Nollaus(self.sovellus),
            KomentoEnum.KUMOA: Kumoa(self.sovellus)
        }

    def hae(self, komento_enum):
        if komento_enum in self.komennot:
            komento = self.komennot[komento_enum]

            return komento
        
        return Tuntematon()
    
    