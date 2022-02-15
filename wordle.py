import random
reducedSet=[]
solutions=open('wordlist.txt')
for s in solutions:
    s=s[3:8]
    reducedSet.append(s)
lettersContain=[]
correctLetters={}
correct=True
solutions=open('wordlist.txt')
guess=" "
word=input("enter solution\n")#write
for count in range(6):
    guess=random.choice(reducedSet)
    while(guess==" "):
        guess=random.choice(reducedSet)
    print(guess)
    if(guess==word):
        print('You have won')
        exit();
    for i in range(5):
        if(word[i]==guess[i]):
            print(word[i], end="")
            correctLetters[i]=word[i]
        elif(word.__contains__(guess[i]) and not lettersContain.__contains__(guess[i])):
            lettersContain.append(guess[i])
            print("_", end="")
        else: 
            print("_", end="")
    print(lettersContain)
    for l in range(len(reducedSet)):
        for i in range(5):#filters correct lettersand indices
            if(i in correctLetters):
                if(not reducedSet[l]==" " and not correctLetters[i] == reducedSet[l][i]):
                    reducedSet[l]=" "
                    break;
        for i in lettersContain:#filters letters that solution contains
            if (not reducedSet[l]==" " and not reducedSet[l].__contains__(i)):
                reducedSet[l]=" "
                break;
sol=random.choice(reducedSet)
while(sol==" "):
    sol=random.choice(reducedSet)
print(sol)
