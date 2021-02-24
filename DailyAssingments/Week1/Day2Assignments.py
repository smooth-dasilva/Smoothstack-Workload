
########################

# doc2

#1. 
print("Hello World"[-3])

#2.a
print("thinker"[2:5])

#2.b Error. Variable h is not defined.
#3. Error. Variable s is not defined.

#4.

print(''.join(set('Missippi')))

#5.
ans=''
inp=int(input("Enter how many phrases you'd like to enter: "))
for i in range(inp):
    pali=input()
    pali = ''.join(pali.lower().split()) # remove white spaces and lowercase strings
    pali = ''.join(filter(str.isalpha, pali)) #remove non-alpha char
    
    if pali==pali[::-1]:
        ans+='Y '
    else:
        ans+='N ' 
print(ans)

########################
