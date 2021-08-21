import random

class Agent():
    def __init__(self,name):
        self.name=name

        self.identity=None
        self.hand=None
        self.score=100
        self.final=0

    def reset(self):
        self.identity = None
        self.hand = None
        self.score = 100
        self.final = 0

    def setIdentity(self,identity):
        self.identity=identity

    def setHand(self,handList):
        self.hand=handList

    def bet(self,score):
        self.score-=score
        return score

    def action(self,last,lowerbound):
        '''
        Make desicion, algorithm should be implement.
        The demo is random policy described in the manner.

        :param lowerbound: Int, the lowerlound of the bet
        :return: actual bet
        '''
        # Score Not Enough
        if self.score+last < lowerbound:
            return self.allin()

        # Score Enough
        randFloat=random.random()
        if randFloat <= 8/10:
            self.score+=last
            return self.call(lowerbound)
        elif randFloat<=9/10:
            self.score += last
            return self.raising(lowerbound)
        else:
            return self.fold()

    def actionAllowCheck(self,last,lowerbound):
        '''
        Make desicion, algorithm should be implement.
        The demo is random policy described in the manner.
        Attention is check allowed.

        :param lowerbound: Int, the lowerlound of the bet
        :return: actual bet
        '''
        # Score Not Enough
        if self.score+last < lowerbound:
            return self.allin()

        # Score Enouth
        randFloat = random.random()
        if randFloat <= 5 / 10:
            self.score += last
            return self.call(lowerbound)
        elif randFloat <= 9 / 10:
            self.score += last
            return self.raising(lowerbound)
        else:
            return self.check()

    def call(self,score):
        return self.bet(score)

    def raising(self,lowerbound):
        randomFloat=random.random()
        return self.bet((self.score-lowerbound)*randomFloat+lowerbound)

    def fold(self):
        self.final=1
        return 0

    def check(self):
        return 0

    def allin(self):
        return self.bet(self.score)

    def print(self):
        print('--------------')
        print('name:',self.name)
        print('identity',self.identity)
        print('score:',self.score)
        if self.hand == None:
            print('Hand Empty')
        else:
            self.hand[0].print()
            self.hand[1].print()
        if self.final == 0:
            print('Alive')
        else:
            print('Folded')