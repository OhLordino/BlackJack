import random
class Deck(object):
    count=0
    progress=[]
    def display_hands(self,deck,sets,lst,count,progress):
        num= random.choice(de)
        progress.append(num)
        a=int(count)
        b=(num)
        c=int(count)
        char=str(deck[str(num)])
        lst.append(char)
        while c is not 1:
            print("-----", end="")
            c-=1
        print("-----")
        i=0
        sum=0
        while i is not a:
            try:
                if int(progress[i]) in range(1,12):
                    sum+=int(progress[i])
                
        
            except:
                sum+=10
            print("|",lst[i], "|", end="")
            i+=1
        num=4
        print("")
        while a is not 1:
            print("-----", end="")
            a-=1
        print("-----")
        print("SUM IS",sum)
        
        return sum
        
    def __init__(self,deck,sets,lst,count,progress):
        n=3
    

de=[1,2,3,4,5,6,7,8,9,10,'K','Q','J']
customer = {'1':1, '2': 2, '3': 3, '4': 4, '5':5, '6':6, '7':7, '8': 8, '9':9 , '10': 10, 'J': 'J', 'K': 'K', 'Q':'Q'}
dealer={'1':'Ɩ', '2': 'Ƨ', '3': 'Ɛ', '4': 'ᔭ', '5':'S', '6':'9', '7':'L', '8': '8', '9':'6' , '10': '0Ɩ', 'J': 'ſ', 'K': 'ʞ', 'Q':'b'}
count=1
cl=[]
dl=[]
progress1=[]
progress2=[]
bet_amount=500
while count is not 7:
    num= random.choice(de)
    print("DEALER")
    deck = Deck(dealer,de,dl,count,progress2)
    dead=deck.display_hands(dealer,de,dl,count,progress2)
    print("YOU")
    deck = Deck(customer,de,cl,count,progress1)
    alive=deck.display_hands(customer,de,cl,count,progress1)
    char2=dealer[str(num)]
    if (int(alive)>21 and int(dead)<=21):
        print("The dealer wins!")
        print("You have lost", bet_amount)
        break
        
    elif (int(dead)>21 and int(alive)<=21):
        print("Congratulations, You have won", bet_amount)
        break
    elif (int(dead)>21 and int(alive)>21):
        print("You have both lost", bet_amount*2)
        break
    else:
        print("Do you want to continue?")
        choice=input("Yes or No?").upper()
        if choice=="YES":
            bet_amount+=500
        else: #I do not want to continue
            if(dead>alive):
                print("The dealer wins!")
                print("You have lost", bet_amount)
                break
            else:
                print("Congratulations! You have won", bet_amount)
                break
    count+=1

