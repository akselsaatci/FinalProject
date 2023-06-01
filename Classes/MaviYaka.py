

from Classes.Calisan import Calisan


class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet,
                         uyruk_bilgileri, sektor, tecrube, maas)

    def zam_hakki(self):
        raise NotImplementedError()
