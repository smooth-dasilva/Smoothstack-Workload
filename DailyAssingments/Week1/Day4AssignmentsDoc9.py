#doc 8

#1
bookShopAccounting = [ 
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Barry", 3, 32.95] ,
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
] 
#2.
ordersTuple =  tuple(map(lambda listEl : ((listEl[0],   listEl[2]*listEl[3])), bookShopAccounting))
updateList = []
ind = 0

for listEl in bookShopAccounting:
    if ordersTuple[ind][1]<100:    
        updateList+= [listEl[0], listEl[1], listEl[2]+10, listEl[3]]  
    else:
        updateList+= [listEl[0], listEl[1], listEl[2]+10, listEl[3]]
    ind+=1

print(list(ordersTuple))
print(updateList)

#3. 
bookShopAccounting2 = [ 
    [34587, (1, 4, 40.95)],
    [98762, (2, 5, 56.80)],
    [77226, (3, 3, 32.95)] ,
    [88112, (4, 3, 24.99)]
] 

ordersTuple2 =  tuple(map(lambda listEl : ((listEl[0],   listEl[1][1]*listEl[1][2])), bookShopAccounting2))
print(list(ordersTuple2))