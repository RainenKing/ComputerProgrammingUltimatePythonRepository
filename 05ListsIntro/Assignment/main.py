def make_abc():
    result = ["a", "b", "c"]
    return result

print("make the abc:")
print(make_abc())



def equal_edges(items):
    first = items[0]
    last = items [-1]
    
    if first == last:
        return True
    else:
        return False

print("equal_edges")
print(equal_edges([9, 6, 7, 5, 9]))
print(equal_edges([9, 6, 7, 5, 4]))



def common_edge(list1, list2):
    first1 = list1[0]
    first2 = list2[0]
    last1 = list1[2]
    last2 = list2[2]

    if first1 or last1 == first2 or last2:
        return True
    else:
        return False

print("common_edge")   
print(common_edge([1, 2, 3], [3, 2, 3]))
print(common_edge([3, 5, 1], [9, 5, 6]))



def all_the_same(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]

    if first == middle and first == last:
        return True
    else:
        return False

print("all_the_same")
print(all_the_same([9, 9, 9]))
print(all_the_same([4, 7, 4]))



def all_unique(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]

    if first != last and first != middle and middle != last:
        return True
    else:
        return False

print("all_unique")
print(all_unique([1, 2, 3]))
print(all_unique([4, 4, 4]))



def increasing(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]

    if first < middle and middle < last:
        return True
    else:
        return False

print("increasing")
print(increasing([1, 2, 3]))
print(increasing([2, 1, 3]))



def all_true(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]

    if first == True and middle == True and last == True:
        return True
    else:
        return False
    
print("all_true")
print(all_true([True, True, True]))
print(all_true([True, False, True]))


def mostly_true(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]

    if first == True and middle == True and last == True or first == True and middle == True or first == True and last == True or middle == True and last == True:
        return True
    else:
        return False

print("mostly_true")
print(mostly_true([True, True, True]))
print(mostly_true([True, False, True]))
print(mostly_true([False, False, True]))










def make_copy(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]

    return [first, middle, last]

print("make_copy")
original_list = [5, 4, 7]
new_list = make_copy(original_list)
print("original list: ", original_list)
print("new list: ", new_list)



def repeat_thrice(list1):
    first = list1[0]

    return [first, first, first]

print("repeat thrice")
print(repeat_thrice([1]))
print(repeat_thrice([5]))



def reverse_in_copy(list1):
    first = list1[0]
    middle = list1[1]
    last = list1[2]
   

    return [last, middle, first]

print("reverse_in_copy")
original_list = [4, 7, 2]
new_list = reverse_in_copy(original_list)
print("original list: ", original_list)
print("new list: ", new_list)



def reverse_in_place(list1):
    first = list1[2]
    middle = list1[1]
    last = list1[0]
    return [first, middle, last]

print("reverse in place")
original_list1 = [4, 3, 2]
original_list2 = reverse_in_place(original_list1)
new_list2 = reverse_in_place(original_list1)
print("original List:", original_list2)
print("new list:", new_list2)









