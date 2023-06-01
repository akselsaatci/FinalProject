from Insan import Insan
from Enum.Sektor import Sektor
import Helper.Functions as Helper


class Calisan(Insan):
    # Tecrübe ay değeri olarak geliyor dikkat edilmeli
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri)
        self._tecrube = tecrube
        self._maas = maas
        if (self.sektor_bul(sektor) != None):
            self._sektor = sektor
        else:
            raise ValueError("Sektor bulunamadi")

    def zam_hakki(self):
        # tecrübe ay olarak geldiği için yıl olarak hesaplanması için 12'ye bölünüyor
        tecrube_yili = self._tecrube / 12
        if (tecrube_yili < 2):
            return 0
        elif (tecrube_yili < 4 and tecrube_yili >= 2 and self._maas < 15000):
            return self._maas % tecrube_yili
        elif (tecrube_yili >= 4 and self._maas < 25000):
            return (self._maas % tecrube_yili) / 2

    def get_sektor(self):
        return self._sektor

    def set_sektor(self, sektor):
        if (self.sektor_bul(sektor) != None):
            self._sektor = sektor
        else:
            raise ValueError("Sektor bulunamadi")

    def get_tecrube(self):
        return self._tecrube

    def set_tecrube(self, tecrube):
        self._tecrube = tecrube

    def get_maas(self):
        return self._maas

    def set_maas(self, maas):
        self._maas = maas

    def sektor_bul(sektor):
        sektor_var_mi = Helper.inputu_enumda_valide_et(Sektor, sektor)
        if (sektor_var_mi):
            return sektor
        else:
            return None
