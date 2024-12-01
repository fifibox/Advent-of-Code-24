# ---- Part 1 ----
# declare output variable
total = 0
lst1=[]
lst2=[]

input='''3   4
4   3
2   5
1   3
3   9
3   3'''

for line in input.split('\n'):
    num1,num2=line.split()
    lst1.append(int(num1))
    lst2.append(int(num2))
lst1.sort()
lst2.sort()
for i in range(len(lst1)):
    total += abs(lst1[i]-lst2[i])
print(total)

# ----Part 2 ----
# declare variable
score = 0
occurance = {}

for num1 in lst1:
    try:
        index = lst2.index(num1)
        occurance[num1] = 1
    except:
        occurance[num1] = 0
        continue
    for i in range (index+1,len(lst2)):
        if lst2[i] == num1:
            occurance[num1] +=1
        else:
            break
    score += num1 * occurance[num1]
print(score)
