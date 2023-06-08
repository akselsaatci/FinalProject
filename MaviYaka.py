

import unittest
from Calisan import Calisan


class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri, sektor, tecrube, maas, yipranma_payi):
        self._yipranma_payi = yipranma_payi
        super().__init__(tc_no, ad, soyad, yas, cinsiyet,
                         uyruk_bilgileri, sektor, tecrube, maas)

    def get_yipranma_payi(self):
        return self._yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self._yipranma_payi = yipranma_payi

    def get_yeni_maas(self):
        if self._yeni_maas == 0:
            self.zam_hakki()
        return self._yeni_maas

    def zam_hakki(self):
        # zam hakkını hesaplıyor ise zam hakkını geri dönmem gerekmezmi ama dökümasyonda maaşı set etmem de söylenmiş
        # tecrübe ay olarak geldiği için yıl olarak hesaplanması için 12'ye bölünüyor
        tecrube_yili = self._tecrube / 12
        # Buna gerek varmı ?  zaten else 'e düşücek
        try:
            if (tecrube_yili < 2):
                self._yeni_maas = self._maas * \
                    (self._yipranma_payi * 10) + self._maas
                return (self._yipranma_payi * 10)
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
        except:
            print("Hata oluştu")

    def __str__(self):
        return self._ad + " " + self._soyad + " " + str(self.get_yeni_maas()) + " " + str(self._tecrube)
