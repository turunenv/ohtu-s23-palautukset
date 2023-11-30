class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._arvohistoria = []

    def tallenna_historiaan(self, arvo):
        self._arvohistoria.append(arvo)

    def miinus(self, operandi):
        self.tallenna_historiaan(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.tallenna_historiaan(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self.tallenna_historiaan(self._arvo)
        self._arvo = 0

    def aseta_edellinen_arvo(self):
        if len(self._arvohistoria) > 0:
            self._arvo = self._arvohistoria.pop(-1)

    def aseta_arvo(self, arvo):
        self.tallenna_historiaan(self._arvo)
        self._arvo = arvo

    def arvo(self):
        return self._arvo
