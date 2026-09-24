import os
os.system("cls")

import os
os.system("cls")

import json
import requests as rq

link = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

data = rq.get(link)
data = data.json()

print("<<<<<<<<<<<<Bankga xush kelibsz>>>>>>>>>>>")
while True:

        print("Valyutani tanlang ")


        for i in range(len(data)):
            print(f"{i } {data[i]['CcyNm_UZ']}: {data[i]['Rate']}")
        m=len(data)

        n=int(input(f"Qaysi valyuta bn ishlaysz(1 dan {m}gacha ):"))
        if n>=0 and n<len(data) :
            print(f"{data[n]['CcyNm_UZ']}: {data[n]['Rate']}")
            q=input(f"Amalyot {data[n]['CcyNm_UZ']}dan so'mgami?Ha/Yo'q.(if 'yoq' teskarisi)")
            if q=="Ha":
                som=int(input("miqdorni  kiriting:"))
                narx=som*float(data[n]['Rate'])         
                print(narx)
            elif q=="Yo'q":
                som2=int(input("Summani kiriting: "))
                narx2=som2/data[n]['Rate']
                print(narx2)
            else:
                print("Ha/Yo'q kiriting faqat ")
            
        else:
            print("xato kiritdingiz")

        d=input("Yana xizmatdan foydalanaszmi ha/yoq ")
        if d=='yoq':
             break
       




