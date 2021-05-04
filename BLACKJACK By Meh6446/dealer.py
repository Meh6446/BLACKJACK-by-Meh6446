import random

#deck tuple
the_deck = [("A♡", 11), ("2♡", 2), \
("3♡", 3), ("4♡", 4), \
("5♡", 5), ("6♡", 6), \
("7♡", 7), ("8♡", 8), \
("9♡", 9), ("10♡", 10), \
("J♡", 10), ("Q♡", 10), \
("K♡", 10), ("A♤", 11), \
("2♤", 2), ("3♤", 3), \
("4♤", 4), ("5♤", 5), \
("6♤", 6), ("7♤", 7), \
("8♤", 8), ("9♤", 9), \
("10♤", 10,), ("J♤", 10), \
("Q♤", 10), ("K♤", 10), \
("A♢", 11), ("2♢", 2), \
("3♢", 3), ("4♢", 4), \
("5♢", 5), ("6♢", 6), \
("7♢", 7), ("8♢", 8), \
("9♢", 9), ("10♢", 10), \
("J♢", 10), ("Q♢", 10), \
("K♢", 10), ("Ace♧", 11), \
("2♧", 2), ("3♧", 3), \
("4♧", 4), ("5♧", 5), \
("6♧", 6), ("7♧", 7), \
("8♧", 8), ("9♧", 9), \
("10♧", 10), ("J♧", 10), \
("Q♧", 10), ("K♧", 10)]

#Meh6446: take an object from list, remove it then return it to a list for player's hand 
def draw_card(x):
  drawn_card = random.choice(x)
  x.remove(drawn_card)
  return drawn_card

#Meh6446: score process/takes int from the deck tuple and puts them in a list of values
def compute_score(x):
  total = 0
  value_set = []
  for i in x:
    value_set.append(i[1])  
  total = sum(value_set)
  ace_check = True
  while ace_check == True:#Meh6446: check if any card is 11 when over 21, if so then turns the card to 1
    if total > 21 and 11 in value_set:
      value_set.remove(11)
      value_set.append(1)
      total = sum(value_set)
    else:
      ace_check = False
  return total

#Meh6446: this function is not really needed but it helps with the readability.
def cards_in_hand(x):
  hand = []
  for i in x:
    hand.append(i[0])
  handstring = hand[0]
  for i in hand[1:]:
    handstring = handstring + ', ' + i
  return handstring