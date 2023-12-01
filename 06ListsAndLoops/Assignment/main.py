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