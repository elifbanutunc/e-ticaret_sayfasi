# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 01:55:14 2023

@author: TUNC
"""

class Urun:
    def __init__(self, urun_id, ad, fiyat, stok_adet):
        self.urun_id = urun_id
        self.ad = ad
        self.fiyat = fiyat
        self.stok_adet = stok_adet

    def bilgileri_goster(self):
        print("Ürün ID:",self.urun_id)
        print("Ürün Adı:",self.ad)
        print("Fiyatı:",self.fiyat)
        print("Stok Adeti:",self.stok_adet)
        
        urunler = []

        def urun_ekle(urun_id, ad, fiyat, stok_adet):
            yeni_urun = Urun(urun_id, ad, fiyat, stok_adet)
            urunler.append(yeni_urun)
            print(ad, "ürünü eklendi.")


        urun_ekle(440,"Televizyon", 40000, 1000)
        urun_ekle(550,"Elektrikli Süpürge", 3000, 2000)
        
        
       

 
    def fiyat_guncelle(self, yeni_fiyat):
        self.fiyat = yeni_fiyat
        print("1 ID'li ürünün fiyatı,", yeni_fiyat, "TL olarak güncellendi.")

    def stok_guncelle(self, yeni_stok):
        self.stok_adet = yeni_stok
        print("2 ID'li ürünün stok adedi,", yeni_stok, "adet olarak güncellendi.")


# Kullanım örneği
urun1 = Urun(110, "Laptop", 14000, 50)
urun2 = Urun(220, "Akıllı Telefon", 7000, 100)
urun3 = Urun(330, "Kulaklık", 7000, 200)

# Ürün bilgilerini gösterme
urun1.bilgileri_goster()
urun2.bilgileri_goster()
urun3.bilgileri_goster()

# Ürün fiyatını güncelleme
urun1.fiyat_guncelle(15000)
urun1.bilgileri_goster()

# Ürün stok adedini güncelleme
urun2.stok_guncelle(200)
urun2.bilgileri_goster()


