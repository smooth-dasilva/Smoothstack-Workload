#doc8 

#1
def printHelloWorld():  print("Hello world")
printHelloWorld()

#2
def printName(name):  print(f"Hello, my name is {name}")
printName("Google")

#3
def printCondition(x, y, z):  
    if bool(z): 
        return x
    else:
        return y
ans=printCondition("This is true","This is false", [])
print(f"The choice is: {ans}")

#4
def retProd(x,y):  return x*y 
print(retProd(2,3))

#5
def checkParity(x):  
    return (True if x%2==0 else False)
print(checkParity(2))
#6
def checkLtGt(x, y):  
    return (x if x>y else y)
print(checkLtGt(2,3))

#7
def arbitraryParamSum(*a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum
print(arbitraryParamSum(1,2,3,4))

#8

def arbitraryList(*a):
    even = []
    for i in a:
        if i%2 ==0:
            even += [i]
    return even
print(arbitraryList(1,2,3,4))

#9
def conditionedString(x):
    st = ""
    position=0
    for char in x:
        if position%2 ==0:
            st+= char.upper()
        else:
            st+=char.lower()
        position+=1
    return st
print(conditionedString("This string has some ...strings... attached"))

#10
def conditionedNums(x,y):

    if x%2==0 and y%2==0 :
        return min(x,y)
    else:
        return max(x,y)
print(conditionedNums(2, 4))
#11
def checkFirstLetterEq(x, y):  
    return (True if x[0]==y[0] else False)
print(checkFirstLetterEq("Hello", "Horld"))

#12
def squareList(numbers): return [i*i for i in numbers] 
print(squareList([1,2,3,4,5]))




#13
def someUpperFun(x):
    st = ""
    position=0
    for char in x:
        if position==0 or position==4:
            st+= char.upper()
        else:
            st+=char
    return st
print(someUpperFun("let's have some fun"))

