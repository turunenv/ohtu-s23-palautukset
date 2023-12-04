OLETUSKAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.validoi_kapasiteetti(
            kapasiteetti, 
            OLETUSKAPASITEETTI
        )

        self.kasvatuskoko = self.validoi_kasvatus_koko(
            kasvatuskoko,
            OLETUSKASVATUS 
        )

        self.luvut = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def validoi_kapasiteetti(self, kapasiteetti, oletusarvo):
        try:
            kapasiteetti = int(kapasiteetti)
            if kapasiteetti > 0:
                return kapasiteetti
        except (ValueError, TypeError):
            return oletusarvo
        
    def validoi_kasvatus_koko(self, kasvatus, oletusarvo):
        try:
            kasvatus = int(kasvatus)
            if kasvatus > 0:
                return kasvatus
        except (ValueError, TypeError):
            return oletusarvo

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False
        
        if self.kapasiteetti_taynna():
            self.lisaa_kapasiteettia()
        
        self.luvut[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1

        return True

    def kapasiteetti_taynna(self):
        return len(self.luvut) == self.alkioiden_lkm
    
    def lisaa_kapasiteettia(self):
        luvut_temp = self.luvut

        self.luvut = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(luvut_temp, self.luvut)

    def poista(self, luku):
        if luku not in self.luvut:
            return False
        
        indeksi = self.luvut.index(luku)
        self.luvut[indeksi] = 0

        for i in range(indeksi, self.alkioiden_lkm - 1):
            temp = self.luvut[i]
            self.luvut[i] = self.luvut[i + 1]
            self.luvut[i + 1] = temp
        
        self.alkioiden_lkm -= 1

        return True
    
    def kuuluu(self, luku):
        return luku in self.luvut

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.luvut[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            joukko.lisaa(b_taulu[i])

        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        
        for i in range(0, len(a_taulu)):
            if b.kuuluu(a_taulu[i]):
                joukko.lisaa(a_taulu[i])

        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        
        for luku in a_taulu:
            if not b.kuuluu(luku):
                joukko.lisaa(luku)

        return joukko

    def __str__(self):
        luku_merkkijono = ", ". join(list(map(lambda x: str(x), self.to_int_list())))

        return f"{{{luku_merkkijono}}}"
