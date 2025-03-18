print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
if size=='S':
    bill+=15
    if pepperoni=='y':
        bill+=2
    else:
        bill+=0
    if extra_cheese=='y':
        bill+=1
    else:
        bill+=0

if size=='M':
    bill+=20
    if pepperoni=='y':
        bill+=3
    else:
        bill+=0
    if extra_cheese=='y':
        bill+=1
    else:
        bill+=0

if size=='L':
    bill+=25
    if pepperoni=='y':
        bill+=3
    else:
        bill+=0
    if extra_cheese=='y':
        bill+=1
    else:
        bill+=0
print(bill)