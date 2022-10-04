my_file = open("Myfile.txt")

print(my_file.read()) ## ---> txt'nin içinde ki yazanı okutur.

my_file.seek(0) ## ---> Sırayı başa getirir tekrar okuturken.

my_file.close() ## ---> Txt'yi kapatır yoksa kullanılıyor olur.

with open("Myfile.txt") as my_file:
    
    file_read = my_file.read()
    
print(file_read)

with open("Myfile.txt", mode = "w") as my_new_file2:
    
    my_new_file_write1 = my_new_file2.write("4")

with open("Myfile.txt", mode = "r") as my_new_file: ## ---> r -> Okumak için çalıştır. Sadece okuma izni. w -> Yazma izni a -> eklemek.

    my_new_file_read2 = my_new_file.read()

with open("Myfile.txt", mode = "a") as my_new_file3: ## ---> r -> Okumak için çalıştır. Sadece okuma izni. w -> Yazma izni a -> eklemek.

    my_new_file_read3 = my_new_file3.write("5")

with open("Myfile.txt", mode = "r") as my_new_file4: ## ---> r -> Okumak için çalıştır. Sadece okuma izni. w -> Yazma izni a -> eklemek.

    my_new_file_read4 = my_new_file4.read()

