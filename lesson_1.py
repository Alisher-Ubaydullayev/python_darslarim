#kun = input("Bugun kun nima? ")
#if kun.lower()=='shanba'or kun.lower()=='yakshanba':
#    print("bugun dam olsh kuni")
#else:
#    print("bugun ish kuni")

#kun = input("bugun kun nima? ")
#havo = int(input("havo harorati necha gradus? "))
#
#if kun.lower()=='shanba' or kun.lower()=='yakshanba' and havo<= 30:
#    print('chomilishga boramiz')
#else:
#    print('bugun uyda dam olamiz')

#narx = 15000
#choy = 0
#salat = 1
#if choy and salat:
#   narx = narx+ 5000
#elif choy or salat:
#    narx = narx+10000

#print(f"jami {narx} so'm bo'ldi")

#sant = {'atvot':'20 lik' ,'troynik':"25lik", 'ushka':"25/15tashqi", 'mufta':"32lik"}

#print(sant['mufta'])
#print(sant['atvot'])

#ishchi = {
#    'ism':"ali ubaydullayev",
#    't_yil':1997,
#    'yosh': 27
#}
#print(f"{hodim ['ism'].t}")

#son = float(input("Juft son kiriting: "))
#if son%2 !=0:
#    print("Bu son juft emas.")
#else:
#    print("Rahmat!")




#yosh = int(input("Yoshingiz nechida?"))

#if yosh<=4 or yosh>=60:
#    narh = 0
#elif yosh < 18:
#    narh = 10000
#else:
#    narh = 20000
#    print(f"Chipta {narh} so'm")

#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat=[]
#
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
#if savat:
#    for mahsulot in savat:
#        if mahsulot in mahsulotlar:
#            print(f"Do'konimizda {mahsulot} bor")
#        else:
#            print(f"Do'konimizda {mahsulot} yo'q")
#else:
#    print("Savatingiz bo'sh")

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
#
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)
#
#if mavjud_emas:
#  print("Do'konimizda quyidagi mahsulotlar yo'q:")
#for mahsulot in mavjud_emas:
#  print(mahsulot)
#else:
#  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

#users = ['alisher1983','aziza','yasina' 'umar']

#login = input("Yangi login tanlang:" )

#if login in users:
#    print('Login band, yangi login tanalng!')
#else:
#    print("Xush kelibsiz!")


#import requests
#from pprint import pprint as print


#API_KEY = '8954f20edb4ccce176fa409b'

#currensy = 'USD'
#url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currensy}/UZS'

#r = requests.get(url)
#print(r.status_code)
#res = r.json
#kurs = r.json()['conversion_rate']
#butun = int(kurs)
#print(f"Bugungi kurs: {butun} so'm")


#oyat = 2
#sura = 8
#tafsir = 'uzb-muhammadsodikmu'

 
#url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json"
#url_oyat = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"

#r = requests.get(url_oyat)
#print(r.status_code)
#res = r.json()
#print(res)


#from pprint import pprint as print


#app_id = "92cc5baf"
#app_key = "8ed5d225ffe547a3c1ac5cbfdd088d5a"
#language = "en-gb"


#word_id = "apple"
#url = f"https://od-api-sandbox.oxforddictionaries.com:443/api/v2/entries/{language}/{word_id.lower()}"

#r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

#print(r.status_code)
#res = r.json()
#print(r)

#talaba = {
#    'ism': 'alijon',
#    'familia': 'shmamsiyev',
#    'yosh':  22,
#    'fakultitet': 'matematika',
#    'kurs':  4
#}
#print(f"bu lug'atning uzunligi {len(talaba)} ta")

#for kalit, qiymat in talaba.items():
#    print(f"kalit: {kalit}")
#    print(f"qiymat: {qiymat}")

#car ={

#}

#a = str(input("mashinangiz markasini yozing: "))
#b = str(input("mashina rangini kiriting: "))
#c = int(input('mashina narxini yozing: '))

#car['marka']= a
#car['rang']= b
#car['narx']= c

#for k, v in car.items():
#    print(f'Mashinaning {k}si {v}')


telefonlar = {
    'olim': 'galaxys9',
    'sardor':'iphone X',
    'aliy': 'galaxys9'
            '',
    'sherzod': 'nokia 3310'
}

#for k, q in telefonlar.items():
#    print(f'{k.title()} ning telefoni {q}')
maxsulotlar = {
    'anor': '20000',
    'olma': '25000',
    'uzum': '14000',
    'sabzi': '5000'
}
#print(maxsulotlar.keys())


#print('Dokondagi maxsulotlar: ')

#for maxsulot in maxsulotlar.keys():
#    print(maxsulot.title())
#print(maxsulotlar.values())

#for tel in telefonlar.values():
#    print(tel)

lugat = {
    'int': 'butun son',
    'float': 'kasir son',
    'keys': 'kalitlar',
    'value': 'qiymat'
}
#for k, q in sorted(lugat.items()):
#    print(f"{k.title()}   {q.title()}")

davlatlar = {
    'ozbekiston': 'toshkent',
    'rossia': 'moskva',
    'turkia': 'istanbul',
    'falastin': 'quddus',
    'qozogiston': 'almata'
}
#for kalit, qiymat in sorted(davlatlar.items()):
#    print(f"{kalit.title()}ning poytaxti {qiymat.title()}")

menu = {
    "vaju": 15000,
    "mastava": 10000,
    "tushonka": 40000,
    "osh": 12000,
    "kabob": 18000,
    "lagmon": 23000,
    "manti": 5000,
    "salat": 7000,
    "choy": 3000

}

#klent =  str(input("istalgan taomni kiriting: "))

#for taom, narx in menu:
#    if klent not in menu:
#        print("Bizda bunday taom yo'q")
#    print(f"{taom} narxi {narx}")

#print("istalgan 3ta taomni kiriting")

#buyurtmalar =[]

#for b in range(3):
#    buyurtmalar.append(input(f"{b+1} - taom: ").lower())
#for buyurtma in buyurtmalar:
#    if buyurtma in menu:
#        print(f"{buyurtma.title()} {menu[buyurtma]} som")
#    else:
#        print(f"kechirasz bizda {buyurtma} yo'q")

#print("Istalgan 3 ta davlatni kiriting")

#sayohatlar = []

#for s in range(3):
#    sayohatlar.append(input(f"{s+1} - davlat: ").lower())
#for sayohat in sayohatlar:
#    if sayohat in davlatlar:
#        print(f"{sayohat.title()} ning poytaxti {davlatlar[sayohat]} bo'ladi")
#    else:
#        print(f" bizning tourda {sayohat} yo'q")


dokon ={
    'atvot': 2000,
    'poltvot': 5000,
    'troynik': 8000,
    'mufta': 1000,
    'adaptor': 20000,
    'ushka': 18000,
    'dushavoy': 100100,
    'mator': 200200
}

spiskalar = []

print("sizga nima masulot kerak: ")

for m in range(5):
    spiskalar.append(input(f"{m+1} - maxsulot: ").lower())

for spiska in spiskalar:
    if spiska in dokon:
         print(f"{spiska.title()} ning narxi {dokon[spiska]}som")
    else:
         print(f" bizda bunday {spiska}  yo'q")


print("haridingiz uchun raxmat")