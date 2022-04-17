import time
import random
from re import split


class Kumanda():
    def __init__(self, tv_durumu="Kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="TRT"):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durumu == "Açık":
            print("Televizyon zaten açık.")
        else:
            print("Televizyon Açılıyor...")
            time.sleep(1)
            self.tv_durumu = "Açık"

    def tv_kapat(self):
        if self.tv_durumu == "Kapalı":
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon Kapatılıyor...")
            self.tv_durumu = "Kapalı"

    def ses(self):
        while True:
            sesayari = input("ses yükseltme '>', ses azaltma '<', çıkmak için 'q' :")

            if sesayari == "q":
                print("Programdan Çıkılıyor..")
                break
            elif sesayari == ">":
                print("Ses arttırılıyor...")
                time.sleep(1)
                self.ses += 1
            elif sesayari == "<":
                print("Ses azaltılıyor...")
                time.sleep(1)
                self.tv_ses -= 1


    def kanal_ekle(self, kanal_ismi):
        print("Kanal Ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi...")

    def Kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki kanal :",self.kanal)

    def __str__(self):
        return "Televizyon Durumu : {}\nSes : {}\nKanal Listesi :{}\nŞuanki Kanal : {}".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)


kumanda = Kumanda()

print("""
*******************************
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısı Öğrenme
6. Şuanki Kanal
7. Televizyon Bilgileri
'Çıkmak için Q ya basınız'
*******************************
""")
while True:
    islem = input("İşlem Seçiniz :")
    if (islem == "q"):
        print("Program Sonlandırılıyor.")
        break
    elif (islem == "1"):
        kumanda.tv_ac()
    elif (islem == "2"):
        kumanda.tv_kapat()
    elif (islem == "3"):
        kumanda.ses()
    elif (islem == "4"):

        yeni_kanallar = input("Kanalları 'Virgül' ile ayırarak giriniz:")
        kanal_listesi = yeni_kanallar.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)




    elif (islem == "5"):
        print("Kanal Sayısı:",len(kumanda))

    elif (islem == "6"):
        kumanda.Kanal()
    elif (islem == "7"):
        print(kumanda)
    else:
        print("Geçersiz İşlem.")










