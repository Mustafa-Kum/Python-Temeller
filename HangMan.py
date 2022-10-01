Name = input("Name: ") ## ---> Kişiden input alıyoruz.

print("Hello", Name, "time to play hangman") ## ---> İnput aldıktan sonra yazılacak şey.

Guess = "IronMan"

Guess_string = "" ## ---> Daha sonra bunu Guess'e eşitlemek için boş değişken atıyoruz.

Lives = 10

while Lives > 0: ## ---> Lives 0'dan büyükken yapılacak şeyleri yazmaya başlıyoruz.
    
    character_left = 0 ## ---> Aldığımız harfler için atadığımız değişken bunu durmak ve oyunu kapatmak için kullanacağız.
    
    for character in Guess: ## ---> Harfleri alt alta yazdırdık.
        
        if character in Guess_string: ## ---> Harflerin kapalı gözükmesi için Guess_string'i kullandık.
            print(character)
        
        else:
            print("-")
            character_left += 1 ## ---> Her harf bilindiğinde Guess'in harf sayısına kadar +1 eklenecek.
    
    if character_left == 0: ## ---> Tüm harfler bittiğinde yani 0'a eşit olduğunda oyunu kapatacak.
        print("You Won Bro")
        break
    
    guess1 = input("Guess a word: ") ## ---> Kişiden aldığımız harfler.
    
    Guess_string += guess1 ## ---> Kişiden aldığımız harfler boş olan Guess_string'e eklenecek.
    
    if guess1 not in Guess: ## ---> guess1'de ki harf Guess'de yoksa Lives'dan 1 düş.
        Lives -= 1
        print("Wrong guess")
        print(f"You have {Lives} left")
        
        if Lives == 0: ## ---> Lives 0'a eşit olduğunda oyunu kapat.
            print("You died bro.")
