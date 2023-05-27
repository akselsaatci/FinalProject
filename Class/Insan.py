class Insan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk_bilgileri):
        self._tc_no = tc_no
        self._ad = ad
        self._soyad = soyad
        self._yas = yas
        self._cinsiyet = cinsiyet
        self._uyruk_bilgileri = uyruk_bilgileri

    def get_tc_no(self):
        return self._tc_no

    def set_tc_no(self, tc_no):
        self._tc_no = tc_no

    def get_ad(self):
        return self._ad

    def set_ad(self, ad):
        self._ad = ad

    def get_soyad(self):
        return self._soyad

    def set_soyad(self, soyad):
        self._soyad = soyad

    def get_yas(self):
        return self._yas

    def set_yas(self, yas):
        self._yas = yas

    def get_cinsiyet(self):
        return self._cinsiyet

    def set_cinsiyet(self, cinsiyet):
        self._cinsiyet = cinsiyet

    def get_uyruk_bilgileri(self):
        return self._uyruk_bilgileri

    def set_uyruk_bilgileri(self, uyruk_bilgileri):
        self._uyruk_bilgileri = uyruk_bilgileri

    def __str__(self):
        return "Tc No: {}\nAd: {}\nSoyad: {}\nYaş: {}\nCinsiyet: {}\nUyruk Bilgileri: {}".format(self._tc_no, self._ad, self._soyad, self._yas, self._cinsiyet, self._uyruk_bilgileri)
