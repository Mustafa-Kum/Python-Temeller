## Advenced Fuctions

def divide(number):
    return number / 2
my_list11 = [1,2,3,4,5,6,7,8,9]
my_new_list2 = []
for number in my_list11:
    my_new_list2.append(divide(number))
print(my_new_list2)

# Map

## ---> iterable, tek tek gezilebilen liste.
list(map(divide,my_list11)) ## ---> Foksyon ve listeyi birbirine uyarladı ve liste şeklinde çıktısını verdi.
print(list(map(divide,my_list11)))

def control_string2(string):
    return "Tony" in string
print(control_string2("Tony")) ## ---> Normalde sadece Foksyon ile dönmesi gerekirken print basmak zorunda kaldık.

my_artist_list = ["Tony", "Stark", "Steve", "Rogers"] ## ---> Koşula uyan ile işlem yapma.
print(list(map(control_string2,my_artist_list))) ## ---> Hepsine tek tek foksyonu uyguladı.

# Filter

list(filter(control_string2,my_artist_list))
print(list(filter(control_string2,my_artist_list))) ## ---> Koşullara uyandan yeni liste oluşturma.

# Lambda ---> Tek kullanımlık foksyonlar için

def multiply(number):
   return number * 3
print(multiply(5))

multiply2 = lambda number: number * 3
print(multiply2(5))

my_list12 = [1,2,3,4,5,6]
list(map(lambda num:num * 2, my_list12 ))
print(list(map(lambda num:num * 2, my_list12 )))