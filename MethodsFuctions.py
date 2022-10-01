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