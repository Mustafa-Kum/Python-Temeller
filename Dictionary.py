## Dictionary

my_dictionary = {"key":"value"}
print(my_dictionary["key"])
my_fitness_dictionary = {"run":100, "swim":200}
print(my_fitness_dictionary["run"]) ### ---> Anahtar ve değeri eşitleme. Örnek = run çağırınca direkt olarak 100 sayısı gelecek.
my_dictionary1 = {"key1":100, "key2":[1,2,3], "key3":{"a":5}}
print(my_dictionary1.keys()) ### ---> Sözlükteki keyleri gösterir.
print(my_dictionary1["key3"])
print(my_dictionary1["key3"]["a"])
print(my_dictionary1.values()) ### ---> Sözlükteki değerleri gösterir.
my_dictionary1["key4"] = 5 ### ---> Sözlüğe yeni key eklemek.
print(my_dictionary1)