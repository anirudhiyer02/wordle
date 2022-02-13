reducedSet=[]
solutions=open('wordlist.txt')
for j in solutions:
    j=j[3:8]
    reducedSet.append(j)
#reducedSet.remove('which')
#print(reducedSet[0])
lettersContain=[]
correctLetters={}
correct=True
solutions=open('wordlist.txt')
word=input("enter solution\n")#write
#guess=input("enter guess\n")#think
for count in range(4):#CHANGE
    guess=input("enter guess\n")#think
    for i in range(5):
        if(word[i]==guess[i]):
            print(word[i], end="")
            correctLetters[i]=word[i]
            if(not lettersContain.__contains__(guess[i])):
                lettersContain.append(guess[i])
            #reducedSet.append(i)
        elif(word.__contains__(guess[i]) and not lettersContain.__contains__(guess[i])):
            lettersContain.append(guess[i])
            print("_", end="")
        else: 
            print("_", end="")
    #solutions=open('wordlist.txt') 
    print(lettersContain)
    #t=0
    for l in reducedSet:
        #if(count==0):
        #l = l[3:8]
        for i in range(5):
            if(i in correctLetters):
                if(not correctLetters[i] == l[i] and reducedSet.__contains__(l)):
                    reducedSet.remove(l)
                    break;
        for i in lettersContain:
            if (not l.__contains__(i) and reducedSet.__contains__(l)):
                reducedSet.remove(l)
                break;
    print(reducedSet)
    print(len(reducedSet))
    #guess =input("enter guess")
print(correctLetters)
print(reducedSet)
print(len(reducedSet))
#print(guess)
#print(len(lettersContain))


