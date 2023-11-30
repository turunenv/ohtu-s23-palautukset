class SyoteKomento:
    def __init__(self, lue_syote, sovellus):
        self.lue_syote = lue_syote
        self.sovellus = sovellus

    @property
    def syote(self):
        try:
            syote = int(self.lue_syote())
            return syote
        except ValueError:
            return None


class Summa(SyoteKomento):
    def __init__(self, lue_syote, sovellus):
        super().__init__(lue_syote, sovellus)

    def suorita(self):
        if self.syote:
            self.sovellus.plus(self.syote)

class Erotus(SyoteKomento):
    def __init__(self, lue_syote, sovellus):
        super().__init__(lue_syote, sovellus)

    def suorita(self):
        if self.syote:
            self.sovellus.miinus(self.syote)

class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus
    def suorita(self):
        self.sovellus.nollaa()

class Kumoa():
    def __init__(self, sovellus):
        self.sovellus = sovellus
    def suorita(self):
        return

class Tuntematon:
    def suorita(self):
        return