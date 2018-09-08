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
    cardArray = [-1]*10;
    i = 0;
    count = 0
    while i < 10:
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
    minCount = 100000
    maxCount = 0

    for i in range(0,itCount):
        count = run_one(numCards);
        if count < minCount:
            minCount = count
        if count > maxCount:
            maxCount = count
        totalCount = totalCount + run_one(numCards);
    print float(totalCount) / itCount
    print maxCount
    print minCount
    return totalCount


run_sim(10000, 100);
print ""
run_sim(10000, 300);
