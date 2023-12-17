from kps_pelimoodit import KPSPelaajaVsPelaaja, KPSTekoaly
from tekoaly import TyhmaTekoaly, ParempiTekoaly

class PeliTehdas:
    @staticmethod
    def luo_peli(pelityyppi):
        if pelityyppi == "a":
            return KPSPelaajaVsPelaaja()
        if pelityyppi == "b":
            return KPSTekoaly(TyhmaTekoaly())
        if pelityyppi == "c":
            return KPSTekoaly(ParempiTekoaly())
        
        return False
