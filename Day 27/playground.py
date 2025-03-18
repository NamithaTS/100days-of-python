def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum
print(add(3,4,5,8,9))

def cal(**kwargs):
    for key,value in kwargs.items():
       print(key)

cal(add=4,mul=5)