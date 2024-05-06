import sys
import random
from word_date import words

def main():
  game()


def game():
  user_input = welcome_message() 
  
  
  if user_input in ['y', 'yes']:
    
    item = random.choice(words)
    word_to_guess = item['word'] 
    hints = item['hints'] 
    lives = 5
    
    updated_version = placeholder(word_to_guess)
    print(f"\nguess this\n{placeholder(word_to_guess)}\n*hints: {hints[0]}")
    for i in range(len(word_to_guess)):
      while lives > 0 :
        player_guess = input("choose a letter >> ").strip().lower()
        if player_guess == 'exit':
          sys.exit()
        else:
          if player_guess == word_to_guess[i]:
            updated_version = updated_version.replace('-',player_guess,1)
            if word_to_guess == updated_version:
              print(f"you win it's {updated_version} :))")
            else:
              print("yay you got it right")
              print(updated_version)
            break
          else:
            lives -= 1
            print(f'you got it wrong\nboat lives:{lives}')
            if lives <= 1:
              print(f"take this hint: {hints[lives]}")
          
          
          
        
    
    
  else:
    sys.exit('see you later :)')
  
def welcome_message():
   start_the_game = input("Welcome to save your boat game :D\n\nDescription :\n1)- you have a boat that have 5 lives when boat lives end it will drown\n2)- you should guess the word by choosing a letter from the English alphabet\n3)- if you got the letter wrong you will lose a live\n4)- when you guess the letter right you will be provided with the updated word\n5)- if you guess everthing right you will win\n6)- if you finish your lives and did not guess the word you will lose\n7)- to quit you can write exit.\n\nwanna play ?(y,n) ").strip().lower()
  
   return start_the_game
 
def placeholder(word):
  return len(word) * '-'

  
if __name__ == '__main__':
  main()