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