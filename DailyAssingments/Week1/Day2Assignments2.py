

#doc4

#1.
print([1, 'Hello', 1.0])

#2
print([1, 1, [1,2]][2][1])

#3. out: 'b', 'c'
print(['a','b', 'c'][1:])

#4.
weekDict= {'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6, }

#5. out:  2 if you replace D[k1][1] with D['k1][1]
D={'k1':[1,2,3]}
print(D['k1'][1]) 

#6. 
tup = ( 'a',  [1,[2,3]] )
print(tup)

#7.
x= set('Missipi')
print(x)


#8
x.add('X')
print(x)

#9 out: [1, 2, ,3]
print(set([1,1,2,3]))

#10
for i in range(2000,3001):
    if (i%7==0) and (i%5!=0):
        print(i) 