## Lists

## ---> Immutabilty ---> String'in harflerini değiştiremezsin.
# my_string = "Mustafa"
# my_string[1] = "B" ---> My_string değişkenimin ikinci harfi (u) B olsun dedik fakat hata aldık.

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

## ---> Nested List ---> İç içe geçmiş liste. Liste içine liste koymak. 
new_list = [1,2,4,"a"]
new_list = [1,2,4,"a",[3,5]]
nested_list = new_list[4]
print(nested_list)
print(new_list[4][1])

## ---> Slicing
print(new_list[2:])
print(new_list[:2])