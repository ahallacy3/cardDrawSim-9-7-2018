import random

def run_one(numCards):
    cardArray = [-1] * numCards
    count = 0
    while not checkSet(cardArray):
        cards = drawCards(numCards);
        cardArray = addCards(cards, cardArray);
        count = count + 1
    return count


def drawCards(numCards):
    packSize = 10
    cardArray = [-1]*packSize;
    i = 0;
    count = 0
    while i < packSize:
        card = random.randint(1,numCards);
        j = 0;
        notFound = True;
        while j < i and notFound:
            if cardArray[j] == card:
                i = i - 1;
                notFound = False;
            j = j + 1
        if notFound:
            cardArray[i] = card;
        i = i + 1
    return cardArray

def checkSet(cardArray):
    for i in range(0, len(cardArray)):
        if cardArray[i] != i + 1:
            return False;
    return True;

def addCards(newCards, cardArray):
    for i in range(0, len(newCards)):
        cardArray[newCards[i] - 1] = newCards[i];
    return cardArray

def run_sim(itCount, numCards):
    totalCount = 0
    for i in range(0,itCount):
        count = run_one(numCards);
        totalCount = totalCount + count;
    return float(totalCount) / itCount


print "Average Number of 10 card packs needed to get 100 Cards: ", run_sim(10000, 100);
print ""
#Can take a long time to run. Reduce first input to reduce iterations and run time
print "Average Number of 10 card packs needed to get 300 Cards: ", run_sim(10000, 300);
