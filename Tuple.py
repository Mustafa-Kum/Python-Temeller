## Tuple

my_tuple = ("a", 2, "b")
## my_tuple[0] = "b" ---> Immutable ---> Tuple'de listenin elemanlarını değiştiremezsin.
my_tuple.count("a")
print(my_tuple.count("a")) ## ---> İçinde kaç tane a değişkeni olduğunu sayıyor.
my_tuple2 = (1,1,1,1,2,3,4,5,6)
print(my_tuple2.count(1))
print(my_tuple2.index(2)) ## ---> Kaçıncı sırada olduğunu bulur değişkenin.