import random
#doc7

#1
print (list(filter(lambda mod7And5InRange : mod7And5InRange % 7 ==0 and mod7And5InRange%5 ==0, range(1500, 2701))))

#2
cel, fan= 60.0, 45.0
toCel = lambda fanToCel : (fanToCel -32) * (5/9) 
toFan = lambda celToFan : celToFan * 1.8 + 32 
print(f"{cel} degrees Celsius is {toFan(cel)} degrees Farenheit\n{fan} degrees Farenheit is {toCel(fan):.2f} degrees Celsius")

#3
guess=0
nToGuess = random.randint(1,10)
while(guess!=nToGuess):
    guess=int(input("Guess a number between 1-9\n"))
else:
    print("Well guessed!")

#4


for whichHalf in range(1,3):
    if whichHalf==1:
        for i in range(1,5):
            print("*"*i)
    else:
        for j in range(4, 0,-1):
            print("*"*j)
#5
reverseUserWord = lambda word : word[::-1]
print(reverseUserWord(input("Enter any word to reverse: ")))

#6
number = (1 ,2 ,3, 4 , 5, 6,)
oddNums = list(filter(lambda even : even % 2 ==0, number))
evenNums= list(filter(lambda odd: odd % 2 ==1 , number))
print ( f"Number of evens: {len(evenNums)}\nNumber of odds: {len(oddNums)}" )


#7
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], { "class" : "V", "section": "A"}] 
print(' '.join(f"{el} {type(el)}" for el in datalist))

#8
n = -1
while(n!=7):
    n+=1
    if (n!=3 or n!=6):
        print(n, end=" ")
    else:
        continue

 
    
