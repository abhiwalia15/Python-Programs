blackjack=[4, 11, 8, 5, 13, 2, 8, 10]
hand=[]
while sum(hand)<=17:
  hand.append(blackjack.pop())
print(hand)