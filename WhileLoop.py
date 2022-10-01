## While Loop

a = 0
while a < 5: ## ---> a 5'den küçük olduğu sürece a 5'den küçük yazdıracak.
    print("a 5'den küçük")
    a = a + 1

b = 0
while b < 5:
    if b == 3: ## ---> a 3'e eşit olduğu anda duracak.
        break
    print(b)
    b += 1

c = 0
while c < 20:
    #print("value of c :" + str(c)) ## ---> Çıktının içine value of c'yi yazdırıp yanına string'e çevrilmiş c değerini yazdırıyoruz.
    print(f"value of c : {c}") ## ---> Formanting ---> Başına f koyarak yukardakinin aynısını alabiliyoruz.
    c +=1
