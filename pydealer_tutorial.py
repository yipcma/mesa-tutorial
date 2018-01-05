import pydealer
from pydealer.const import POKER_RANKS

# If you want it shuffle when rebuilding, with rank:
deck = pydealer.Deck(rank=POKER_RANKS, rebuild=True, re_shuffle=True)

# sort the deck by its rank
deck.sort()

# shuffle the deck
deck.shuffle()

# construct a Stack instance for discard pile
discard = pydealer.Stack()
hand = pydealer.Stack()

# deal cards to hand from a stack/deck
print(deck[0:6])

# add cards to stack, default end="top"
hand.add(deck.deal(3))

print(deck[0:6])
print(hand)

# empty a stack to discard pile
discard.add(hand.empty(return_cards=True))
print(hand)
print(discard)

# size of stack
deck.size

