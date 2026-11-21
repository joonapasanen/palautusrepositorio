import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from tuote import Tuote

KAUPAN_TILI = "33333-44455"


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # varaston tuotteet ja saldot: tuote 3 on loppu
        tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipä", 3),
            3: Tuote(3, "juusto", 3),
        }
        saldot = {1: 10, 2: 5, 3: 0}

        self.varasto_mock = Mock()
        self.varasto_mock.saldo.side_effect = lambda tuote_id: saldot.get(tuote_id)
        self.varasto_mock.hae_tuote.side_effect = lambda tuote_id: tuotteet.get(tuote_id)

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        self.kauppa.aloita_asiointi()

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_jalkeen_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", KAUPAN_TILI, 5)

    def test_kahden_eri_tuotteen_ostossa_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # 5 + 3 = 8
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", KAUPAN_TILI, 8)

    def test_kahden_saman_tuotteen_ostossa_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # 2 * 5 = 10
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", KAUPAN_TILI, 10)

    def test_loppuneen_tuotteen_hintaa_ei_lasketa_tilisiirtoon(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # tuote 3 on loppu, joten summaan lasketaan vain tuote 1
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", KAUPAN_TILI, 5)
