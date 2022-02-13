<<<<<<< HEAD
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
=======
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
            #if(not lettersContain.__contains__(guess[i])):
                #lettersContain.append(guess[i])
            #reducedSet.append(i)
        elif(word.__contains__(guess[i]) and not lettersContain.__contains__(guess[i])):
            lettersContain.append(guess[i])
            print("_", end="")
        else: 
            print("_", end="")
    #solutions=open('wordlist.txt') 
    print(lettersContain)
    #t=0
    for l in range(len(reducedSet)):
        #if(count==0):
        #l = l[3:8]
        for i in range(5):
            if(i in correctLetters):
                if(not correctLetters[i] == reducedSet[l][i]):
                    reducedSet[l]=" "
                    
                    break;
        for i in lettersContain:
            if (not reducedSet[l].__contains__(i)):
                reducedSet[l]=" "
                break;
    print(reducedSet)
    print(len(reducedSet))
    #guess =input("enter guess")
print(correctLetters)
print(reducedSet)
print(len(reducedSet))
#print(guess)
#print(len(lettersContain))


>>>>>>> 17466507aad8d50824d3452fb8dfbe6e97dd6f87
