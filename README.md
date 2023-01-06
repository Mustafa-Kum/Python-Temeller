# Python

```python

## Integer ( Tam Sayı )
print(5 + 6)

## Float ( Ondalık Sayı )
print(0.5 + 0.3)

x = 3

y = 5

print(x + y)


r = input("r: ") ## ---> Kullanıcıdan alınan veri. 

r = int(r) ## ---> Kullanıcıdan alınan veri sadece integer olacak.

print(r + y)

## Strings

z = "1234567890"

print(len(z)) ## ---> len(z) ---> Z string'inin uzunluğu

print(z)

print("Welcome \nThe \nMatrix") ## ---> \n Escape Character. New Line anlamına gelir. Bir satır alta yazdırır.

print("Welcome \tThe \tMatrix")  ## ---> \t Escape Character. Tab kadar boşluk bırakır.

## Indexing

print(z[0]) ## ---> z[0] ---> z Değişkenimde ki ilk harfi gösterir.

print(z[2:]) ## ---> z[2:] ---> z Değişkenimde ki ilk iki harfi alma diğerlerini göster. ---> Slicing denir.

print(z[:2]) ## ---> z[:2] ---> z Değişkenimde ki ilk iki harfi gösterir. ---> Stoping Index.

print(z[2:4]) ## ---> z[2:4] ---> z Değişkenimde ki ilk 4 harfi göster ama ilk ikisini alma.

print(z[::3]) ## ---> z[::3] ---> z Değikenimde ki harfleri 3'er 3'er atlar.

print(z[::-1]) ## ---> z[::-1] ---> z Değikenimi ters yazdır.

## String Methods

my_name = "mustafa"

---> Değişkenin yanına getirdiğimiz nokta o değişken ile yapabileceğimiz yada sorgulayabileceğimiz şeyleri gösterir.

print(my_name.capitalize()) ## ---> Capitalize ile baş harfini büyütür.

my_name_capitalized = my_name.capitalize() ## ---> Yeni bir değişken oluşturulup büyük harfi kaydetme.

print(my_name_capitalized) ## ---> Tüm değişkenlerin ilk harfi büyük olacak.

my_name2 = "Mustafa Kum"

print(my_name2.split()) ## ---> İçeride ki değişkenleri ayırır.

my_name2_split = my_name2.split() ## ---> Yeni değişken oluşturulup Split'i kaydetme.

print(my_name2_split) ## ---> Split aslında liste haline getiriyor ve 0 hiçbir şey yazmazsak tüm listeyi getiriyor. 

print(my_name2_split[0]) ## ---> Split aslında liste haline getiriyor ve 0 yazarak ilk kelimeyi getiriyoruz.

print(my_name2_split[1]) ## ---> Split aslında liste haline getiriyor ve 1 yazarak ilk kelimeyi getiriyoruz.

print(my_name2.upper()) ## ---> Upper tüm string'i büyük harf haline getirir.

my_surname = "Kum"

my_full_name  = my_name + my_surname ## ---> my_name ve my_surname değişkenlerini toplayabiliriz ama direkt olarak yan yana yazar.

print(my_full_name)

my_full_name = my_name + " " + my_surname ## ---> my_name ve my_surname değişkenlerini toplayabiliriz ama arada boşluk kullanarak yazar.

print(my_full_name)

## Lists

---> Immutabilty ---> String'in harflerini değiştiremezsin.

my_string = "Mustafa"

my_string[1] = "B" ---> My_string değişkenimin ikinci harfi (u) B olsun dedik fakat hata aldık.

my_list = [1,2,3]

print(my_list[0])

my_list[0] = 5

print(my_list[0]) ## ---> Mutable ---> Sayıların listler içerisinde ki değiştirilebilmesi.

my_list.append(7) ## ---> Append eklemek.

print(my_list)

print(my_list.pop()) ## ---> Listenin en son elemanını gösterdi ve listeden attı.

print(my_list)

my_list1 = [1,2,3]

my_list2 = [4,5,6]

my_list3 = my_list1 + my_list2 ## ---> Listeler toplanabilir. Tam sayılar ile çarpılabilir.

print(my_list3)

my_list1.reverse() ### ---> Reverse, listeyi ters çevirdi.

print(my_list1)

---> Nested List ---> İç içe geçmiş liste. Liste içine liste koymak. 

new_list = [1,2,4,"a"]

new_list = [1,2,4,"a",[3,5]]

nested_list = new_list[4]

print(nested_list)

print(new_list[4][1])

---> Slicing

print(new_list[2:])

print(new_list[:2])

## Dictionary

my_dictionary = {"key":"value"}

print(my_dictionary["key"])

my_fitness_dictionary = {"run":100, "swim":200}

print(my_fitness_dictionary["run"]) ### ---> Anahtar ve değeri eşitleme. Örnek = run çağırınca direkt olarak 100 sayısı gelecek.

my_dictionary1 = {"key1":100, "key2":[1,2,3], "key3":{"a":5}}

print(my_dictionary1.keys()) ### ---> Sözlükteki keyleri gösterir.

print(my_dictionary1["key3"])

print(my_dictionary1["key3"]["a"])

print(my_dictionary1.values()) ### ---> Sözlükteki değerleri gösterir.

my_dictionary1["key4"] = 5 ### ---> Sözlüğe yeni key eklemek.

print(my_dictionary1)

## Set

my_list_set = [1,2,3,1]

## ---> Casting ---> Çevirme... List - Set,, INT - FLOAT

my_list_set = set(my_list_set)

print(my_list_set)

my_set = set() ### ---> Normal olarak set'i tanımlarsak Dictionary olarak görür fakat bu şekilde tanımlarsak hep set olarak görecektir.

my_set.add(1) ### ---> Set olarak tanımlamazsan .add çıkmaz.

my_set.add(2)

print(my_set)

my_dict = dict() ### ---> Dictionary olarak da yapılabilir.

my_dict["key1"] = 1

print(my_dict)

my_list4 = list() ### ---> List için de yapılabilir.

my_list4.append(1)

print(my_list4)

## Tuple

my_tuple = ("a", 2, "b")

my_tuple[0] = "b" ---> Immutable ---> Tuple'de listenin elemanlarını değiştiremezsin.

my_tuple.count("a")

print(my_tuple.count("a")) ## ---> İçinde kaç tane a değişkeni olduğunu sayıyor.

my_tuple2 = (1,1,1,1,2,3,4,5,6)

print(my_tuple2.count(1))

print(my_tuple2.index(2)) ## ---> Kaçıncı sırada olduğunu bulur değişkenin.

## Boolean ---> Doğru yanlış cevabını veren operatör.

my_boolean = True

is_Dead = False

print(5>3) ## ---> Doğru olup olmadığını yazar.

a = 5

b = input("b: ")

b_int = int(b)

print(a > b_int)

## Comparison ---> Karşılaştırma. <=, >=, ==, !=, and, or, not

print(2 > 1 and 2 < 3) ## ---> And için ikiside doğru olması gerekiyor. True döner.

print(2 < 1 or 2 > 1) ## ---> Or iiçin bir tanesi doğru olması yeterli.

print(not 10 == 10) ## ---> Not direkt olumsuz. True ise False yapar.

## If Statements

if 3 > 2:
    print("3 is greater than 2")

q = 4

w = 5

if q < w:
    print("Q W'dan küçük") ## ---> Eğer q w'dan küçük ise Q W'dan küçük yazdır.

else:
    print("W Q'dan büyük") ## ---> Eğer w q'dan büyük ise W Q'dan büyük yazdır.

e = 4

r = 5

if e > r:
    print("E R'den büyük") ## ---> Eğer e r'den büyük ise E R'den büyük yazdır.
else:
    print("E R'den küçük") ## ---> Eğer e r'den küçük ise E R'den küçük yazdır.

t = 4

u = 4

if t > u:
    print("T U'dan büyük")

elif t == u:
    print("T ve U birbirine eşit") ## ---> if ve else'den başka diğer bir kontrol aracı.

else:
    print("Diğer durumlar.")


my_superhero = input("superhero: ") ## ---> Kullanıcıdan alınan input

if my_superhero == "IronMan":
    print("Iron Man is the best defender of Earth") ## ---> Iron Man girdiyse kullanıcı bunu yazdır.

elif my_superhero == "SuperMan":
    print("Iron Man is the best my man change it") ## ---> SuperMan girdiyse kullanıcı bunu yazdır.

else:
    print("Just Iron Man just") ## ---> SuperMan yada Iron Man girmediyse kullanıcı bunu yazdır.

c = 10

v = 20

m = 30

if c < 20 and v > m: ## ---> And operatöründe ikiside doğru olması lazım. Doğru olmadığı için elif kontrolüne geçti.
    print("IronMan")

elif v < m or c > m:
    print("Batman")

else:
    print("SuperMan")


isDeath = False

if isDeath:
    print("Character is Death") ## ---> Burada direkt True ise bunu yazdır anlamına gelir.

else:
    print("Character is not Death") ## ---> Burada direkt False ise bunu yazdır anlamına gelir.

if not isDeath:
    print("Character is not Death") ## ---> Direkt True sorgulamasını geçiyoruz not ile.

my_string = "Hello World"

if "Hello" in my_string: ## ---> My_String'in içinde Hello var mı ? Kontrolü
    print("True")

else:
    print("False")

my_list5 = [1,2,3,4,5]

if 2 in my_list5: ## ---> Liste içinde de istediğimiz şeyin bulunup bulunmadığı kontrol edilebilir.
    print("True")

else:
    print("False")

my_dict2 = {"key1":100, "key2":200 }

if 100 in my_dict2.values():
    print("True")

else:
    print("False")

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

## Continue Break Pass

my_list7 = [10,20,30,40,50,60]

for num in my_list7:
    if num == 30:
        break ## ---> 30'a geldiğin anda işlemi kes.
    print(num * 5)

for item in my_list7:
    if item == 30:
        continue ## ---> 30'a geldiği anda 30'dan sonrası için devam etti yani 40'dan
    elif item == 40:
        continue
    print(item)

for no in my_list7:
    pass ## ---> Bu işlemi geç anlamında. Hiçbir işlem yapma.

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

## Useful Methods

# Range

print(range(20)) ## ---> 0'dan 20'ye gösterim. 20 dahil değil.

print(list(range(20)))

for number in list(range(20)): ## ---> Kolay yoldan tek kod ile liste içindeki herşey ile işlem yapma.
    print(number * 5)

my_list8 = range(5,20,3) ##----> 3'er 3'er git.  

for number in my_list8:
    print(number)

my_list9 = list(range(0,10)) ## ---> 0 ile 10 aarsında liste oluşturdu. İstediğimiz zaman kullanabiliriz.

# Enumerate

for number in enumerate(list(range(5,15))): ## ---> Yanında index'ini gösterir. Yani listede kaçıncı sırada olduğunu.
    print(number)

for (index,number) in enumerate(list(range(5,15))):
    print(index)
    print(number)

# Random

from random import randint ## ---> Anaconda ile birlikte random kütüphanesinden randint sözlüğünü çektik. 

print(randint(0,1000)) ## ---> 0 ile 1000 arasında rastgele bir sayı verecek.

from random import shuffle ## ---> Karıştıma.

my_list10 = list(range(0,10))

shuffle(my_list10)

print(my_list10)

# Zip ---> Liste birleştirmek

sports_list = ["run", "swim", "basketball"]

calories_list = [100, 200, 300]

day_list = ["pazartesi", "salı", "çarşamba"]

new_list2 = list(zip(sports_list,calories_list,day_list))

print(new_list2)

for (x,y,z) in new_list2:
    print(x)

print(new_list2[0])

## List advanced

new_list3 = []

my_string2 = "IronMan"

for element in my_string2: ## ---> My_string2'de ki harfleri tek tek new_list3'e ekliyoruz.
    new_list3.append(element)

print(new_list3)

new_list4 = [Iron for Iron in my_string2] ## ---> Yukarıda ki işlemin aynısı.

print(new_list4)

new_list5 = [number2 for number2 in list(range(0,10))]

print(new_list5)

new_list6 = [number3*5 for number3 in list(range(0,10))]

print(new_list6)

## Methods And Fuctions

my_string3 = "Mustafa"

my_string3_upper = my_string3.upper() ## ---> Küçük Method örneği.

print(my_string3_upper)

def hello_world(): ## ---> Foksyonu tanımladın. Artık direkt olarak hello_world yazınca kullanabilirsin.
    print("hello")
    print("world")

hello_world() ## ---> Print yazmaya gerek yok direkt olarak döndürür.

# Input and Output

def IronMan(CivilWar): ## ---> CivilWar burada bir değişken olarak atandı. Yani input alıyor.
    print(CivilWar)

IronMan("Cap")

def TonyStark(CivilWar = "Cap"): ## ---> Default olarak Cap yazdırır parantezi boş bırakınca.
    print(CivilWar)

TonyStark()

TonyStark("IronMan") ## ---> Kendimizde buradan Input'u değiştirebiliriz.

def summ(number1,number2):
    number3 = number1 + number2
    print(number3)

summ(42,52)

def summation(num1,num2,num3):
    return num1 + num2 + num3 

summation(10,20,30)

my_result = summation(10,20,30)

print(my_result) ## ---> Değişkene de eşitleyebiliriz. Return yapmadan eşitleyemezsin.

def control_string(Marvel):
    if Marvel[0] == "t":
        print(Marvel.capitalize()) ## ---> Marvel değişkeninin ilk harfi t ise onu büyüt dedik.

control_string("tony")

def control_string(Marvel):
    print(Marvel.capitalize()) ## ---> Marvel değişkeninin ilk harfi t ise onu büyüt dedik.

control_string("cony")

# Arbitrary arguments & Key word arguments

def summation_2(*args): ## ---> * buraya ne yazarsam onu al demek.
    sum(args)
    print(args)

summation_2(10,20)

def example_fuction(**kwargs): ## ---> ** keyword'lü bir şekilde yansıttı.
    print(kwargs)

example_fuction(run=100, swim=200)

def summ2(*args):
    return sum(args)

summ2(30,20,50)

print(summ2(10,20,30)) ## ---> Toplamlarını görmek için print ile yazdırmak zorunda kaldık.

def example_fuct(**kwargs):
    if "Tony" in kwargs:
        print("Iron Man")
    
    else:
        print("Cap")

example_fuct(Tony = 1)

## Advenced Fuctions

def divide(number):
    return number / 2

my_list11 = [1,2,3,4,5,6,7,8,9]

my_new_list2 = []

for number in my_list11:
    my_new_list2.append(divide(number))

print(my_new_list2)

# Map

## ---> iterable, tek tek gezilebilen liste.

list(map(divide,my_list11)) ## ---> Foksyon ve listeyi birbirine uyarladı ve liste şeklinde çıktısını verdi.

print(list(map(divide,my_list11)))

def control_string2(string):
    return "Tony" in string

print(control_string2("Tony")) ## ---> Normalde sadece Foksyon ile dönmesi gerekirken print basmak zorunda kaldık.

my_artist_list = ["Tony", "Stark", "Steve", "Rogers"] ## ---> Koşula uyan ile işlem yapma.

print(list(map(control_string2,my_artist_list))) ## ---> Hepsine tek tek foksyonu uyguladı.

# Filter

list(filter(control_string2,my_artist_list))

print(list(filter(control_string2,my_artist_list))) ## ---> Koşullara uyandan yeni liste oluşturma.

# Lambda ---> Tek kullanımlık foksyonlar için

def multiply(number):
   return number * 3

print(multiply(5))

multiply2 = lambda number: number * 3

print(multiply2(5))

my_list12 = [1,2,3,4,5,6]

list(map(lambda num:num * 2, my_list12 ))

print(list(map(lambda num:num * 2, my_list12 )))

## Decorator

def func(new_func):
    print("Func started") 
    new_func() ## ---> İlk önce func ilk satırı çalıştı sonra new_func değişkeni çalıştı ve devam etti.
    print("Func ended")

def my_func():
    print("Hello World")

func(my_func)

def decorator_func(func):

    def wrapper_func():

        print("wrapper started")

        func()

        print("wrapper ended")
    
    return wrapper_func

def func_new():
    
    print("Hello World")

example_fuct2 = decorator_func(func_new) ## ---> Bunu.

@decorator_func ## ---> Üstte yaptığım işlemin direkt olarak entegre etti.

def func_new():
    
    print("Hello World")

func_new()

## OOP Classes

my_list13 = list() ## ---> Liste sınıfından bir obje oluşturmak instance. ## ---> attribute, . koydukttan sonraki özzellikler.

class MyMusician():
    
    job = "musician" ## ---> Buraya varsayılan olarak şeyler eklenebilir.
    
    def __init__(self,name,age): ## ---> MyMusician ek özellikler atamamızı sağladı. Attribute gibi.
        
        self.name_attribute = name
        
        self.age_attribute = age
    
    # Method

    def sing(self):
        print(f"We are the champions {self.age_attribute}")

my_musician = MyMusician("James", 50) ## ---> Yukarıda yaş ve isim attribute'unu atadık bu yüzden isim ve yaş yazdık.

print(my_musician.age_attribute) ## ---> Bu şekilde yaşını çağırırsak direkt olarak atadığımız yaşı verecek.

print(my_musician.name_attribute)

my_musician.name_attribute = "Lars" ## ---> İstediğimiz gibi değiştirebiliriz.

print(my_musician.name_attribute)

print(my_musician.sing())

class DogYear():

    year_factor = 7

    def __init__(self,age=0): ## ---> Default olarak istediğimiz şeyi gösterebiliriz.
        
        self.age = age
    
    def calculation(self):
        
        return self.age * self.year_factor ## ---> DogYear.year_factor olarak da çalışır.

my_dog = DogYear(5)

print(my_dog.age)

print(my_dog.calculation())

# Inheritance ---> Kısaca miras alma.

class Class1():

    def __init__(self):
        print("Class 1 created.")
    
    def method_1(self):
        print("Method 1")
    
    def method_2(self):
        print("Method 2")

my_instance = Class1()

my_instance.method_1()

my_instance.method_2()

class Class2(Class1): ## ---> Class1'i Class2'nin içerisinde sorunsuz şekilde kullanabiliriz.

    def __init__(self):
        Class1.__init__(self)
        print("Class 2 created.")

    def method_3(self):
        print("Method 3")

    def method_1(self):
        print("Method_1 overrided")

my_instance2 = Class2() ## ---> Kullandıktan sonra ikisini birden yazdıracaktır.

my_instance2.method_1() ## ---> Buradaki olay Class1'i Class2 için attiribute yapmış olduk.

my_instance2.method_3()

# Polymorphism ---> Aynı isimde ki methodları farklı sınıflara göre çalıştırma. 

class Apple():

    def __init__(self, name):
        self.name = name

    def information(self):
        return self.name + "100 calories"

class Banana():

    def __init__(self, name):
        self.name = name
    
    def information(self):
        return self.name + "200 calories"  

banana = Banana("banana")

apple = Apple("apple")

print(banana.information())

print(apple.information())

fruit_list = [banana, apple]

for fruit in fruit_list:
    print(fruit.information()) ## ---> Aynı isimde ki attribute'ları liste şeklinde aynı anda çalıştırılabilir.

def get_info(fruit):
    print(fruit.information())

get_info(apple)

get_info(banana)

## Speacial Methods

class Fruits():

    def __init__(self,name,calories):
        self.name = name
        self.calories = calories

    def __str__(self): ## ---> String'e çevirip print şeklinde yazdırır.
        return("Example")

my_fruit = Fruits("Banana", 300)

print(my_fruit) ## ---> My_fruit default olarak Example yazdırıyor.

class Fruits():

    def __init__(self,name,calories):
        self.name = name
        self.calories = calories

    def __str__(self): 
        return(f"{self.name} has {self.calories}") ## ---> Hangi name ve calories'i verdiysek öyle yazdırdı.

    def __len__(self):
        return self.calories

my_fruit = Fruits("Banana", 300)

print(my_fruit)

print(len(my_fruit))

## Error Handling

def summation(number1, number2):
    #return number1 + number2

x = input("Number1")

y = input("Number2") ---> Bir tanesine sayı değilde string yazarsak program çöker onu ele alıcaz.

def numberpower(a,b):
    return a + b

print(numberpower(3,5)) ## ---> String yazarsak çöker.

# Try, Except, Finally

while True:

    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number2: "))

    except:
        print("Enter a number!!")
        continue ## ---> Hiçbir şey olmamış gibi başa dön.

   else:
        print("Ok")
        break
    
    finally:
        print("Finally") ## ---> Her zaman çalıştırılacaktır.


## Modules Packages ---> pip install numpy . 

import numpy as np ## ---> Numpy'ı np adı olarak da kaydedilebilir.

grades = np.random.normal(80,30,15) ## ---> Ortalama 80, Standart Sapma 30, 15 Tane

print(np.mean(grades)) ## ---> Ortalamasını al.

my_file = open("Myfile.txt")

print(my_file.read()) ## ---> txt'nin içinde ki yazanı okutur.

my_file.seek(0) ## ---> Sırayı başa getirir tekrar okuturken.

my_file.close() ## ---> Txt'yi kapatır yoksa kullanılıyor olur.

with open("Myfile.txt") as my_file:
    
    file_read = my_file.read()
    
print(file_read)

with open("Myfile.txt", mode = "w") as my_new_file2:
    
    my_new_file_write1 = my_new_file2.write("4")

with open("Myfile.txt", mode = "r") as my_new_file: ## ---> r -> Okumak için çalıştır. Sadece okuma izni. w -> Yazma izni a -> eklemek.

    my_new_file_read2 = my_new_file.read()

with open("Myfile.txt", mode = "a") as my_new_file3: ## ---> r -> Okumak için çalıştır. Sadece okuma izni. w -> Yazma izni a -> eklemek.

    my_new_file_read3 = my_new_file3.write("5")

with open("Myfile.txt", mode = "r") as my_new_file4: ## ---> r -> Okumak için çalıştır. Sadece okuma izni. w -> Yazma izni a -> eklemek.

    my_new_file_read4 = my_new_file4.read()
    
```




