import random
import words
import arts
print(arts.logo)
chosen_word = random.choice(words.word_list)
lives = 6
print(arts.stages[lives])
display = ['_'] * len(chosen_word)
while '_' in display:
    if lives == 0:
        print(f"You lost, the word was {chosen_word}")
        break
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed letter {guess}")
        print(display)
        continue
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]
    if guess not in chosen_word:
        lives -= 1
        print(arts.stages[lives])
    print(*display)
if '_' not in display:
    print("You won!")
