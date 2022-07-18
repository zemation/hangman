import random
import words

def main():
    print("Welcome to unoriginal Hangman.")

    print(the_game())


def the_game():
    the_word = random.choice(words.word_list).lower()
    display = []
    lives = 6
    for letter in the_word:
        if letter == " ":
            display += " "
        else:
            display += "_"
    
    while lives != 0:
        print(f"number of lives {lives}")
        guess = input("Pick a letter: ") 
        if guess in display:
            print("You've already used that letter. Lose a life")
            lives -= 1
        elif guess not in the_word:
            print("This is a wrong choice. Lose a Life")
            lives -= 1
        
        else:
            for letter in range(len(the_word)):
                if the_word[letter] == guess:
                    display[letter] = guess
            print(display)
            if "".join(display) == the_word:
                return "You win"

    else:
        return "You lose"
   
 


 



    
       


if __name__ == "__main__":
    main()