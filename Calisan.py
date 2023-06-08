
from Insan import Insan


sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]


class Calisan(Insan):
    # Tecrübe ay değeri olarak geliyor dikkat edilmeli
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri)
        self._tecrube = tecrube
        self._maas = maas
        self._yeni_maas = 0
        self.sektor_bul
        if sektor in sektorler:
            self._sektor = sektor
        else:
            raise ValueError("Sektor bulunamadi")

    def zam_hakki(self):
        # tecrübe ay olarak geldiği için yıl olarak hesaplanması için 12'ye bölünüyor
        tecrube_yili = self._tecrube / 12
        # Buna gerek varmı ?  zaten else 'e düşücek
        if (tecrube_yili < 2):
            self._yeni_maas = self._maas
            return 0
        elif (tecrube_yili < 4 and tecrube_yili >= 2 and self._maas < 15000):
            zam = self._maas % tecrube_yili
            self._yeni_maas = self._maas + self._maas * zam
            return zam

        elif (tecrube_yili >= 4 and self._maas < 25000):
            zam = (self._maas % tecrube_yili) / 2
            self._yeni_maas = self._maas + self._maas * zam
            return zam
        else:
            self._yeni_maas = self._maas
            return 0

    def get_sektor(self):
        return self._sektor

    def set_sektor(self, sektor):
        if sektor in sektorler:
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

    def __str__(self):
        return self._ad + " " + self._soyad + " " + str(self._yeni_maas) + " " + str(self._tecrube)
