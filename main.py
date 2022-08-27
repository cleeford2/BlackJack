############### Blackjack Project #####################
import random
from replit import clear
from art import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """Returns a random card from the deck"""
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score from the calculated cards"""
#Find blackjack
  if sum(cards) == 21 and cards(len) == 2:
    return 0 #zero represent blackjack
    
# If the score is already over 21, remove the 11 and replace it with a 1.
  if 11 in cards and sum(cards) > 21:
    cards.revome(11)
    cards.append(1)

  return sum(cards)

def compare(user_score, computer_score):
  """Compare two scores to determine winner"""
  #compare computer and user score
  if user_score == computer_score:
    return "It's a draw"
  elif computer_score == 0:
    return "he Computer has won..."
  elif user_score == 0:
    return "You win!!"
  elif user_score > 21:
    return "You went over. Computer win..."
  elif computer_score > 21:
    return "Computer went over. You win"
  elif user_score > computer_score:
    return "You win!!!"
  else:
    return "You lose..."
    
def play_game():

  print(logo)
  
  #Deal computer and user two sets of random cards
  user_cards = []
  computer_cards = []
  game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_over:
    #User and computer score
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"   You draw:{user_cards}, and your current score is: {user_score}")
    print(f"   The computer's first card is: {computer_cards[0]}")
    
    # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
      
    if user_score == 0 or computer_score == 0 or user_score > 21:
      print("Game over")
      game_over = True
    else:
      answer = input("Type 'y' to draw another card or 'n' if you want to pass:\n")
      if answer == "y":
        user_cards.append(deal_card())
      else:
        game_over = True
  
  # The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(   f"Your final hand is: {user_score}")
  print(   f"The computer's final hand is: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
  clear()
  play_game()

