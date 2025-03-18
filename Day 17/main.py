class user:
    def __init__(self,id,uname):
        self.id=id
        self.uname=uname
        print(f"uid:{self.id}")
    def get_fname(self):
        fname=input("enter:")
        print(f"{fname}")

u=user(9,"df")
print(u.uname)
u.get_fname()