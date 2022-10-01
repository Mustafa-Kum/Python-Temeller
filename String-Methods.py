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