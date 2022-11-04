#!/usr/bin/env python
# coding: utf-8

# In[4]:


sayi1=1
cift_toplam=0
tek_toplam=0
sayi2=int(input("Sayı giriniz:"))
while sayi1<=sayi2:
    if sayi1%2==0:
        cift_toplam+=(sayi1**3)
    else:
        tek_toplam+=(sayi1**2)
    sayi1+=1
print(f"Çift sayıların küpünün toplamı:{cift_toplam}")
print(f"Tek sayıların karesinin toplamı{tek_toplam}")

