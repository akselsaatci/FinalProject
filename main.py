from Insan import Insan
from BeyazYaka import BeyazYaka
from Calisan import Calisan
from Issiz import Issiz
from MaviYaka import MaviYaka
import pandas as pd


def main():
    try:
        # Öncelikle tüm objelerimi bir listede tutuyorum. Bu sayede daha sonra ekstra bir insan vs gibi bir class eklemek istersem bu listeye ekleyebilirim.
        obje_listesi = []
        # Gerekli objeleri oluşturuyorum
        Insan1 = Insan("151441122", "Ali", "Mehmet", 48, "Erkek", "Türk")
        print(str(Insan1))
        obje_listesi.append(Insan1)
        Insan2 = Insan("4545154784", "Ayşe", "Fatma", 59, "Kadın", "Türk")
        print(str(Insan2))
        obje_listesi.append(Insan2)
        Issiz1 = Issiz("23243546234", "Aksel", "Saatcı", 32, "Erkek", "Türk", {
            "mavi_yaka": 10, "beyaz_yaka": 5, "yonetici": 12})
        print(str(Issiz1))
        obje_listesi.append(Issiz1)
        Issiz2 = Issiz("345646544545", "Zeynep", "Fatma", 43, "Kadın", "Türk", {
            "mavi_yaka": 4, "beyaz_yaka": 7, "yonetici": 23})
        print(str(Issiz2))
        obje_listesi.append(Issiz2)
        Issiz3 = Issiz("231254354545", "Batuhan", "Doğa", 26, "Erkek", "Türk", {
            "mavi_yaka": 10, "beyaz_yaka": 1, "yonetici": 8})
        print(str(Issiz3))
        obje_listesi.append(Issiz3)

        Calisan1 = Calisan("34343434344", "Hasan", "Yiğit", 42,
                           "Erkek", "Türk", "teknoloji", 59, 5800)
        obje_listesi.append(Calisan1)
        print(str(Calisan1))
        Calisan2 = Calisan("23243354545", "Yiğit", "Meriç", 56,
                           "Erkek", "Türk", "muhasebe", 57, 15400)
        print(str(Calisan2))
        obje_listesi.append(Calisan2)
        Calisan3 = Calisan("23243567565", "Serkan", "Melih", 47,
                           "Erkek", "Türk", "teknoloji", 13, 23000)
        obje_listesi.append(Calisan3)
        print(str(Calisan3))

        MaviYaka1 = MaviYaka("23245564545", "Melih", "Fatma",
                             38, "Erkek", "Yabancı", "diğer", 0, 16800, 10)
        obje_listesi.append(MaviYaka1)
        print(str(MaviYaka1))
        MaviYaka2 = MaviYaka("343545454546", "Şeyma", "Aydın",
                             36, "Kadın", "Türk", "muhasebe", 4, 43000, 10)
        obje_listesi.append(MaviYaka2)
        print(str(MaviYaka2))
        MaviYaka3 = MaviYaka("232435645656", "Merve", "Kaya",
                             32, "Kadın", "Yabancı", "teknoloji", 23, 47800, 10)
        obje_listesi.append(MaviYaka3)
        print(str(MaviYaka3))
        BeyazYaka1 = BeyazYaka("232456565435", "Nihal", "Kaya",
                               30, "Kadın", "Türk", "diğer", 22, 60000, 10)
        obje_listesi.append(BeyazYaka1)
        print(str(BeyazYaka1))
        BeyazYaka2 = BeyazYaka("343454657565", "Ayşe", "Erdoğan",
                               27, "Kadın", "Türk", "muhasebe", 79, 15600, 10)
        obje_listesi.append(BeyazYaka2)
        print(str(BeyazYaka2))
        BeyazYaka3 = BeyazYaka("3413546653454", "Ümit", "Kalem",
                               26, "Erkek", "Yabancı", "inşaat", 8, 28000, 10)
        obje_listesi.append(BeyazYaka3)
        print(str(BeyazYaka3))
        # obje listemden datamı oluşturuyorum. Burda hata vermemesi için bazı yerlerde hasattr ile kontrol ediyorum. Listeyi de for ile dönerek gerekli alanları dolduruyorum.
        data = {
            "Nesne Değeri": [type(obje).__name__ for obje in obje_listesi],
            "TC No": [obje.get_tc_no() for obje in obje_listesi],
            "Ad": [obje.get_ad() for obje in obje_listesi],
            "Soyad": [obje.get_soyad() for obje in obje_listesi],
            "Yaş": [obje.get_yas() for obje in obje_listesi],
            "Cinsiyet": [obje.get_cinsiyet() for obje in obje_listesi],
            "Uyruk": [obje.get_uyruk_bilgileri() for obje in obje_listesi],
            "Sektör": [(obje.get_sektor() if hasattr(obje, "get_sektor") else 0) for obje in obje_listesi],
            "Tecrübe(Yıl)": [(obje.get_tecrube() / 12 if hasattr(obje, "get_tecrube") else 0)for obje in obje_listesi],
            "Maaş": [(obje.get_maas() if hasattr(obje, "get_maas") else 0) for obje in obje_listesi],
            "Yıpranma Payı": [(obje.get_yipranma_payi() if hasattr(obje, "get_yipranma_payi") else 0)for obje in obje_listesi],
            "Teşvik Primi": [(obje.get_tesvik_pirimi() if hasattr(obje, "get_tesvik_pirimi") else 0) for obje in obje_listesi],
            "Yeni Maaş": [(obje.get_yeni_maas() if hasattr(obje, "get_yeni_maas") else 0) for obje in obje_listesi]
        }
        print("---------------------")

        df = pd.DataFrame(columns=["Nesne Değeri", "TC No", "Ad", "Soyad", "Yaş",  "Cinsiyet", "Uyruk",
                                   "Sektör",  "Tecrübe(Yıl)", "Maaş",  "Yıpranma Payı",  "Teşvik Primi", "Yeni Maaş"], data=data)

        # Mavi yakalilar b)
        mavi_yakalar = df[df["Nesne Değeri"] == "MaviYaka"]

        # Mavi yakaların maaş ortalaması
        print("Mavi Yakalıların maaş ortalaması : " +
              str(mavi_yakalar["Maaş"].mean()))
        # Calisanlar b)
        calisanlar = df[df["Nesne Değeri"] == "Calisan"]
        # Calisanların maaş ortalaması b)
        print("Çalışanların maaş ortalaması " + str(calisanlar["Maaş"].mean()))
        # beyaz yakalilar  b)
        beyaz_yakalar = df[df["Nesne Değeri"] == "BeyazYaka"]
        # Beyaz yakaların maaş ortalaması b)
        print("Beyaz yakalıların maaş ortalaması " +
              str(beyaz_yakalar["Maaş"].mean()))

        # Maasi 15000 den fazla olanlarin listesi c)
        print("\n-----------------------\Maasi 15000 den fazla olanlarin listesi\n-----------------------\n")
        print(df[df["Maaş"] > 15000])

        # Küçükten büyüğe sıralanmış dataframe d)
        print(
            "\n-----------------------\nSort edilmiş dataframe\n-----------------------\n")
        print(df.sort_values(by=["Yeni Maaş"], ascending=False))

        # Tecrubesi 3 seneden fazla olan beyaz yakalilar e)
        print("\n-----------------------\nTecrubesi 3 seneden fazla olan beyaz yakalilar\n-----------------------\n")
        print(df[(df["Tecrübe(Yıl)"] > 3) & (
            df["Nesne Değeri"] == "BeyazYaka")])

        # Yeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanlar f)
        print("\n-----------------------\nYeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanlar\n-----------------------\n")

        print(df[(df["Yeni Maaş"] > 10000) & (df.index > 1)
                 & (df.index < 5)][["TC No", "Yeni Maaş"]])

        # g) Yeni dataframe oluşturulması
        print("\n-----------------------\nYeni DataFrame\n-----------------------\n")

        yeni_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]
        print(yeni_df)
    except:
        print("Hata oluştu")


main()
