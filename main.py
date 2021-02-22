def richly_numbers(x):
    return x*(x%2)

lst=[1,5,8,6,2,55,3,96,56]

max_num=max(lst,key=richly_numbers)
print(max_num)
