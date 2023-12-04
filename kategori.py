# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:05:44 2023

@author: TUNC
"""

class Kategori:
   def __init__(self,kategori_id, kategori_adi):
        self.kategori_id=kategori_id
        self.kategori_adi = kategori_adi
        


   def bilgileri_goster(self):
    print("Kategori ID:",self.kategori_id)
    print("Kategori Adı:",self.kategori_adi)
    



k1=Kategori("111","Ev Aletleri")
k2=Kategori("222","Beyaz Eşyalar")
k3=Kategori("333","Aksesuarlar")
k4=Kategori("444","Kişisel Bakım")
k5=Kategori("555","Isıtma&Soğutma")

k1.bilgileri_goster()
k2.bilgileri_goster()
k3.bilgileri_goster()
k4.bilgileri_goster()
k5.bilgileri_goster()




def kategori_ekle(self, kategori_adi):
    yeni_kategori = Kategori(kategori_adi)
    self.Kategori.append(yeni_kategori)
   
   
k6=Kategori("666", "Elektronik")
print(k6.kategori_id,"ID'li", k6.kategori_adi, "Kategorisi Eklendi.")

k7=Kategori("777", "Notebooklar")
print(k7.kategori_id,"ID'li", k6.kategori_adi, "Kategorisi Eklendi.")




