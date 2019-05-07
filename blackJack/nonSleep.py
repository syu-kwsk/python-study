import random
from time import sleep




dealCardSum = random.randrange(1, 14) #ランダムな一枚にしたい

game = 'start'

print('私のアップカードは', dealCardSum, 'です')

userCard1 = random.randrange(1, 14)
userCard2 = random.randrange(1, 14)

print('あなたの手札：', userCard1, userCard2, '\n')

userCardSum = userCard1 + userCard2

while game != 'finish': 
    userChoice = input('"stand"しますか？"hit"しますか？:')   
         
    if userChoice == "h" or userChoice == "hit":
         hitCard =  random.randrange(1, 14)
         print('\nヒットしたカードは', hitCard, 'でした' )
         userCardSum += hitCard
         print('現在の手札の合計は', userCardSum, 'です\n')
         
         if userCardSum >= 22:
             print('バーストですね. あなたの負けです')
             game = 'finish'
         
          
    elif userChoice == "s" or userChoice == "stand":
         print('スタンドします\n')

         if userCardSum >= 22:
             print('バーストですね. あなたの負けです')
             game = 'finish'
             break
         
         print('それで来ましたか. 私の番ですね\n')
         print('アップカードは', dealCardSum, 'でした')
    
         while True:
             dealHitNum = random.randrange(1, 14)
             dealCardSum += dealHitNum

             print('引きます')
             print(dealHitNum, 'でした')
             print('合計は', dealCardSum, 'です\n')
             
             if dealCardSum <= 16:
                 print('ヒットします')

             elif dealCardSum > 21:
                 print('バーストですね. あなたの勝ちです')
                 game = 'finish'
                 break
             else:
                 print('それではいきます')
                 print('私は　', dealCardSum, '　で、あなたは', userCardSum, '　です')
                 if dealCardSum < userCardSum:
                     if userCardSum == 21:
                         print('blackJack!!')
                     print('あなたの勝ちです')
                     game = 'finish'
                     break
                 elif dealCardSum >= userCardSum:
                     print('あなたの負けです')
                     game = 'finish'
                     break

    

    
    
    


