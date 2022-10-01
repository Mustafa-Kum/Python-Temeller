def calculator(x, y, ops):
    
    if ops == "+": ## ---> if not in "+-*/" ---> Direkt bu kod ile kontrol edilebilirdi.
       
        return(str(x) + " " + ops + " " + str(y) + " " + "=" + " " + str(x+y))
    
    elif ops == "-":
        
        return(str(x) + " " + ops + " " + str(y) + " " + "=" + " " + str(x-y))

    elif ops == "/":
        
        return(str(x) + " " + ops + " " + str(y) + " " + "=" + " " + str(x/y)) 

    elif ops == "*":
        
        return(str(x) + " " + ops + " " + str(y) + " " + "=" + " " + str(x*y))       
    
    else:
        
        print("Please type one these items +, -, *, /")

while True:

    x = int(input("Please type the first number: "))
    
    y = int(input("Please type the second number: "))
    
    ops = input("Choose between +, -, /, * ")

    print(calculator(x,y,ops))

