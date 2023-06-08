
from Insan import Insan


class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri, gecmis_tecrubeler: dict):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri)
        self._gecmis_tecrubeler = gecmis_tecrubeler
        self.statu_bul()

    def get_gecmis_tecrubeler(self):
        return self._gecmis_tecrubeler

    def set_gecmis_tecrubeler(self, gecmis_tecrubeler):
        self._gecmis_tecrubeler = gecmis_tecrubeler

    def get_statu(self):
        if(self.statu == "Bulunmadi"):
            self.statu_bul()
        return self.statu

    def set_statu(self, statu):
        self.statu = statu

    statu = "Bulunmadi"

    def statu_bul(self):
        try:
            tecrubeler = self._gecmis_tecrubeler
            mavi_yaka = int(self._gecmis_tecrubeler["mavi_yaka"])
            beyaz_yaka = int(self._gecmis_tecrubeler["beyaz_yaka"])
            yonetici = int(self._gecmis_tecrubeler["yonetici"])
            mavi_yaka_orani = mavi_yaka * 20 / 100
            beyaz_yaka_orani = beyaz_yaka * 35 / 100
            yonetici_orani = yonetici * 45 / 100

            if mavi_yaka_orani > beyaz_yaka_orani and mavi_yaka_orani > yonetici_orani:
                self.statu = "Mavi Yaka"
            elif beyaz_yaka_orani > mavi_yaka_orani and beyaz_yaka_orani > yonetici_orani:
                self.statu = "Beyaz Yaka"
            elif yonetici_orani > mavi_yaka_orani and yonetici_orani > beyaz_yaka_orani:
                self.statu = "Yonetici"

        except:
            print("Gecmis tecrubelerde hata mevcut")

    def __str__(self):
        return self._ad + " " + self._soyad + "\nStatu: {}".format(self.get_statu())
