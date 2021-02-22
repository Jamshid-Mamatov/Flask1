def my_decorate(func):

    def wrapper():
        print("11")
        func()
    
    return wrapper

@my_decorate

def hi():
    print("hi")

@my_decorate
def bye():
    print("bye")

bye()

hi()
# x=my_decorate(bye)
# x()