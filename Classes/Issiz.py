from Enums.Statu import Statu
from Insan import Insan


class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri, gecmis_tecrubeler: dict):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri)
        self.statu_bul()
        self._gecmis_tecrubeler = gecmis_tecrubeler

    def get_gecmis_tecrubeler(self):
        return self._gecmis_tecrubeler

    def set_gecmis_tecrubeler(self, gecmis_tecrubeler):
        self._gecmis_tecrubeler = gecmis_tecrubeler

    def get_statu(self):
        return self.statu

    def set_statu(self, statu):
        self.statu = statu

    statu = 0

    def statu_bul(self):
        try:
            mavi_yaka = int(self._gecmis_tecrubeler["mavi_yaka"])
            beyaz_yaka = int(self._gecmis_tecrubeler["beyaz_yaka"])
            yonetici = int(self._gecmis_tecrubeler["yonetici"])
            mavi_yaka_orani = mavi_yaka * 20 / 100
            beyaz_yaka_orani = beyaz_yaka * 35 / 100
            yonetici_orani = yonetici * 45 / 100

            if mavi_yaka_orani > beyaz_yaka_orani and mavi_yaka_orani > yonetici_orani:
                self.statu = Statu.mavi_yaka
            elif beyaz_yaka_orani > mavi_yaka_orani and beyaz_yaka_orani > yonetici_orani:
                self.statu = Statu.beyaz_yaka
            elif yonetici_orani > mavi_yaka_orani and yonetici_orani > beyaz_yaka_orani:
                self.statu = Statu.yonetici

        except:
            print("Gecmis tecrubelerde hata mevcut")
