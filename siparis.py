# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 02:36:49 2023

@author: TUNC
"""

class Siparis:

    def __init__(self, siparis_id, urun_id, adet, fiyat, uye_id, uye_tel, durum, kargo_id):
   
        self.siparis_id = siparis_id
        self.urun_id = urun_id
        self.adet = adet
        self.uye_id = uye_id
        self.uye_tel= uye_tel
        self.durum = durum
        self.kargo_id=kargo_id
        self.fiyat=fiyat
        
        

    def bilgileri_goster(self):
        print("Sipariş Bilgileri")  
        print("Üye ID:", self.uye_id)
        print("Sipariş ID:", self.siparis_id)
        print("Ürün ID:", self.urun_id)      
        print("Adet:", self.adet)
        print("Fiyat:", self.fiyat)      
        print("Üye Tel:", self.uye_tel)
        print("Durumu:", self.durum)
        print("Kargo ID:", self.kargo_id)
        

      

    def siparis_guncelle(self, yeni_adet):
        
        self.adet = yeni_adet
        print(self.uye_id, "ID'li üyenin sipariş adedi", yeni_adet,"adet olarak güncellendi.")
        
    def tel_guncelle(self, yeni_tel):
        self.uye_tel=yeni_tel
        print(self.uye_id, "ID'li üyenin telefon numarası", yeni_tel, "olarak güncellendi.")
         
   
siparis1=Siparis("3","999","110",2, 14.000, "05074563221", "Sipariş Hazırlanıyor.","22")
siparis2=Siparis("2","888","220",1, 7000, "05446589781", "Tedarik Aşamasında.","33")


siparis1.siparis_guncelle("5")
siparis2.tel_guncelle("05445978120")

siparis1.bilgileri_goster()
siparis2.bilgileri_goster()
