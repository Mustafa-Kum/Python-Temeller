## Useful Methods

# Range

print(range(20)) ## ---> 0'dan 20'ye gösterim. 20 dahil değil.
print(list(range(20)))
for number in list(range(20)): ## ---> Kolay yoldan tek kod ile liste içindeki herşey ile işlem yapma.
    print(number * 5)

my_list8 = range(5,20,3) ## ---> 3'er 3'er git.  
for number in my_list8:
    print(number)

my_list9 = list(range(0,10)) ## ---> 0 ile 10 aarsında liste oluşturdu. İstediğimiz zaman kullanabiliriz.
print(my_list9)

# Enumerate

for number in enumerate(list(range(5,15))): ### ---> Yanında index'ini gösterir. Yani listede kaçıncı sırada olduğunu.
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

# List advanced

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