

from Calisan import Calisan


class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri, sektor, tecrube, maas, tesvik_primi):
        self._tesvik_primi = tesvik_primi
        self._yeni_maas = 0
        super().__init__(tc_no, ad, soyad, yas, cinsiyet,
                         uyruk_bilgileri, sektor, tecrube, maas)

    def get_tesvik_pirimi(self):
        return self._tesvik_primi

    def set_tesvik_pirimi(self, tesvik_pirimi):
        self._tesvik_primi = tesvik_pirimi

    def get_yeni_maas(self):
        if self._yeni_maas == 0:
            self.zam_hakki()
        return self._yeni_maas

    def zam_hakki(self):
        tecrube_yili = self._tecrube / 12
        try:
            if tecrube_yili < 2:
                self._yeni_maas = (
                    self._maas + self._tesvik_primi)
                return self._tesvik_primi * self._maas
            elif tecrube_yili < 4 and tecrube_yili >= 2 and self._maas < 15000:
                zam_miktari = (self._maas % tecrube_yili) * \
                    5 + self._tesvik_primi
                self._yeni_maas = self._maas + zam_miktari
                return zam_miktari
            elif tecrube_yili > 4 and self._maas < 25000:
                zam_miktari = (self._maas % tecrube_yili) * \
                    4 + self._tesvik_primi
                self._yeni_maas = self._maas + zam_miktari
                return zam_miktari
            else:
                self._yeni_maas = self._maas
                return 0
        except:
            print(str(self._tc_no) +
                  " TC ye sahip Beyaz yakalının zam hakkı fonksiyonunda Hata oluştu")

    def __str__(self):
        return self._ad + " " + self._soyad + " " + str(self.get_yeni_maas()) + " " + str(self._tecrube)

