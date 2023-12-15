import csv
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")



def find_most_vowels(wordlist):
    most_so_far = ""
    max_vowelcount = 0

    for word in wordlist:
        current_vowelcount = 0
        for letter in word:
            if letter== "a" or letter== "e" or letter== "i" or letter== "o" or letter== "u":
                current_vowelcount = current_vowelcount + 1
        if current_vowelcount > max_vowelcount:
            max_vowelcount = current_vowelcount
            most_so_far = word
    return most_so_far

print(find_most_vowels(words))



def average_word_legth(wordlist):