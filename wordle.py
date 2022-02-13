reducedSet=[]
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
    if(count==1):
        solutions = open('wordlist.txt')
    else:
        solutions=reducedSet
    print(lettersContain)
    for l in solutions:
        l = l[3:8]
        for i in range(5):
            if(i in correctLetters and len(l)>i):
                if(not correctLetters[i] == l[i]):
                    correct=False
                    break;
        for i in range(len(lettersContain)):
            if (not l.__contains__(lettersContain[i])):
                correct = False
                break;
        if (correct and not reducedSet.__contains__(l)):
            reducedSet.append(l)
        correct=True
    print(reducedSet)
    #guess =input("enter guess")

print(correctLetters)
print(reducedSet)
print(len(reducedSet))
#print(guess)
#print(len(lettersContain))


