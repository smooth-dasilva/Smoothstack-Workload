#1
import numpy as np
#2
print(np.zeros(10))
#3
print(np.ones(10))
#4
print(list(map(lambda OnesToFive: OnesToFive*5 , np.ones(10))))
#5
print(np.arange(10,51))
#6
print(list(filter( lambda OnlyEvens : OnlyEvens%2==0,np.arange(10,51)  )))
#7

#8
print(np.random.randint(0, 8, (3,3) ))
#9
print(np.random.rand(1))

