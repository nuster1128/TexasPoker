from Agent import Agent
from utils import *
import numpy as np

class TexasPoker():
    def __init__(self,agentList,debug=True):
        self.agentList=agentList
        self.debug=debug

        self.cardPool=CardPool()
        self.publicList=None
        self.scorePool=0
        self.DPosition=None
        self.roundScoreList=[0 for i in range(6)]
        self.foldNum=0
        self.agentCompetList=[]
        self.foldWinner=None

    def game(self):
        self.reset()
        self.prepare()
        self.round1()
        self.round2()
        self.round3()
        self.round4()
        return self.win()

    def reset(self):
        self.cardPool.reset()
        self.publicList=None
        self.scorePool=0
        self.DPosition=None
        self.roundScoreList = [0 for i in range(6)]
        self.foldNum=0
        self.agentCompetList=[]
        self.foldWinner=None
        for agent in self.agentList:
            agent.reset()

    def prepare(self):
        Dposition=random.randint(0,5)
        self.DPosition=Dposition
        idBox=['D','S','R','A','B','C']
        for i in range(6):
            self.agentList[(Dposition+i)%6].setIdentity(idBox[i])

    def round1(self):
        self.roundScoreList=[0 for i in range(6)]
        # Card Distrbution
        for i in range(6):
            handList=[]
            handList.append(self.cardPool.getCard())
            handList.append(self.cardPool.getCard())
            self.agentList[i].setHand(handList)

        # Blind Bet
        self.roundScoreList[S(self.DPosition)]+=self.agentList[S(self.DPosition)].bet(1)
        self.roundScoreList[R(self.DPosition)]+=self.agentList[R(self.DPosition)].bet(2)

        # Round1 Bet
        now=A(self.DPosition)
        top=2
        while self.roundScoreList[now] != top and self.foldNum < 6:
            if self.agentList[now].final == 0:
                bet=self.agentList[now].action(self.roundScoreList[now],top)
                # print(now,'bet',bet,top)
                if bet != 0 :
                    self.roundScoreList[now]=bet
                    top=bet
                else:
                    self.foldNum+=1
                    if self.foldNum == 6:
                        self.foldWinner=now
            now=(now+1)%6

        # Sum Up Score Pool
        for score in self.roundScoreList:
            self.scorePool+=score

        if self.debug:
            print('======Round1======')
            self.printEnv()
            self.printAgents()

    def round2(self):
        self.roundScoreList = [0 for i in range(6)]
        # Card Distrbution
        self.publicList=[]
        self.publicList.append(self.cardPool.getCard())
        self.publicList.append(self.cardPool.getCard())
        self.publicList.append(self.cardPool.getCard())

        # Round2 Bet
        now = S(self.DPosition)
        top = 2

        ## Small Blind Check
        if self.agentList[now].final == 0:
            bet = self.agentList[now].actionAllowCheck(self.roundScoreList[now],top)
            # print(now, 'bet', bet, top)
            if bet != 0:
                self.roundScoreList[now] = bet
                top = bet
        now = (now + 1) % 6

        ## Others bet
        while self.roundScoreList[now] != top and self.foldNum < 6:
            if self.agentList[now].final == 0:
                bet = self.agentList[now].action(self.roundScoreList[now],top)
                # print(now, 'bet', bet, top)
                if bet != 0:
                    self.roundScoreList[now] = bet
                    top = bet
                else:
                    self.foldNum+=1
                    if self.foldNum == 6:
                        self.foldWinner=now
            now = (now + 1) % 6

        # Sum Up Score Pool
        for score in self.roundScoreList:
            self.scorePool += score

        if self.debug:
            print('======Round2======')
            self.printEnv()
            self.printAgents()

    def round3(self):
        self.roundScoreList = [0 for i in range(6)]
        # Card Distrbution
        self.publicList.append(self.cardPool.getCard())

        # Round3 Bet
        now = S(self.DPosition)
        top = 2

        ## Small Blind Check
        if self.agentList[now].final == 0:
            bet = self.agentList[now].actionAllowCheck(self.roundScoreList[now],top)
            # print(now, 'bet', bet, top)
            if bet != 0:
                self.roundScoreList[now] = bet
                top = bet
        now = (now + 1) % 6

        ## Others bet
        while self.roundScoreList[now] != top and self.foldNum < 6:
            if self.agentList[now].final == 0:
                bet = self.agentList[now].action(self.roundScoreList[now],top)
                # print(now, 'bet', bet, top)
                if bet != 0:
                    self.roundScoreList[now] = bet
                    top = bet
                else:
                    self.foldNum+=1
                    if self.foldNum == 6:
                        self.foldWinner=now
            now = (now + 1) % 6

        # Sum Up Score Pool
        for score in self.roundScoreList:
            self.scorePool += score

        if self.debug:
            print('======Round3======')
            self.printEnv()
            self.printAgents()

    def round4(self):
        self.roundScoreList = [0 for i in range(6)]
        # Card Distrbution
        self.publicList.append(self.cardPool.getCard())

        # Round4 Bet
        now = S(self.DPosition)
        top = 2

        ## Small Blind Check
        if self.agentList[now].final == 0:
            bet = self.agentList[now].actionAllowCheck(self.roundScoreList[now],top)
            # print(now, 'bet', bet, top)
            if bet != 0:
                self.roundScoreList[now] = bet
                top = bet
        now = (now + 1) % 6

        ## Others bet
        while self.roundScoreList[now] != top and self.foldNum < 6:
            if self.agentList[now].final == 0:
                bet = self.agentList[now].action(self.roundScoreList[now],top)
                # print(now, 'bet', bet, top)
                if bet != 0:
                    self.roundScoreList[now] = bet
                    top = bet
                else:
                    self.foldNum+=1
                    if self.foldNum == 6:
                        self.foldWinner=now
            now = (now + 1) % 6

        # Sum Up Score Pool
        for score in self.roundScoreList:
            self.scorePool += score

        if self.debug:
            print('======Round4======')
            self.printEnv()
            self.printAgents()

    def win(self):
        for i in range(6):
            index,subindex=getCompet(self.publicList,self.agentList[i].hand)
            if isinstance(subindex,list):
                subindex=convertSubindex(subindex)
            self.agentCompetList.append((self.agentList[i].final,index,subindex,i))
        self.agentCompetList.sort(key=lambda tp:(tp[0],tp[1],-tp[2]))

        winnerIndex=self.agentCompetList[0][1]
        winnerSubindex=self.agentCompetList[0][2]
        winnerList=[self.agentCompetList[0][3]]
        for i in range(1,6):
            if self.agentCompetList[i][1] == winnerIndex and self.agentCompetList[i][2] == winnerSubindex:
                if self.agentCompetList[i][0] == 0:
                    winnerList.append(self.agentCompetList[i][3])

        finalScore=[agent.score for agent in self.agentList]
        if self.foldNum == 6:
            winnerList=[self.foldWinner]
        for winner in winnerList:
            finalScore[winner]+=self.scorePool/len(winnerList)

        return finalScore

    def printEnv(self):
        print('=========')
        print('Environment Follows')
        self.cardPool.print()
        if self.publicList == None:
            print('PublicList Empty')
        else:
            print('publicList:')
            for card in self.publicList:
                card.print()
        print('scorePool:',self.scorePool)
        print('RoundScore:',self.roundScoreList)
        print('Dposition:',self.DPosition)

    def printAgents(self):
        for agent in self.agentList:
            agent.print()

