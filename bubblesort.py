ints=[]
bools=[]

num = int(input("number of digits: "))

for x in range(num):
    bools.append(False)

while len(ints)<num:
    num2 = int(input("add digit: "))
    ints.append(num2)

def bubbleSort(digits):
    while all(bools) != True:
        for i in range(len(digits)):
            if i == 0 and digits[i]>digits[i+1]:
                bools[i]= False
                digits[i], digits[i+1] = digits[i+1], digits[i]
            elif i == 0:
                bools[i] = True
            elif i < (len(digits)-1) and digits[i] > digits[i+1]:
                bools[i] = False
                digits[i], digits[i+1] = digits[i+1], digits[i]
            elif i < (len(digits)-1) and digits[i] <= digits[i+1] and digits[i] >= digits[i-1]:
                bools[i] = True
            else:
                bools[i]= True
    return(ints)


print("done", bubbleSort(ints))
