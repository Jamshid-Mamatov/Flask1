def my_decorate(func):

    def wrapper():
        print("11")
        func()
    
    return wrapper

def hi():
    print("hi")

def bye():
    print("bye")

x=my_decorate(bye)
x()