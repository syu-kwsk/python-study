import random

upCardNum = random.randrange(1, 14) #ランダムな一枚にしたい


print('私のアップカードは', upCardNum, 'です')
userCard1 = random.randrange(1, 14)
userCard2 = random.randrange(1, 14) 
print('あなたの手札：', userCard1, userCard2, '\n')
userCardSum = userCard1 + userCard2
while True:    
    userChoice = input('"stand"しますか？"hit"しますか？:')

    if userChoice == "s" or userChoice == "stand":
        print('\n')
        break
    elif userChoice == "h" or userChoice == "hit":
        hitCard =  random.randrange(1, 14)
        print('\nヒットしたカードは', hitCard, 'でした' )
        userCardSum += hitCard
        print('現在の手札の合計は', userCardSum, 'です\n')
    
    
    


