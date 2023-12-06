def count_failing_grades(grades):
    count = 0
    for grade in grades:
        if grade <= 60:
            count = count + 1
    return count

print("count_failing_grades")
inputlist = [83, 73, 54, 37, 60]
returnvalue = count_failing_grades(inputlist)
print(returnvalue)



def count_act_scores(scores):
    count = 0
    for score in scores:
        if score <= 36 and score >=1:
            count = count + 1
    return count

print("count_act_scores")
inputlist = [1, 36, 25, 38, 6]
returnvalue = count_act_scores(inputlist)
print(returnvalue)



def number_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

print("number_sum")
inputlist=[3, 7, 5]
returnvalue = number_sum(inputlist)
print(returnvalue)



def average_act_score(acts):
    count = 0
    total = 0
    for act in acts:
        if act <= 36 and act>= 1:
            total = total + act
            count = count + 1
    return total / count

print("average_act_score")
inputlist=[3, 12, 54, 32, 27, 38, 24]
returnvalue = average_act_score(inputlist)
print(returnvalue)










def all_true(booleans):
    
    for booleans in booleans:
        if booleans not in [True]:
           return False
    return True
        

print("all_true")
print(all_true([True, True, True, True, True]))
print(all_true([True, False, True, True, True]))



def any_true(booleans):
    
    for booleans in booleans:
        if booleans == True:
           return True
    return False
        

print("any_true")
print(any_true([False, True, False, True, True]))
print(any_true([False, False, False, False, False]))



def has_vowel(letters):
    
    for letters in letters:
        if letters in ["a", "e", "i", "o", "u"]:
           return True
    return False
        

print("has_vowel")
print(has_vowel(["d", "n", "r", "f", "c"]))
print(has_vowel(["f", "s", "r", "n", "a"]))



def mostly_true(Booleans):
    count = 0
    countF = 0
    for Boolean in Booleans:
        if Boolean == True:
            count += 1
        if Boolean == False:
            countF += 1

    if count > countF:
            return True
    return False

print("mostly_True")
print(mostly_true([True, True, False]))
print(mostly_true([False, False, True]))










def all_the_same(nums):

    first = nums[0]

    for num in nums:
        if num != first:
            return False
    return True


       
print("all_the_same")
print(all_the_same([5, 5, 5, 5, 5]))
print(all_the_same([4, 7, 3, 5, 1]))



def sum_with_skips(nums):
    total = 0
    ignoring = False

    for num in nums:
        if ignoring == True:
            if num == -1:
                ignoring = False
        elif ignoring == False:
            if num == -1:
                ignoring = True
            else:
                total = total + num
        print(num, ignoring)
    return total

print("sum_with_skips")
print(sum_with_skips([4, 2, -1, 3, -1, 4]))



def is_incrementing(nums):
    previous = nums[0]-1
    for num in nums:
        if num != previous + 1:
            return False
    return True



def increasing(nums):
    previous = nums[0]-1
    for num in nums:
        if num <= previous:
            return False
        previous = num
    return True

print("increasing")
print(increasing(1, 2, 3, 4, 5))
print(increasing(7, 2, 5, 6, 9))



def has_adjacent_repeat(nums):
    previous = nums[0]-1
    for num in nums:
        if num == previous:
            return True
        previous = num
    return False


    
