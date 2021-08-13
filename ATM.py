print("""
***************************************
Bankamatiğe Hoşgeldiniz 

İşlemler;

1. Bakiye Sorma

2. Para Yatırma

3. Para Çekme

4. Döviz Satın Al

Kartınız almak için 0 tuşuna basınız.
***************************************
""")
dolar_bakiye = 0
euro_bakiye = 0
gram_altin_bakiye = 0
bakiye = 10000
dolar_kuru = 7.63
euro_kuru = 9.35
gram_altin_kuru = 462.40

while True:
    islem = int(input("İşlemi seçiniz:"))
    if islem == 0:
        print("Yine bekleriz....")
        break
    elif islem == 1:
        secim = input("Hangi tür bakiye sormak istiyorsunuz\n(TL, Dolar, Euro, Altın?):")
        if secim == "TL":
            print("Bakiyeniz {} TL'dir.".format(bakiye))
        elif secim == "Dolar":
            print("Bakiyeniz {} $'dir.".format(dolar_bakiye))
        elif secim == "Euro":
            print("Bakiyeniz {} €'dir.".format(euro_bakiye))
        elif secim == "Altın":
            print("Bakiyeniz {} gr'dir.".format(gram_altin_bakiye))
    elif islem == 2:
        miktar = int(input("Miktarı giriniz:"))
        bakiye += miktar
    elif islem == 3:
        miktar = int(input("Miktarı giriniz:"))
        if bakiye - miktar < 0:
            print("Böyle bir miktar çekemezsiniz.")
            continue
        bakiye -= miktar
    elif islem == 4:
        secim = input("Yapmak istediginiz islemi seçiniz\n(Dolar, Euro, Altın):")
        if secim == "Dolar":
            dolar_miktar = int(input("Dolar miktarını giriniz:"))
            dolar_bakiye += dolar_miktar
            if bakiye - (dolar_miktar * dolar_kuru) < 0:
                print("Bu miktarda dolar alışı yapmak için yeterli bakiyeniz yoktur.")
                continue
            bakiye -= (dolar_miktar * dolar_kuru)
        elif secim == "Euro":
            euro_miktar = int(input("Euro miktarını giriniz:"))
            euro_bakiye += euro_miktar
            if bakiye - (euro_miktar * dolar_kuru) < 0:
                print("Bu miktarda euro alışı yapmak için yeterli bakiyeniz yoktur.")
                continue
            bakiye -= (euro_miktar * euro_kuru)
        elif secim == "Altın":
            gram_altin_miktar = int(input("Altin miktarını giriniz:"))
            gram_altin_bakiye += gram_altin_miktar
            if bakiye - (gram_altin_miktar * gram_altin_kuru) < 0:
                print("Bu miktarda gram altın alışı yapmak için yeterli bakiyeniz yoktur.")
                continue
            bakiye -= (gram_altin_miktar * gram_altin_kuru)
    else:
        print("Geçersiz işlem....")
