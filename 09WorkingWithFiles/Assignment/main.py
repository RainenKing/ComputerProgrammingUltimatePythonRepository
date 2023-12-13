import csv

f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()

def most_vowels(words):
    total = 0
    for word in words:
        if word in "aeiou":
            total = total + 1
    return total

print(most_vowels(words))

