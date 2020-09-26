sayılar = []
i = 0
while i < 5:
    try:
        sayı = int(input("Bir sayı giriniz: "))
    except:
        print("Not Valid Input !!!")
    else:
        i += 1
        sayılar.append(sayı)
print(sayılar)
büyük = sayılar[0]
for i in range (1, len(sayılar)):
    if sayılar[i] > büyük:
        büyük = sayılar[i]
print(sayılar)
print("Girdiğiniz sayılardan en büyüğü : ", büyük)