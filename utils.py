import random

class CardPool():
    def __init__(self):
        self.bin=[0 for i in range(52)]

    def reset(self):
        self.bin=[0 for i in range(52)]

    def getCard(self):
        cardInt=random.randint(0,51)
        while self.bin[cardInt] == 1:
            cardInt = random.randint(0, 51)
        self.bin[cardInt]=1
        suit=int(cardInt/13)
        point=cardInt%13+1
        return Card(suit,point)

    def print(self):
        print('----------')
        print('cardPool:')
        print(self.bin)

class Card():
    def __init__(self,suit,point):
        self.suit=suit
        self.point=point

    def print(self):
        if self.suit == 0:
            print('黑桃',self.point)
        if self.suit == 1:
            print('红桃',self.point)
        if self.suit == 2:
            print('梅花',self.point)
        if self.suit == 3:
            print('方块',self.point)

def S(Dposition):
    return (Dposition+1)%6

def R(Dposition):
    return (Dposition + 2) % 6

def A(Dposition):
    return (Dposition + 3) % 6

def getCompet(publicList,hand):
    suitBox=[0 for i in range(4)]
    pointBox=[0 for i in range(13)]
    for card in publicList:
        suitBox[card.suit]+=1
        pointBox[card.point-1]+=1
    for card in hand:
        suitBox[card.suit]+=1
        pointBox[card.point-1]+=1

    index,subindex,done = 11,-1,False
    index, subindex, done =Top1_2(suitBox,publicList,hand)
    if done :
        return index, subindex
    index, subindex, done = Top3_4_7_8_9(pointBox)
    if done:
        if index >= 4:
            return index, subindex
        else:
            index5, subindex5, done5 = Top5(suitBox,publicList,hand)
            if done5:
                return index5, subindex5
            index6, subindex6, done6 = Top6(pointBox)
            if done6:
                return index6, subindex6
            return index, subindex
    index, subindex, done = Top10(pointBox)

    assert index != 11
    return index, subindex

def Top1_2(suitBox,publicList,hand):
    # Top1 : RSameShunzi
    # Top2 : SameShunzi
    suitTag=4
    for i in range(4):
        if suitBox[i] >= 5 :
            suitTag = i

    if suitTag == 4:
        return 11,-1,False

    pointSubbox=[0 for i in range(13)]
    for card in publicList:
        if card.suit == suitTag:
            pointSubbox[card.point-1]=1
    for card in hand:
        if card.suit == suitTag:
            pointSubbox[card.point-1]=1

    index,subindex,done=Top6(pointSubbox)
    if done :
        if subindex == 13:
            return 1,0,True
        else:
            return 2,subindex,True
    else:
        return 11,-1,False

def Top3_4_7_8_9(pointBox):
    # Top3 : 4+1
    # Top4 : 3+2
    # Top7 : 3+1+1
    # Top8 : 2+2+1
    # Top9 : 2+1+1+1
    same4=[]
    same3=[]
    same2=[]
    same1=[]
    for i in range(13):
        if pointBox[12-i] == 1:
            same1.append(12-i)
        if pointBox[12-i] == 2:
            same2.append(12-i)
        if pointBox[12-i] == 3:
            same3.append(12-i)
        if pointBox[12-i] == 4:
            same4.append(12-i)

    # Check Top3
    if len(same4) != 0:
        subindex=[same4[0]]
        pt=-1
        if len(same3) != 0 :
            pt=max(pt,same3[0])
        if len(same2) != 0 :
            pt=max(pt,same2[0])
        if len(same1) != 0 :
            pt=max(pt,same1[0])
        subindex.append(pt)
        return 3,subindex,True

    # Check Top4
    if len(same3) != 0:
        subindex=[same3[0]]
        pt=-1
        if len(same3) != 1:
            pt=max(pt,same3[1])
        if len(same2) != 0 :
            pt=max(pt,same2[0])
        if pt != -1:
            subindex.append(pt)
            return 4,subindex,True

    # Check Top7
    if len(same3) == 1:
        subindex=[same3[0],same1[0],same1[1]]
        return 7,subindex,True

    # Check Top8
    if len(same2) >= 2:
        subindex=[same2[0],same2[1]]
        if len(same2) == 3:
            pt=max(same2[2],same1[0])
            subindex.append(pt)
        if len(same2) == 2:
            subindex.append(same1[0])
        return 8,subindex,True

    # Check Top9
    if len(same2) == 1:
        subindex=[same2[0],same1[0],same1[1],same1[2]]
        return 9,subindex,True

    return 11,-1,False

def Top5(suitBox,publicList,hand):
    # Top5 : Same suit
    suitTag = 4
    for i in range(4):
        if suitBox[i] >= 5:
            suitTag = i

    if suitTag == 4:
        return 11, -1, False

    pointSubbox = [0 for i in range(13)]
    for card in publicList:
        if card.suit == suitTag:
            pointSubbox[card.point-1] = 1
    for card in hand:
        if card.suit == suitTag:
            pointSubbox[card.point-1] = 1

    index, subindex, done = Top10(pointSubbox)
    return 5,subindex,True

def Top6(pointBox):
    # Top6 : Shunzi
    start,end,sum=9,13,0

    for i in range(start,end):
        if pointBox[i] != 0:
            sum+=1
    if pointBox[0] !=0:
        sum+=1
    start-=1
    end-=1
    if sum == 5:
        return 6,13,True

    while start != -1:
        if pointBox[(end+1)%13] != 0:
            sum-=1
        if pointBox[start] != 0:
            sum+=1
        start -= 1
        end -= 1
        if sum == 5:
            return 6, end, True

    return 11,-1,False

def Top10(pointBox):
    # Others
    subindex=[]
    for i in range(13):
        for j in range(pointBox[12 - i]):
            subindex.append(12-i)
    return 10, subindex, True

def convertSubindex(subindex):
    ans=0
    n=len(subindex)
    for i in range(n):
        ans+=pow(13,n-i)*subindex[i]
    return int(ans)