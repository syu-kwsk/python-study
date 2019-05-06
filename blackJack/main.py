import random

upCardNum = random.randrange(1, 14) #ランダムな一枚にしたい


print('私のアップカードは', upCardNum, 'です')
userCard1 = random.randrange(1, 14)
userCard2 = random.randrange(1, 14) 
print('あなたの手札：', userCard1, userCard2)

userChoice = input('"stand"しますか？"hit"しますか？:')


