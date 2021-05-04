import random
import copy 
import dealer
import os

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')


clear()
print('Made by Meh6446')
print('\nIt was really fun making this, was a challenge too\nPlease let me know if you found any bugs\n')
print('Discord: Meh6446#6446')
input('Hope you enjoy it as much as i did!!!')
print("\nWould you like to turn on betting?")
betting_on = input("[Y/N] > ").lower()
print("")
if betting_on == 'y':
  betting = True
  player_wallet = 100
elif betting_on == 'n':
  betting = False

# Meh6446 : Game setup
keep_playing = True
clear()
while keep_playing:
  playing_deck = copy.copy(dealer.the_deck)
  player_hand = []
  player_score = 0
  dealer_hand = []
  dealer_score = 0

#show players hand and total
  player_hand.append(dealer.draw_card(playing_deck))
  player_hand.append(dealer.draw_card(playing_deck))
  player_score = dealer.compute_score(player_hand)
  print("Starting hand: " + dealer.cards_in_hand(player_hand))
  print("Total: " + str(player_score))
  if betting == True:
    print("Player Credits: " + str(player_wallet))
  print("")
 
#bet code
  player_bet = 0
  if betting == True:
      while player_bet == 0:
        try:
          player_bet = int(input("How many credits would you like to bet?\n> "))
          if player_bet > player_wallet:
            print("\nYou don't have that many credits to bet\n")
            player_bet = 0
        except:
          print("\nThat's not a number lol\n")
          player_bet = 0
  print("")
  
#game loop
  in_game = True
  player_wins = None
  while in_game:
    print("Would you like to draw a card?")
    keep_going = input("Hit or Stand\n[H/S] > ").lower()
    print('')
#if player hit
    if keep_going == "h":
      clear()
      player_hand.append(dealer.draw_card(playing_deck))
      player_score = dealer.compute_score(player_hand)
      if player_score > 21:
        print("Current hand: " + dealer.cards_in_hand(player_hand))
        print("Current Total: " + str(player_score))
        print('')
        print("Oh no!  You went bust!")
        player_wins = False
        in_game = False
      elif player_score == 21:
        print("Current hand: " + dealer.cards_in_hand(player_hand))
        print("Current Total: " + str(player_score))
        print('')
        print("BLACKJACK!!! You Win!")
        player_wins = True
        in_game = False      
      elif len(player_hand) > 4:
        print("Wow!  You got a 'Five Card Charlie'!  You Win!")
        player_wins = True
        in_game = False
      else:
        print("Current hand: " + dealer.cards_in_hand(player_hand))
        print("Current Total: " + str(player_score) + "\n")
#when the player stands the dealer draws/code for dealer
    elif keep_going == "s":
      clear()
      print("Now the dealer will draw.")
      dealer_hand.append(dealer.draw_card(playing_deck))
      dealer_hand.append(dealer.draw_card(playing_deck))
      dealer_score = dealer.compute_score(dealer_hand)
      while dealer_score < 16:
        dealer_hand.append(dealer.draw_card(playing_deck))
        dealer_score = dealer.compute_score(dealer_hand)
      print("Dealer's hand: " + dealer.cards_in_hand(dealer_hand))
      print("Dealer's Total: " + str(dealer_score))
      print('')
      if dealer_score > 21:
        print("The dealer went bust!  You win!")
        player_wins = True
        in_game = False
      elif len(dealer_hand) > 4:
        print("The dealer got a 'Five Card Charlie'.  You lose!")
        player_wins = False
        in_game = False
      elif dealer_score == 21:
        print("Dealer's BLACKJACK!!! You Lose!")
        player_wins = False
        in_game = False
      elif dealer_score >= player_score:
        print("The dealer beat you!  You lose!")
        player_wins = False
        in_game = False
      else:
        print("You beat the dealer!  You win!")
        player_wins = True
        in_game = False
#betting total/added to player's wallet if win
  if betting == True:
    if player_wins == True:
      print("\nYour hand: " + dealer.cards_in_hand(player_hand))
      input('')
      player_wallet = player_wallet + player_bet
    elif player_wins == False:
      print("\nYour hand: " + dealer.cards_in_hand(player_hand))
      input('')
      player_wallet = player_wallet - player_bet
    if player_wallet < 1:
      print("You've run out of credits!\nGame Over!")
      break
  
  check_continue = input("\nContinue Playing?\n[Y/N] > ").lower()
  if check_continue == "n":
    print("See you next time!!!")
    keep_playing = False  
  elif check_continue == "y":
    clear()
    print('\n##### NEW GAME #####\n')

