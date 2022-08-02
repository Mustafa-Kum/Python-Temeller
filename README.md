# Python

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

## ---> Değişkenin yanına getirdiğimiz nokta o değişken ile yapabileceğimiz yada sorgulayabileceğimiz şeyleri gösterir.

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
