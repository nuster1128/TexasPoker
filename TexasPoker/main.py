from TexasPoker import TexasPoker
from Agent import Agent
from utils import CardPool

import time

if __name__ == '__main__':
    agentList=[Agent(str(i)) for i in range(6)]

    texasPoker=TexasPoker(agentList,debug=False)

    epi=30000000
    printEpi=100000
    totalRewardList=[0 for i in range(6)]
    startTime=time.time()
    for i in range(epi):
        rewardList=texasPoker.game()

        for j in range(6):
            totalRewardList[j]+=rewardList[j]

        if i % printEpi == 0 and i != 0:
            avgRewardList=[r/i for r in totalRewardList]
            endTime=time.time()
            print('Epoch',i,avgRewardList,endTime-startTime,'secs')



