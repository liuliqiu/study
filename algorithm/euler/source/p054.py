##In the card game poker, a hand consists of five cards and are ranked, from
##lowest to highest, in the following way:
##High Card: Highest value card.
##One Pair: Two cards of the same value.
##Two Pairs: Two different pairs.
##Three of a Kind: Three cards of the same value.
##Straight: All cards are consecutive values.
##Flush: All cards of the same suit.
##Full House: Three of a kind and a pair.
##Four of a Kind: Four cards of the same value.
##Straight Flush: All cards are consecutive values of same suit.
##Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
##The cards are valued in the order:
##2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
##If two players have the same ranked hands then the rank made up of the highest
##value wins; for example, a pair of eights beats a pair of fives (see example 1
##below). But if two ranks tie, for example, both players have a pair of queens,
##then highest cards in each hand are compared (see example 4 below); if the
##highest cards tie then the next highest cards are compared, and so on.
##Consider the following five hands dealt to two players:
##Hand	 	Player 1	 	Player 2	 	Winner
##1	 	5H 5C 6S 7S KD
##Pair of Fives
## 	2C 3S 8S 8D TD
##Pair of Eights
## 	Player 2
##2	 	5D 8C 9S JS AC
##Highest card Ace
## 	2C 5C 7D 8S QH
##Highest card Queen
## 	Player 1
##3	 	2D 9C AS AH AC
##Three Aces
## 	3D 6D 7D TD QD
##Flush with Diamonds
## 	Player 2
##4	 	4D 6S 9H QH QC
##Pair of Queens
##Highest card Nine
## 	3D 6D 7H QD QS
##Pair of Queens
##Highest card Seven
## 	Player 1
##5	 	2H 2D 4C 4D 4S
##Full House
##With Three Fours
## 	3C 3D 3S 9S 9D
##Full House
##with Three Threes
## 	Player 1
##The file, poker.txt, contains one-thousand random hands dealt to two players.
##Each line of the file contains ten cards (separated by a single space): the
##first five are Player 1's cards and the last five are Player 2's cards. You
##can assume that all hands are valid (no invalid characters or repeated cards),
##each player's hand is in no specific order, and in each hand there is a clear
##winner.
##How many hands does Player 1 win?
def trannum(s):
    if s=='T':
        return 10
    if s=='J':
        return 11
    if s=='Q':
        return 12
    if s=='K':
        return 13
    if s=='A':
        return 14
    return int(s)
def p(pokers):
    num=[]
    col=[]
    value=0
    for p in pokers:
        col.append(p[1])
        num.append(trannum(p[0]))
    if len(set(col))==1:
        value=value+5
    s={}
    for n in num:
        if n in s:
            s[n]=s[n]+1
        else:
            s[n]=1
    rs={}
    for n in s:
        if s[n] in rs:
            rs[s[n]].append(n)
        else:
            rs[s[n]]=[n]
    if 4 in rs:
        value=value+7
    elif 3 in rs and 2 in rs:
        value=value+6
    elif 3 in rs:
        value=value+3
    elif 2 in rs:
        if len(rs[2])==2:
            value=value+2
        else:
            value=value+1
    re=[]
    for i in range(4,0,-1):
        if i in rs:
            for j in range(14,1,-1):
                if j in rs[i]:
                    for k in range(i):
                        re.append(j)
    if re[0]==re[1]+1==re[2]+2==re[3]+3==re[4]+4:
        value=value+4
    return (value,)+tuple(re)
def p1(pokers):
    s1=p(pokers[:5])
    s2=p(pokers[5:])
    return s1>s2 
def fi():
    f=open('txt\\poker.txt')
    re=0
    for s in f:
        s=s.strip()
        if s!='' and p1(s.split(' ')):
            re=re+1
    print(re)
##v=('3C 3D 3S 9S 9D').split(' ')
##print(p(v))
fi()
