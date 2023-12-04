# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 01:33:33 2023

@author: TUNC
"""
class Uye:
    def __init__(self, uye_id, ad, soyad, adres, tel, eposta):
        self.uye_id = uye_id
        self.ad = ad
        self.soyad = soyad
        self.adres=adres
        self.tel=tel
        self.eposta=eposta

    def bilgileri_goster(self):
        print("ID:",self.uye_id)
        print("Ad:",self.ad)
        print("Soyad:",self.soyad)    
        print("Adres:",self.adres)
        print("Telefon:",self.tel)
        print("E-Posta:",self.eposta)
        

    def adres_degistir(self, yeni_adres):
        self.adres = yeni_adres
        print(self.uye_id, "ID'li üyenin adresi", yeni_adres,"olarak güncellendi.")
        
    def tel_guncelle(self, yeni_tel):
        self.tel=yeni_tel
        print(self.uye_id, "ID'li üyenin telefonu", yeni_tel, "olarak güncellendi.")
        
    def eposta_guncelle(self, yeni_posta):
        self.eposta=yeni_posta
        print(self.uye_id, "ID'li üyenin e-posta adresi", yeni_posta, "olarak güncellendi.")
        
    

  
        
uye1 = Uye(1, "Ahmet", "Demir", "Ankara", "05078789541", "ahmetdemir@gmail.com")
uye2 = Uye(2, "Ayşe", "Yılmaz", "İstanbul", "05078975412", "ayseyilmaz@gmail.com")
uye3 = Uye(3, "Mehmet", "Kara", "İzmir", "05445891230","mehmetkara@gmail.com")


uye1.bilgileri_goster()
uye2.bilgileri_goster()
uye3.bilgileri_goster()


uye1.adres_degistir("İzmir")
uye1.bilgileri_goster()


uye2.tel_guncelle("05541236581")
uye2.bilgileri_goster()


uye3.eposta_guncelle("mehmetkara11@gmail.com")
uye3.bilgileri_goster()