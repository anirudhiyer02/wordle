reducedSet=[]
lettersContain=[]
correctLetters={}
correct=True
solutions=open('wordlist.txt')
word=input("enter solution\n")#write
guess=input("enter guess\n")#think
for count in range(1):#CHANGE
    for i in range(5):
        if(word[i]==guess[i]):
            print(word[i], end="")
            correctLetters[i]=word[i]
            #reducedSet.append(i)
        elif(word.__contains__(guess[i]) and not lettersContain.__contains__(guess[i])):
            lettersContain.append(guess[i])
            print("_", end="")
        else: 
            print("_", end="")
    solutions = open('wordlist.txt')
    for l in solutions:
        l = l[3:8]
        for i in range(5):
            if(i in correctLetters):
                if(not correctLetters[i] == l[i]):
                    correct=False
        for i in range(len(lettersContain)):
            if (not l.__contains__(lettersContain[i])):
                correct = False
        if (correct and not reducedSet.__contains__(l)):
            reducedSet.append(l)
        correct=True

print("\n",len(reducedSet))
print(reducedSet)
#print(len(lettersContain))


