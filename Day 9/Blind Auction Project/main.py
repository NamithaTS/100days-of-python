# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
d={}
c=True
while(c):
    name=input("enter ur name:")
    bid=int(input("enter ur amt:"))
    d[name]=bid
    y=input("enter yes or no").lower()
    if y=="yes":
        print("\n" * 20)

    else:
        c=False
        m=0
        for key in d:
            if d[key]>m:
                m=d[key]
                w=key
                print(f"winner is {w} with bid {m}")



