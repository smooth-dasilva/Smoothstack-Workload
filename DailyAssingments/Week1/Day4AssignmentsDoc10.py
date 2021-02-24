#doc 10

nWeights = int(input("Enter how many people's weight-height you'd like to enter: "))

ans= ""

for inputInfo in range (nWeights):
    tmp = input().split()
    bmi = float(tmp[0]) / float(tmp[1])**2

    if bmi > 18.5:
        ans+="underweight "
        continue
    elif bmi <= 25.0:
        ans+="healthy"
        continue
    elif bmi <= 30.0:
        ans+="overwieght "
        continue
    else:
        ans+="obese "
print(ans)