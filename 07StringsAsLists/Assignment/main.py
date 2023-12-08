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



def in_alphabetical_order(letters):
    previous = letters[0]
    for letter in letters:
        if letter < previous:
            return False
        previous = letter
    return True










def alternate_case(word):
    result = ""
    next_upper = True
    for letter in word:
        if next_upper == True:
            result == result + letter.upper()
            next_upper = False
        elif next_upper == False:
            result = result + letter
            next_upper = True
    return result



def remove_vowels(letters):
    result = ""
    for letter in letters:
        if letter in "aeiou":
            pass
        else:
            result = result + letter
    return result



def to_camel_case(word):
    result = ""
    next_upper = True
    for letter in word:
        if next_upper == True:
             result = result + letter.upper()
             next_upper = False
        elif letter == " ":
            pass
            next_upper = True
        
print(to_camel_case("hello world"))

def to_snake_case(word):
    result = ""
    next_upper = True
    for letter in word:
        if next_upper == True:
             result = result + letter
             next_upper = False
        elif letter == " ":
            pass
            next_upper = True






    