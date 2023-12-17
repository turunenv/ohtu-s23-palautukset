SIIRROT = ["k", "p", "s"]

class TyhmaTekoaly:
    def __init__(self):
        self._siirto_num = 0

    def anna_siirto(self, siirto):
        self._siirto_num += 1
        
        siirto_idx = self._siirto_num % len(SIIRROT)
        return SIIRROT[siirto_idx]
    

class ParempiTekoaly:
    def __init__(self):
        self.vastustajan_siirrot = {siirto: 0 for siirto in SIIRROT}

    def vastustajan_suosikki_siirto(self):
        return max(self.vastustajan_siirrot, key=self.vastustajan_siirrot.get)
    
    def anna_voittava_siirto(self, siirto):
        voittajat = {
            "k": "p",
            "p": "s",
            "s": "k"
        }

        return voittajat[siirto]

    def anna_siirto(self, vastustajan_siirto):
        if not vastustajan_siirto in SIIRROT:
            return "k"

        self.vastustajan_siirrot[vastustajan_siirto] += 1

        suosikki = self.vastustajan_suosikki_siirto()
        vastaus = self.anna_voittava_siirto(suosikki)

        return vastaus
