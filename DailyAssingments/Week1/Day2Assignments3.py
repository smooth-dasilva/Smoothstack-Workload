#There is a crowd part 1:
print("Begin part 1: \n")
def crowd_test1(l):
    if len(l)>2:
        print("The room's crowded...")
mobPeeps = ["George", "Howard", "Bulma","Albert", "Eleanor","Erik"]
peeps = ["George", "Howard", "Bulma","Albert"]
lessPeeps = ["George", "Howard"]

crowd_test1(peeps)
crowd_test1(lessPeeps)

#There is a crowd part 2:
print("Begin part 2: \n ")

def crowd_test2(l):
    if len(l)>2:
        print("The room's crowded...")
    else:
        print("Not very crowded")

crowd_test2(peeps)
crowd_test2(lessPeeps)


#Six is a mob:
print("Begin six is a mob: \n ")

def crowd_test3(l):
    if len(l)<3:
        print("Not very crowded")
    elif len(l)<6:
        print("The room's crowded...")
    else:
        print("There's a mob!")
peeps = ["George", "Howard", "Bulma","Albert"]
lessPeeps = ["George", "Howard"]

crowd_test3(peeps)
crowd_test3(lessPeeps)
crowd_test3(mobPeeps)

