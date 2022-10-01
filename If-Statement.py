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