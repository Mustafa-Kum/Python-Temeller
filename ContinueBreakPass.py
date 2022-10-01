## Continue Break Pass

my_list7 = [10,20,30,40,50,60]
for num in my_list7:
    if num == 30:
        break ## ---> 30'a geldiğin anda işlemi kes.
    print(num * 5)
for item in my_list7:
    if item == 30:
        continue ## ---> 30'a geldiği anda 30'dan sonrası için devam etti yani 40'dan
    elif item == 40:
        continue
    print(item)
for no in my_list7:
    pass ## ---> Bu işlemi geç anlamında.