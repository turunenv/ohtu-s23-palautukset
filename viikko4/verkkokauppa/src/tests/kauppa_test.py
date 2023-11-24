import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        #luodaan apumetodi, jolle haetun tuotteen saldo palauttaa joko positiivisen luvun tai nollan
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0
        
        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "Piimä", 1.99)
            if tuote_id == 3:
                return Tuote(3, "vessapaperi", 3)
            
        #otetaan luodut apumetodit käyttöön
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote   
        self.varasto_mock.saldo.side_effect = varasto_saldo

        #viitegeneraattori-mockin uusi-metodi palauttaa aina arvon 42
        self.viitegeneraattori_mock.uusi.return_value = 42

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
       
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla_kun_kaksi_eri_tuotetta(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 6.99)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla_kun_kaksi_samaa_tuotetta(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla_kun_kaksi_tuotetta_joista_toinen_loppu(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_metodi_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)

        self.kauppa.aloita_asiointi()

        self.assertEqual(self.kauppa._ostoskori.hinta(), 0)

    def test_jokainen_maksu_kayttaa_uutta_viitetta(self):
        #tätä testiä varten luodaan oma kauppansa
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("janne", "12345")

        #tarkista että viitegeneraattorin uusi-metodia on kutsuttu kerran
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 1)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("petteri", "1234576")

        #tarkista että viitegeneraattorin uusi-metodia on kutsuttu kahdesti
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 2)

    def test_metodi_poista_korista_poistaa_tuotteen_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)

        #poista lisätty tuote
        self.kauppa.poista_korista(1)

        #varmista että ostoskori on tyhjä
        self.assertEqual(len(self.kauppa._ostoskori._tuotteet), 0)

        


        



