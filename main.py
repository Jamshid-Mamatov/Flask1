def cube(v):
    return v**3

def os(f,v):
    return f(v)

x=os(cube,3)
# print(x)
print(type(os))
