from collections import defaultdict
import sys


def getKind(hand):
  cards = defaultdict(int)
  for card in hand:
    cards[card] += 1

  # ugly code, basically replaces "J" with highest card if needed
  if part == "p2" and len(cards) > 1 and "J" in hand:
    sortedCards = defaultdict(int)
    # sort cards high-low
    for card, value in sorted(cards.items(), key=lambda x: x[1], reverse=True):
      sortedCards[cardmap[card]] = value

    # get highest card
    for sortKey, _ in sortedCards.items():
      if sortKey != cardmap["J"]:
        maxCard = [x for (x, y) in cardmap.items() if y == sortKey][0]
        break

    # re-arranging cards due to above change
    cards = defaultdict(int)
    for card in hand.replace("J", maxCard):
      cards[card] += 1

  # getting kind of each hand, can be made cleaner
  values = sorted(list(cards.values()))
  if values == [5]:
    return 7
  elif values == [1, 4]:
    return 6
  elif values == [2, 3]:
    return 5
  elif values == [1, 1, 3]:
    return 4
  elif values == [1, 2, 2]:
    return 3
  elif values == [1, 1, 1, 2]:
    return 2
  elif values == [1, 1, 1, 1, 1]:
    return 1
  return -1


def sortHandsForKind(hands):
  handvalues = defaultdict(list)
  for hand in hands:
    handvalue = []
    for card in hand:
      handvalue.append(cardmap[card])
    handvalues[hand] = handvalue

  sortedhands = sorted(handvalues.items(), key=lambda x: x[1], reverse=True)
  return [x for (x, _) in sortedhands]


with open(sys.argv[1], "r") as f:
  lines = [l.strip() for l in f.read().split("\n")]
  part = sys.argv[2]

  # mapping each card to relevant value
  cardmap = defaultdict(int)
  cardmap["A"] = 14
  cardmap["K"] = 13
  cardmap["Q"] = 12
  cardmap["J"] = 1 if part == "p2" else 11
  cardmap["T"] = 10
  for i in range(9, 1, -1):
    cardmap[str(i)] = i

  hands = defaultdict(int)
  handBids = defaultdict(int)

  # store bid and kind of each hand
  for line in lines:
    hand, bid = line.split(" ")
    handBids[hand] = int(bid)
    kind = getKind(hand)
    hands[hand] = kind

  # sorting hands for each of the 7 kinds
  sortedHands = []
  for i in range(7, 0, -1):
    for l in sortHandsForKind([k for k, v in hands.items() if v == i]):
      sortedHands.append(l)

  # calculate rank for all hands
  rank = len(sortedHands)
  ans = 0
  for hand in sortedHands:
    ans += rank * handBids[hand]
    rank -= 1

  print(f"Answer for {part}: {ans}")
