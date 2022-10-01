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

