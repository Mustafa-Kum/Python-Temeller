## For Loop

my_list6 = [1,2,3,4,5,6]
for number in my_list6: ## ---> My_list6'da ki elemanları al number diye bir değişkene ata.
    print(number)
for item in my_list6:
    new_number = item * 5
    print(new_number)
for number1 in my_list6:
    if number1 % 2 == 0: ## ---> Number1 diye bir değişken atadık her bir listenin karakterine. İçlerinden 2 ile tam bölünebilir olanları getirdi.
        print(number1)
my_string1 = "Mustafa Kum"
for letter in my_string1:
    print(letter)
for letter1 in my_string1:
    if letter1 == "a":
        print(letter1)

my_new_list = [("a","b"), ("c","d"), ("e","f"), ("g","h")]
for (x,y) in my_new_list:
    print((x,y)) ## ---> Düzenli bir listeden bahsediyorsak basit olarak bu yapılabilir. Karışık olmayan liste.
for (x,y) in my_new_list:
    print((x)) ## ---> Sadece x'leri aldı.
for (x,y) in my_new_list:
    print((y)) ## ---> Sadece y'leri aldı.

my_dict3 = {"key1": 100, "key2": 200, "key3": 300}
for (a,b) in my_dict3.items(): ## ---> Dictionary için a ve b'yi değişken atadık ve içindekileri a ve b ile ayrı ayrı görebildik.
    print(a)
    print(b)