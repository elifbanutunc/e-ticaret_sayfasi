# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 02:20:48 2023

@author: TUNC
"""

class Kargo:
    
    def __init__(self, kargo_id, kargo_ad, alici, gonderici,durum):
 
        self.kargo_id = kargo_id
        self.kargo_ad = kargo_ad
        self.alici = alici
        self.gonderici = gonderici
        self.durum = durum
       

    def bilgileri_goster(self):
        
        print("Kargo ID:", self.kargo_id)
        print("Kargo Adı:", self.kargo_ad)
        print("Alıcı:", self.alici)
        print("Gönderici:",self.gonderici)
        print("Durumu:", self.durum)
        
        #gıncelleme
kargo1=Kargo(22, "ABC Kargo", "Ahmet Demir", "Çiçek Mağazası","Hazırlanma Aşamasında")
kargo2=Kargo(33, "Hızlı Kargo", "Ayşe Yılmaz", "Elektronik Mağazası","Adrese Teslim")
kargo3=Kargo(44, "Hızlı Kargo", "Mehmet Kara", "Elektronik Mağazası","Teslim Edildi")

kargo1.bilgileri_goster()
kargo2.bilgileri_goster()
kargo3.bilgileri_goster()
