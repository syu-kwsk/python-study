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
         
    if userChoice == "h" or userChoice == "hit":
         hitCard =  random.randrange(1, 14)
         thinkingTimer(2)
         print('\nヒットしたカードは', hitCard, 'でした' )
         userCardSum += hitCard
         print('現在の手札の合計は', userCardSum, 'です\n')
          
    elif userChoice == "s" or userChoice == "stand":
         print('スタンドします\n')
         thinkingTimer(1)

         if userCardSum >= 22:
             thinkingTimer(1)
             print('バーストですね. あなたの負けです')
             break
         
         print('それで来ましたか. 私の番ですね\n')
         print('アップカードは', dealCardSum, 'でした')
         thinkingTimer(2)
    
         while True:
             dealHitNum = random.randrange(1, 14)
             dealCardSum += dealHitNum

             print('引きます')
             thinkingTimer(1)
             print(dealHitNum, 'でした')
             print('合計は', dealCardSum, 'です\n')
             thinkingTimer(2)

             if dealCardSum <= 16:
                 print('ヒットします')
                 thinkingTimer(1)

             elif dealCardSum > 21:
                 print('バーストですね. あなたの勝ちです')
                 thinkingTimer(1)
                 break
             else:
                 print('それではいきます')
                 thinkingTimer(1)
                 print('私は　', dealCardSum, '　で、あなたは', userCardSum, '　です')
                 thinkingTimer(1)
                 if dealCardSum < userCardSum:
                     print('あなたの勝ちです')
                     break
                 elif dealCardSum >= userCardSum:
                     print('あなたの負けです')
                     break	

    else:
        break

    
    
    


