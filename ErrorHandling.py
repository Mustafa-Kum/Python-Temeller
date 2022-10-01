## Error Handling

#def summation(number1, number2):
    #return number1 + number2

#x = input("Number1")
#y = input("Number2") ---> Bir tanesine sayı değilde string yazarsak program çöker onu ele alıcaz.

def numberpower(a,b):
    return a + b

print(numberpower(3,5)) ## ---> String yazarsak çöker.

# Try, Except, Finally

while True:

    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number2: "))

    except:
        print("Enter a number!!")
        continue ## ---> Hiçbir şey olmamış gibi başa dön.

    else:
        print("Ok")
        break
    
    finally:
        print("Finally") ## ---> Her zaman çalıştırılacaktır.