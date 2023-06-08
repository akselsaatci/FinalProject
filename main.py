from Insan import Insan
from BeyazYaka import BeyazYaka
from Calisan import Calisan
from Issiz import Issiz
from MaviYaka import MaviYaka


def main():
    Insan1 = Insan("12345678910", "Ali", "Veli", 25, "Erkek", "Türk")
    print(str(Insan1))
    Insan2 = Insan("12345678911", "Ayşe", "Fatma", 25, "Kadın", "Türk")
    print(str(Insan2))
    Issiz1 = Issiz("12345678912", "Ahmet", "Mehmet", 25, "Erkek", "Türk", {
                   "mavi_yaka": 10, "beyaz_yaka": 5, "yonetici": 12})
    print(str(Issiz1))
    Issiz2 = Issiz("12345678913", "Ayşe", "Fatma", 25, "Kadın", "Türk", {
                   "mavi_yaka": 4, "beyaz_yaka": 7, "yonetici": 23})
    print(str(Issiz2))
    Issiz3 = Issiz("12345678914", "Ayşe", "Fatma", 25, "Kadın", "Türk", {
                   "mavi_yaka": 10, "beyaz_yaka": 1, "yonetici": 8})
    print(str(Issiz3))

    Calisan1 = Calisan("12345678915", "Ayşe", "Fatma", 25,
                       "Kadın", "Türk", "teknoloji", 24, 10000)
    print(str(Calisan1))
    Calisan2 = Calisan("12345678916", "Ayşe", "Fatma", 25,
                       "Kadın", "Türk", "teknoloji", 24, 10000)
    print(str(Calisan2))
    Calisan3 = Calisan("12345678917", "Ayşe", "Fatma", 25,
                       "Kadın", "Türk", "teknoloji", 24, 10000)
    print(str(Calisan3))

    MaviYaka1 = MaviYaka("12345678918", "Ayşe", "Fatma", 25, "Kadın", "Türk","teknoloji", 24, 10000, 10) 
    print(str(MaviYaka1))
    MaviYaka2 = MaviYaka("12345678919", "Ayşe", "Fatma", 25, "Kadın", "Türk","teknoloji", 24, 10000, 10)
    print(str(MaviYaka2))
    MaviYaka3 = MaviYaka("12345678920", "Ayşe", "Fatma", 25, "Kadın", "Türk","teknoloji", 24, 10000, 10)
    print(str(MaviYaka3))
    BeyazYaka1 = BeyazYaka("12345678921", "Ayşe", "Fatma", 25, "Kadın", "Türk","teknoloji", 24, 10000, 10)
    print(str(BeyazYaka1))
    BeyazYaka2 = BeyazYaka("12345678922", "Ayşe", "Fatma", 25, "Kadın", "Türk","teknoloji", 24, 10000, 10)
    print(str(BeyazYaka2))
    BeyazYaka3 = BeyazYaka("12345678923", "Ayşe", "Fatma", 25, "Kadın", "Türk","teknoloji", 24, 10000, 10)
    print(str(BeyazYaka3))
    

main()
