import random

def getDiceNum():
    diceNum=random.randint(1,6)
    print('You throw {} this time.'.format(diceNum))
    return diceNum

if __name__=='__main__':
    for i in range(50):
        print(getDiceNum())