## Decorator

def func(new_func):
    print("Func started") 
    new_func() ## ---> İlk önce func ilk satırı çalıştı sonra new_func değişkeni çalıştı ve devam etti.
    print("Func ended")
def my_func():
    print("Hello World")
func(my_func)

def decorator_func(func):

    def wrapper_func():

        print("wrapper started")

        func()

        print("wrapper ended")
    
    return wrapper_func

def func_new():
    
    print("Hello World")

example_fuct2 = decorator_func(func_new) ## ---> Bunu.

@decorator_func ## ---> Üstte yaptığım işlemin direkt olarak entegre etti.
def func_new():
    
    print("Hello World")

func_new()