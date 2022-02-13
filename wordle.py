reducedSet = []
solutions = open('wordlist.txt','r')
for j in solutions:
    j = j[3:8]
    reducedSet.append(j)
for i in reducedSet:
   # i = i[3:8]
    if (not(i[0] == 't')):
        reducedSet.remove(i)
print(len(reducedSet))         
