# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 03:56:19 2023

@author: TUNC
"""

class StokYonetimi:
     def __init__(self, urun_id, ad, stok_adet):
       self.urun_id = urun_id
       self.ad = ad
       self.stok_adet=stok_adet
   
     def stok_guncelle(self, yeni_stok):
       self.stok_adet=yeni_stok
       print(self.urun_id, "ID'li ürünün stok adedi", yeni_stok, "olarak güncellenmiştir.")
    
     def bilgileri_goster(self):
       print("Urun ID:", self.urun_id)
       print("Urun Ad:", self.ad)
       print("Stok Adeti:", self.stok_adet)   
       
       
       
        
       def urun_ekle(self, urun_id,ad,stok_adet):
           yeni_urun=StokYonetimi(urun_id, ad, stok_adet)
           self.StokYonetimi.append(yeni_urun)
        
       
        
       
urun1 = StokYonetimi("110", "Laptop", 500)
urun2 = StokYonetimi("220", "Akıllı Telefon",1000)
urun3 = StokYonetimi("330", "Kulaklık", 800)
urun4 = StokYonetimi("440", "Televizyon", 1000)
urun5 = StokYonetimi("550", "Elektrikli Süpürge", 700)
urun6 = StokYonetimi("660", "Televizyon", 700)
urun7 = StokYonetimi("770", "Ütü", 800)
urun8 = StokYonetimi("880", "Buzdolabı", 500)
urun9 = StokYonetimi("990", "Fırın", 500)
       
       
urun1.bilgileri_goster()
urun2.bilgileri_goster()
urun3.bilgileri_goster()
urun4.bilgileri_goster()
urun5.bilgileri_goster()
urun6.bilgileri_goster()
urun7.bilgileri_goster()
urun8.bilgileri_goster()
urun9.bilgileri_goster()
urun10 = StokYonetimi("1100", "Çamaşır Makinesi",500)
print(urun10.urun_id, "ID'li", urun10.ad, "ürünü eklenmiştir.")

urun8.stok_guncelle(750)
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
#     def urun_ekle(self, urun_id, urun_adi, adet):
#         self.stok[urun_adi] = miktar
#         print(f"{urun_adi} ürünü stoklara eklendi. Yeni Stok Miktarı: {self.stok[urun_adi]}")

#     def urun_cikar(self, urun_adi, miktar):
#         if urun_adi in self.stok and self.stok[urun_adi] >= miktar:
#             self.stok[urun_adi] -= miktar
#             print(f"{urun_adi} ürününden {miktar} adet satıldı. Yeni Stok Miktarı: {self.stok[urun_adi]}")
#         else:
#             print(f"Stokta yeterli {urun_adi} ürünü bulunmamaktadır.")

#     def stok_durumu_goster(self):
#         print("Stok Durumu:")
#         for urun_adi, miktar in self.stok.items():
#             print(f"{urun_adi}: {miktar} adet")

# # Kullanım Örneği
# stok_yonetimi = StokYonetimi()

# stok_yonetimi.urun_ekle("Laptop", 10)
# stok_yonetimi.urun_ekle("Telefon", 20)
# stok_yonetimi.urun_ekle("Tablet", 15)

# stok_yonetimi.stok_durumu_goster()

# stok_yonetimi.urun_cikar("Laptop", 5)
# stok_yonetimi.urun_cikar("Kamera", 3)

# stok_yonetimi.stok_durumu_goster()