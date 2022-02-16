import random
reducedSet=[]
solutions=open('wordlist.txt')
for s in solutions:
    s=s[3:8]
    reducedSet.append(s)
eliminatedLetters=[]
lettersContain=[]
correctLetters={}
guessArray=[]
correct=True
u=0
def elimCheck(list, word):
    for w in list:
        if(w in word):
            return False
    return True
#add
solutions=open('wordlist.txt')
guess=" "
word=input("enter solution\n")#write
for count in range(6):
    guess=random.choice(reducedSet)
    #for char in eliminatedLetters:
     #   if(guess.__contains__(char)):
      #      correct=False
       #     break;
    while(guess==" " or guessArray.__contains__(guess)):
        guess=random.choice(reducedSet)
        #print(hex(id(guess)))
        #if(u==10):
         #   exit;
        #u=u+1
        #correct=True
        #for char in eliminatedLetters:
         #   if(guess.__contains__(char)):
          #      correct=False
           #     break;
    if(not guessArray.__contains__(guess)):
        guessArray.append(guess)
    print(guess)
    if(guess==word):
        print('Computer has won')
        exit();
    for i in range(5):
        if(word[i]==guess[i]):
            print(word[i], end="")
            correctLetters[i]=word[i]
        elif(word.__contains__(guess[i]) and not lettersContain.__contains__(guess[i])):
            lettersContain.append(guess[i])
            print("_", end="")
        elif(not word.__contains__(guess[i])): 
            print("_", end="")
            if(not eliminatedLetters.__contains__(guess[i])):
                eliminatedLetters.append(guess[i])
    print(lettersContain)
    for l in range(len(reducedSet)):
        for i in range(5):#filters correct letters and indices
            if(i in correctLetters):
                if(not reducedSet[l]==" " and not correctLetters[i] == reducedSet[l][i]):
                    reducedSet[l]=" "
                    break;
        for i in lettersContain:#filters letters that solution contains
            if (not reducedSet[l]==" " and not reducedSet[l].__contains__(i)):
                reducedSet[l]=" "
                break;
        if(not elimCheck(eliminatedLetters, reducedSet[l])):#eliminate words with eliminated letters
            reducedSet[l]= " "
#print(reducedSet)
sol=random.choice(reducedSet)
while(sol==" "):
    sol=random.choice(reducedSet)
if(sol==word):
    print("Computer has won")
else:
    print("Computer has lost. Answer was ")
    print(word)
#print(len(reducedSet))