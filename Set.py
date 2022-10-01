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