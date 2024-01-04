import random
from hangman_words import word_list
from hangman_art import logo
print(logo)
from hangman_art import stages


end_of_game = False
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

lives  = 6

print(f"Pssst , the solution is {choosen_word}.")

display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter:\n").lower()
  
  if guess in display:
      print(f"You've already guessed {guess}")

  for position in range(word_length):
      letter = choosen_word[position]
      # print(f"Current position: {position} \n Current letter: {letter} \n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter
          
  if guess not in choosen_word:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You Lose!")
  print(f"{' '.join(display)}")

  
  if "_" not in display:
      end_of_game = True
      print("You Won!")
  
  
  from hangman_art import stages
  print(stages[lives])
    
        
          
      
    







