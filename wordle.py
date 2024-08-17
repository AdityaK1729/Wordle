def repcheck(guess,answer,x):
    curruptox=0
    curr=0
    for i in range(5):
        if guess[i]==answer[i] and guess[i]==guess[x]:
            curr+=1
            if i<=x:
                curruptox+=1
    return guess[:x].count(guess[x])-curruptox<answer.count(guess[x])-curr

import random
print('Welcome to Wordle!')
print('Guess the 5-letter word!')
print('ONLY USE UPPERCASE')
print('may the luck be with you')
print('You shall input your first guess now, all the best')
'''
words = [
    "TABLE", "OCEAN", "POWER", "MAGIC", "CRISP", "BLAZE", "DANCE", "QUICK", "FLARE", "STORM",
    "BRAVE", "LEARN", "BRUSH", "FLICK", "GRAPE", "CROWN", "FRESH", "GLOWN", "LEAFY", "SWEET",
    "FOCUS", "NOBLE", "LIMIT", "SHARP", "BLISS", "CLEAR", "GLEAM", "DRIVE", "DREAM", "PLATE",
    "BRISK", "BRAIN", "FROST", "BEAST", "STONE", "SHIFT", "FIELD", "FLUID", "CHARM", "SOLID",
    "PLUSH", "CRUSH", "LOFTY", "GUIDE", "GROVE", "GLINT", "FAITH", "BRISK", "RIVER", "CLOUD",
    "RUSTY", "GLARE", "SMILE", "STAGE", "WOVEN", "GRIND", "SCENE", "SNACK", "FLICK", "GRASP",
    "MIGHT", "LOOSE", "STILL", "BLANK", "PRIZE", "TRACE", "CLEAN", "FLAME", "GROWL", "BRINK",
    "EAGER", "LIGHT", "TREND", "FORGE", "PRIDE", "WISER", "FLOAT", "SCOPE", "BASIC", "CHASE",
    "GLORY", "STEEP", "CLOSE", "TRUST", "BLOOM", "SPARK", "BRAND", "SHINE", "FLEET", "SCARY",
    "SHOCK", "GUEST", "STAMP", "FRANK", "CRAFT", "SPICE", "LOVER", "SMOKE", "TOWER", "SMASH"
]
'''
read=open('validwords.txt','r')
words=read.read().split()
read.close()
read2=open('validguess.txt','r')
guesses=read2.read().split()
read2.close()
guesses={x.upper() for x in guesses}
words={x.upper() for x in words}
guesses=guesses.union(words)
answer=random.choice(list(words))
won=False
i=0
while i<6:
    res=[]
    guess=input()
    if len(guess)!=5:
        print('5 letter word only, try again')
        continue
    elif guess not in guesses:
        print('Guess not in the dictionary, try again')
        continue
    
    for x in range(5):
        if guess[x]==answer[x]:
            res.append('G')
        elif guess[x] in answer and repcheck(guess,answer,x):
            res.append('Y')
        else:
            res.append('R')
    mystr=''.join(res)
    print(mystr)
    if res==['G','G','G','G','G']:
        won=True
        print(f'You win in {i+1} guesses!',f'The word was {answer}',sep='\n')
        break
    i+=1
if not won:
    print('You lose, better luck next time!',f'The word was {answer}',sep='\n')