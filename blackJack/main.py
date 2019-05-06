import random
from time import sleep

def thinkingTimer(time):
    print('. . .\n')
    sleep(time)


dealCardSum = random.randrange(1, 14) #ランダムな一枚にしたい



print('私のアップカードは', dealCardSum, 'です')

userCard1 = random.randrange(1, 14)
userCard2 = random.randrange(1, 14)

print('あなたの手札：', userCard1, userCard2, '\n')

userCardSum = userCard1 + userCard2

while True:    
    userChoice = input('"stand"しますか？"hit"しますか？:')
    thinkingTimer(2)

    if userChoice == "s" or userChoice == "stand":
         print('スタンドします\n')
         break
    elif userChoice == "h" or userChoice == "hit":
         hitCard =  random.randrange(1, 14)
         print('\nヒットしたカードは', hitCard, 'でした' )
         userCardSum += hitCard
         print('現在の手札の合計は', userCardSum, 'です\n')

if userCardSum >= 22:
    print('バーストですね. あなたの負け確定です')

else:
    print('それで来ましたか. 私の番ですね\n')
    thinkingTimer(2)
    
    while True:
         dealHitNum = random.randrange(1, 14)
         dealCardSum += dealHitNum

         print(dealHitNum, 'でした')
         print('合計は', dealCardSum, 'です\n')
         thinkingTimer(2)
         
         if dealCardSum <= 16:
             print('ヒットします')
         elif dealCardSum > 21:
             print('バーストですね')
             break
         else:
             print('それではいきます')
             print('')
             if dealCardSum < userCardSum:
                 print('あなたの勝ちです')
                 break
             elif dealCardSum >= userCardSum:
                 print('あなたの負けです')
                 break
    
    
    


