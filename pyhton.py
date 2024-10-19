kingmoves=[[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]
def board(x,y):
    if 0<=x<8 and 0<=y<8:
        return True
import random as r
def game():
    k1x=r.randint(0,7)
    k1y=r.randint(0,7)
    k2x=r.randint(0,7)
    k2y=r.randint(0,7)
    motionk1=r.choice(kingmoves)
    posk1x=k1x+motionk1[0]
    posk1y=k1y+motionk1[1]
    motionk2=r.choice(kingmoves)
    posk2x=k2x+motionk2[0]
    posk2y=k2y+motionk2[1]
    steps=0
    while True:
        if board(posk1x,posk1y):
            k1x=posk1x
            k1y=posk2y
        steps+=1
        if abs(k1x-k2x)<=1 and abs(k2y-k1y)<=1:
            return steps
        if board(posk2x,posk2y):
            k2x=posk2x
            k2y=posk2y
        steps+=1
        return steps
def avgstep(totalgame):
    totalsteps=0
    for i in range(totalgame):
        totalsteps+=game()
    avg=(totalsteps/totalgame)
    return avg
avgstep(3)
        


