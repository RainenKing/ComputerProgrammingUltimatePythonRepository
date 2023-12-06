def is_alliteration(word1, word2):
    if word1[0] == word2[0]:
        return True
    return False



def count_vowels(letters):
    total = 0
    for letter in letters:
        if letter in "aeiou":
            total = total + 1
    return total



def count_numbers(nums):
    total = 0
    for num in nums:
        if num in "1234567890":
            total = total + 1
    return total



def count_target_letters(words, letters):
    total = 0
    for word in words:
        if letters in word:
             total = total + 1
    return total


    