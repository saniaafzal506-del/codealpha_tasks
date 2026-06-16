# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 03:07:17 2026

@author: Administrator
"""

import random

# 5 predefined words
words = ["python", "github", "codealpha", "laptop", "internet"]
secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("🎮 Welcome to Hangman Game!")
print(f"Hint: Word me {len(secret_word)} letters hain")
print("_ " * len(secret_word))
print(f"Aapke paas {max_incorrect} galat guesses hain\n")

while incorrect_guesses < max_incorrect:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("Word:", display_word)
    
    if "_" not in display_word:
        print("\n🎉 Mubarak ho! Aap jeet gaye. Word tha:", secret_word)
        break
    
    guess = input("1 letter guess karo: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Sirf 1 letter likho a-z tak!\n")
        continue
    
    if guess in guessed_letters:
        print("Ye letter pehle try kar chuke ho!\n")
        continue
    
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print("✅ Sahi guess!\n")
    else:
        incorrect_guesses += 1
        print(f"❌ Galat guess! Baqi chances: {max_incorrect - incorrect_guesses}\n")

if incorrect_guesses == max_incorrect:
    print(f"💀 Game Over! Word tha: {secret_word}")